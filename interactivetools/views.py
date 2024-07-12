from django.shortcuts import render

# Dummy data for demonstration purposes
RECYCLABLE_ITEMS = [
    'Plastic Bottles', 'Glass Jars', 'Paper', 'Cardboard', 'Aluminum Cans', 'Electronics'
]


def searchable_database(request):
    query = request.GET.get('q')
    if query:
        results = [item for item in RECYCLABLE_ITEMS if query.lower() in item.lower()]
    else:
        results = []
    return render(request, 'interactivetools/searchable_database.html', {'query': query, 'results': results})


def carbon_footprint_calculator(request):
    carbon_footprint = None
    if request.method == 'POST':
        miles_per_week = int(request.POST.get('miles'))
        carbon_footprint = miles_per_week * 52 * 0.404 # Approximate kg CO2 per mile driven
    return render(request, 'interactivetools/carbon_footprint_calculator.html', {'carbon_footprint': carbon_footprint})