from django.shortcuts import render
from datetime import datetime

def user_history(request):
    visit_count = request.session.get('total_visit_count', 0)
    last_visit_time = request.session.get('last_visit_time', 'N/A')
    daily_visits = request.session.get('daily_visits', {})
    visit_history = request.session.get('visit_history', [])

    # Convert visit history timestamps to datetime objects
    visit_history = [datetime.fromisoformat(timestamp) for timestamp in visit_history]

    return render(request, 'userhistory/userhistory.html', {
        'visit_count': visit_count,
        'last_visit_time': last_visit_time,
        'daily_visits': daily_visits,
        'visit_history': visit_history,
    })