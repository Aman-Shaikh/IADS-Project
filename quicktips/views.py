from django.shortcuts import render, redirect
from .forms import WasteTypeForm, TipForm
from .models import WasteType, Tip

def quicktips_view(request):
    form = WasteTypeForm(request.GET)
    tips = None
    waste_choice_display = None

    if form.is_valid():
        waste_choice_key = form.cleaned_data['waste_choices']
        tips = Tip.objects.filter(waste_type__waste_choices=waste_choice_key)
        waste_choice_display = dict(WasteType.Waste_Options).get(waste_choice_key)

    return render(request, 'quicktips/get_recycletips.html', {
        'tips': tips,
        'form': form,
        'waste_choice_display': waste_choice_display
    })

def add_tip_view(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'quicktips/thank_you.html')
    else:
        form = TipForm()

    return render(request, 'quicktips/add_tip.html', {'form': form})
