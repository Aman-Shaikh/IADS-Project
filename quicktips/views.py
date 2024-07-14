from django.shortcuts import render
from .forms import QuickTipForm
from .models import QuickTip, Tips

def quicktips_view(request):
    form = QuickTipForm(request.GET)
    tips = None
    waste_choice_display = None

    if form.is_valid():
        waste_choice_key = form.cleaned_data['waste_choices']
        tips = Tips.objects.filter(waste_type__waste_choices=waste_choice_key)
        waste_choice_display = dict(QuickTip.Waste_Options).get(waste_choice_key)

    return render(request, 'quicktips/get_recycletips.html', {
        'tips': tips,
        'form': form,
        'waste_choice_display': waste_choice_display
    })
