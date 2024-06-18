from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from videogames.forms import VideogamesForm, UserForm
from videogames.models import Videogames
from videogames.serializers import VideogamesSerializer
from django.middleware.csrf import get_token
# Create your views here.


def get_all_videogames():
    videogames = Videogames.objects.all().order_by('nombre')
    videogames_serializers = VideogamesSerializer(videogames, many=True)
    return videogames_serializers.data


def index_videogames(request):
    videogames = get_all_videogames()
    return render(request, 'index_videogames.html', {'videogames': videogames})


def videogames_rest(request):
    videogames = get_all_videogames()
    return JsonResponse(videogames, safe=False)


def users_rest(request):
    return JsonResponse("Ok", safe=False)


# def add_funko_view(request):
    
#     if request.method == 'POST':
#         funko_form = FunkoForm(request.POST)
#         if funko_form.is_valid():
#             funko = funko_form.save()
#             return HttpResponseRedirect('/')
#     if request.method == 'GET':
#         funko_form = FunkoForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {funko_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)

class NewVideogamesView(CreateView):
    form_class = VideogamesForm
    template_name = 'form_videogames.html'
    success_url = '/index_videogames'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_videogames.html'
    success_url = '/'