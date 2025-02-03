from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from players.models import Player, Concert, Review
from players.forms import PlayerForm, ConcertForm, ReviewForm
from django.urls import reverse

# CONCERTS:

def concerts_summary(request):
    concerts_list = Concert.objects.order_by('-place')
    context = {'concerts_list': concerts_list}
    return render(request, 'players/concerts/concerts_summary.html', context)


CONCERT_KEYS = ['Place', 'Date and Time']

def concert_detail(request, concert_id):
    selected_concert = Concert.objects.get(pk=concert_id)
    players = list(selected_concert.players.all())
    concert_values = list(selected_concert.__dict__.values())[2:]  # ignore __stat and id
    details = []
    for i in range(len(CONCERT_KEYS)):
        field = (CONCERT_KEYS[i], concert_values[i])
        details.append(field)

    context = {'details': details, 'players': players, 'concert': selected_concert}
    return render(request, 'players/concerts/concert_detail.html', context)


def concert_insert(request):
    if request.method == 'GET':  # new player, return empty form
        form = ConcertForm()
        return render(request, 'players/general/insert.html', {'form': form})
    else:
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('players:concerts_summary'))


def concert_modify(request, concert_id):
    if request.method == 'GET':  # want to modify existing concert, get the form filled with current values
        conc = Concert.objects.get(pk=concert_id)
        form = ConcertForm(instance=conc)
        return render(request, 'players/general/insert.html', {'form': form})
    else:
        conc = Concert.objects.get(pk=concert_id)  # POST: push modified values into DB
        form = ConcertForm(request.POST, instance=conc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('players:concert_detail', args=(concert_id,)))


def concert_delete(request, concert_id):
    concert = Concert.objects.get(pk=concert_id)
    concert.delete()
    return HttpResponseRedirect(reverse('players:concerts_summary'))

