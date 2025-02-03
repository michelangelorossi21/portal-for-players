from django.shortcuts import render
from django.http import HttpResponseRedirect
from players.models import Player
from players.forms import PlayerForm
from django.urls import reverse


# PLAYERS:

def players_summary(request):
    players_list = Player.objects.order_by('surname')
    context = {'players_list': players_list}
    return render(request, 'players/players/players_summary.html', context)


PLAYER_KEYS = ['Name', 'Surname', 'Instrument', 'Date of birth']

def player_detail(request, player_id):  # print on screen infos about a player
    selected_player = Player.objects.get(pk=player_id)
    age = selected_player.get_age()  # Compute age of a player

    player_values = list(selected_player.__dict__.values())[2:]  # Ignore __stat__ and id (don't need to be shown in the web page)

    details = []
    for i in range(len(PLAYER_KEYS)):  # Get a tuple to pair every field to every value
        field = (PLAYER_KEYS[i], player_values[i])
        details.append(field)

    concerts = list(selected_player.concert_set.all())  # Extract concerts in which a player was involved

    context = {'details': details, 'player': selected_player, 'age': age, 'concerts': concerts}
    return render(request, 'players/players/player_detail.html', context)


def player_insert(request):
    if request.method == 'GET':  # new player, return empty form
        form = PlayerForm()
        return render(request, 'players/general/insert.html', {'form': form})
    else:
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('players:players_summary'))


def player_modify(request, player_id):
    if request.method == 'GET':  # want to modify existing player, get the form filled with current values
        pl = Player.objects.get(pk=player_id)
        form = PlayerForm(instance=pl)
        return render(request, 'players/general/insert.html', {'form': form})
    else:
        pl = Player.objects.get(pk=player_id)  # POST: push modified values into DB
        form = PlayerForm(request.POST, request.FILES, instance=pl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('players:player_detail', args=(player_id,)))


def player_delete(request, player_id):
    player = Player.objects.get(pk=player_id)
    player.delete()
    return HttpResponseRedirect(reverse('players:players_summary'))
