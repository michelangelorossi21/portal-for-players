from django.forms import ModelForm
from .models import Player, Review, Concert


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'surname', 'instrument', 'date_of_birth', 'photo']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'player', 'text', 'rating']


class ConcertForm(ModelForm):
    class Meta:
        model = Concert
        fields = ['place', 'concert_time', 'players']
