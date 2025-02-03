from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from players.models import Player, Concert, Review
from players.forms import PlayerForm, ConcertForm, ReviewForm
from django.urls import reverse


# INSTRUMENTS:
def instruments(request):
    players_list = Player.objects.all()
    instruments = []
    for player in players_list:
        instruments.append(player.instrument.capitalize())

    instruments = sorted(set(instruments))

    return render(request, 'players/instruments/instruments.html', {'instruments': instruments})


def instruments_search_results(request, instr):
    players = Player.objects.filter(instrument=instr.lower()).order_by('surname')
    return render(request, 'players/instruments/instruments_search_results.html', {'players': players})
