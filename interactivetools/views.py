import csv
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import RecyclableItem, CarbonFootprint
from .forms import RecyclableItemForm


def search_csv(item_name):
    try:
        with open('recyclable_items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name'].strip().lower() == item_name.strip().lower():
                    return row['description']
    except FileNotFoundError:
        return None
    return None


def searchable_database(request):
    query = request.GET.get('q')
    results = []
    form = RecyclableItemForm(request.POST or None)
    item_added = False  # Flag to indicate if an item was added

    if query:
        results = RecyclableItem.objects.filter(Q(name__icontains=query))
        if not results.exists():
            description = search_csv(query)
            if description:
                item = RecyclableItem(name=query, description=description)
                item.save()
                results = RecyclableItem.objects.filter(Q(name__icontains=query))

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Item added successfully!')
        return redirect('searchable_database')  # Redirect to clear the form after submission

    return render(request, 'interactivetools/searchable_database.html', {
        'query': query,
        'results': results,
        'form': form,
        'item_added': item_added  # Pass the flag to the template
    })


CARBON_FOOTPRINT_CATEGORIES = {
    'Low': {
        'range': (0, 1000),
        'suggestions': [
            "Maintain your low emissions by continuing to use public transportation or walking.",
            "Consider renewable energy options for your home."
        ]
    },
    'Moderate': {
        'range': (1001, 5000),
        'suggestions': [
            "Carpool or use public transportation more often.",
            "Reduce your energy consumption by turning off lights and appliances when not in use."
        ]
    },
    'High': {
        'range': (5001, 10000),
        'suggestions': [
            "Consider switching to an electric or hybrid vehicle.",
            "Implement more energy-efficient appliances in your home."
        ]
    },
    'Very High': {
        'range': (10001, float('inf')),
        'suggestions': [
            "Significantly reduce car travel and opt for public transportation.",
            "Invest in home insulation and renewable energy sources."
        ]
    }
}

def categorize_carbon_footprint(value):
    for category, details in CARBON_FOOTPRINT_CATEGORIES.items():
        if details['range'][0] <= value <= details['range'][1]:
            return category, details['suggestions']
    return None, []

def carbon_footprint_calculator(request):
    carbon_footprint = None
    category = None
    suggestions = []
    if request.method == 'POST':
        miles_per_week = int(request.POST.get('miles'))
        carbon_footprint_value = miles_per_week * 52 * 0.404  # Approximate kg CO2 per mile driven
        category, suggestions = categorize_carbon_footprint(carbon_footprint_value)
        carbon_footprint = CarbonFootprint.objects.create(
            miles_per_week=miles_per_week,
            carbon_footprint=carbon_footprint_value,
            category=category
        )
    return render(request, 'interactivetools/carbon_footprint_calculator.html', {
        'carbon_footprint': carbon_footprint,
        'category': category,
        'suggestions': suggestions
    })