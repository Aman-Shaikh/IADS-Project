from django.shortcuts import render
from .forms import WasteTypeForm
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
