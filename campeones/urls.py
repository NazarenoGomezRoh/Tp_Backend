from django.urls import path
from campeones import views

urlpatterns = [
    path('index_campeones', views.index_campeones, name='index_campeones'),
    path('campeones_rest/', views.campeones_rest, name='campeones_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    #path('add_campeon/', views.add_campeon_view, name='add_campeon'),
    path('new_campeones/', views.NewCampeonesView.as_view(), name='new_campeones'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
]