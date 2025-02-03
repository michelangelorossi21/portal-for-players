from django.urls import path
from . import views
app_name = 'players'

urlpatterns = [
    # Main page, summaries and search:
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('players/', views.players_summary, name='players_summary'),
    path('concerts/', views.concerts_summary, name='concerts_summary'),

    # Instruments:
    path('instruments/', views.instruments, name='instruments'),
    path('instruments/<str:instr>', views.instruments_search_results, name='instruments_search_results'),


    # Players:
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),
    path('players/player_insert/', views.player_insert, name='player_insert'),
    path('players/<int:player_id>/player_modify/', views.player_modify, name='player_modify'),
    path('players/<int:player_id>/player_delete/', views.player_delete, name='player_delete'),

    # Concerts:
    path('concerts/<int:concert_id>/', views.concert_detail, name='concert_detail'),
    path('concerts/concert_insert/', views.concert_insert, name='concert_insert'),
    path('concerts/<int:concert_id>/concert_modify/', views.concert_modify, name='concert_modify'),
    path('concerts/<int:concert_id>/concert_delete/', views.concert_delete, name='concert_delete'),

    # Reviews:
    path('players/<int:player_id>/reviews/', views.reviews_summary, name='reviews'),
    path('players/<int:player_id>/review_insert/', views.review_insert, name='review_insert'),
    path('players/<int:player_id>/<int:review_id>/review_modify/', views.review_modify, name='review_modify'),
    path('players/<int:player_id>/<int:review_id>/review_delete/', views.review_delete, name='review_delete'),

]
