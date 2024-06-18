from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from campeones.forms import CampeonForm, UserForm
from campeones.models import Campeon
from campeones.serializers import CampeonSerializer
from django.middleware.csrf import get_token
# Create your views here.


def get_all_campeones():
    campeones = Campeon.objects.all().order_by('nombre')
    campeones_serializers = CampeonSerializer(campeones, many=True)
    return campeones_serializers.data


def index_campeones(request):
    campeones = get_all_campeones()
    return render(request, 'index_campeones.html', {'campeones': campeones})


def campeones_rest(request):
    campeones = get_all_campeones()
    return JsonResponse(campeones, safe=False)


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

class NewCampeonesView(CreateView):
    form_class = CampeonForm
    template_name = 'form_campeones.html'
    success_url = '/index_campeones'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_campeones.html'
    success_url = '/'