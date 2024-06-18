from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from libros.forms import LibrosForm, UserForm
from libros.models import Libros
from libros.serializers import LibrosSerializer
from django.middleware.csrf import get_token
# Create your views here.


def get_all_libros():
    libros = Libros.objects.all().order_by('nombre')
    libros_serializers = LibrosSerializer(libros, many=True)
    return libros_serializers.data


def index_libros(request):
    libros = get_all_libros()
    return render(request, 'index_libros.html', {'libros': libros})


def libros_rest(request):
    libros = get_all_libros()
    return JsonResponse(libros, safe=False)


def users_rest(request):
    return JsonResponse("Ok", safe=False)


# def add_campeon_view(request):
    
#     if request.method == 'POST':
#         campeon_form = CampeonForm(request.POST)
#         if campeon_form.is_valid():
#             campeon = campeon_form.save()
#             return HttpResponseRedirect('/')
#     if request.method == 'GET':
#         campeon_form = CampeonForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {campeon_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)

class NewLibrosView(CreateView):
    form_class = LibrosForm
    template_name = 'form_libros.html'
    success_url = '/index_libros'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_libros.html'
    success_url = '/'