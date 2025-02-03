from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from players.models import Player, Concert, Review
from players.forms import PlayerForm, ConcertForm, ReviewForm
from django.urls import reverse


# Main Page:

def home(request):
    return render(request, 'players/general/home.html')


def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        searched_split = searched.split(' ')  # split string if multiple words

        search_results = []  # check if a word is contained in a field (insensitive)
        for item in searched_split:  # I'll get a list of Query-sets
            search_results.append(Player.objects.filter(name__icontains=item))
            search_results.append(Player.objects.filter(surname__icontains=item))
            search_results.append(Player.objects.filter(instrument__icontains=item))

        search_readable = []  # from the Query set list extract list of players
        for query in search_results:  # from each query-set extract players and put them in a readable list
            for player in query:
                search_readable.append(player)

        search_readable = sorted(set(search_readable), key=lambda x: x.surname)  # sort players by surname

        concerts_results = Concert.objects.filter(place__icontains=searched).order_by('-concert_time')  # sort concerts by time
        for concert in concerts_results:
            concert.concert_time = concert.concert_time.strftime("%d-%m-%Y, %H:%m")


        context = {'searched': searched, 'players': search_readable, 'concerts': concerts_results}
        return render(request, 'players/general/search.html', context)







