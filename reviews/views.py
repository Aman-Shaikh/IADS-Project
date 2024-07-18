from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


# Display all reviews and allow user to create a review
def get_reviews(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Assign the current user to the review
            review.save()
            return redirect('get_reviews')  # Redirect to the same page to see the new review
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'reviews/reviews.html', {'form': form, 'reviews': reviews})
