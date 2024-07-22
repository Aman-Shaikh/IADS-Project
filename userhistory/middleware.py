from datetime import datetime, timedelta
from django.utils import timezone


class UserHistoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current visit time
        current_visit_time = timezone.now()

        # Get visit history from the session
        visit_history = request.session.get('visit_history', [])

        # Initialize visit count and daily visits if not present
        if 'total_visit_count' not in request.session:
            request.session['total_visit_count'] = 0
        if 'daily_visits' not in request.session:
            request.session['daily_visits'] = {}

        # Check if the last visit was more than a day ago and update daily visits
        last_visit_time = request.session.get('last_visit_time')
        if last_visit_time:
            last_visit_time = datetime.fromisoformat(last_visit_time)
            if current_visit_time.date() != last_visit_time.date():
                visit_date_str = last_visit_time.date().isoformat()
                if visit_date_str in request.session['daily_visits']:
                    request.session['daily_visits'][visit_date_str] += 1
                else:
                    request.session['daily_visits'][visit_date_str] = 1

        # Update the visit history
        visit_history.append(current_visit_time.isoformat())
        request.session['visit_history'] = visit_history

        # Update the total visit count
        request.session['total_visit_count'] += 1

        # Update the last visit time
        request.session['last_visit_time'] = current_visit_time.isoformat()

        # Get the response
        response = self.get_response(request)

        return response