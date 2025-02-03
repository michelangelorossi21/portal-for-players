from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from players.models import Player, Concert, Review
from players.forms import PlayerForm, ConcertForm, ReviewForm
from django.urls import reverse

from .players import *
from .concerts import *
from .reviews import *
from .general import *
from .instruments import *