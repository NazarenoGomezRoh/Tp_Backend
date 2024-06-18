from django.urls import path
from libros import views

urlpatterns = [
    path('index_libros', views.index_libros, name='index_libros'),
    path('libros_rest/', views.libros_rest, name='libros_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    #path('add_campeon/', views.add_campeon_view, name='add_campeon'),
    path('new_libros/', views.NewLibrosView.as_view(), name='new_libros'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
]