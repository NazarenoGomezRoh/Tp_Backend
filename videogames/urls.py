from django.urls import path
from videogames import views

urlpatterns = [
    path('index_videogames', views.index_videogames, name='index_videogames'),
    path('videogames_rest/', views.videogames_rest, name='videogames_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    #path('add_campeon/', views.add_campeon_view, name='add_campeon'),
    path('new_videogames/', views.NewVideogamesView.as_view(), name='new_videogames'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
]