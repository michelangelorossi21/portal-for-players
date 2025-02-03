from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from players.models import Player, Concert, Review
from players.forms import PlayerForm, ConcertForm, ReviewForm
from django.urls import reverse


# REVIEWS VIEWS:

def compute_average(reviews_list):
    if reviews_list:
        # avg rounded to 2 floating digits
        average = round(sum(review.rating for review in reviews_list)/len(reviews_list), 2)
    else:
        average = False
    return average


def reviews_summary(request, player_id):
    reviews_list = Review.objects.filter(player=player_id).order_by('-pub_date', 'title')
    reviews_count = len(reviews_list)
    average = compute_average(reviews_list)
    context = {'reviews_list': reviews_list, 'count': reviews_count, 'average': average, 'player_id': player_id}
    return render(request, 'players/general/reviews_summary.html', context)


def review_insert(request, player_id):
    if request.method == 'GET':  # new player, return empty form
        form = ReviewForm()
        return render(request, 'players/general/insert.html', {'form': form})
    else:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # player = form.cleaned_data.get("player")
            return HttpResponseRedirect(reverse('players:reviews', args=(player_id,)))


def review_modify(request, player_id, review_id):
    if request.method == 'GET':  # want to modify existing review, get the form filled with current values
        rev = Review.objects.get(pk=review_id)
        form = ReviewForm(instance=rev)
        return render(request, 'players/general/insert.html', {'form': form})
    else:
        rev = Review.objects.get(pk=review_id)  # POST: push modified values into DB
        form = ReviewForm(request.POST, instance=rev)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('players:reviews', args=(player_id,)))


def review_delete(request, player_id, review_id):
    selected_review = Review.objects.get(pk=review_id)
    selected_review.delete()
    return HttpResponseRedirect(reverse('players:reviews', args=(player_id,)))
