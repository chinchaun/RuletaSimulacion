from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.http import Http404
from ruleta.models import Tirada
from django.views import generic

# Create your views here.


def grafico(request, tirada_id):
    tirada1 = get_object_or_404(Tirada, pk=13)
    tirada2 = get_object_or_404(Tirada, pk=14)
    tirada3 = get_object_or_404(Tirada, pk=15)
    data = []
    data.append(['x', 'Tirada 1', 'Tirada 2', 'Tirada 3'])
    for i in range(1, 5000):
        data.append([i,
        tirada1.numeros[i][2],
        tirada2.numeros[i][2],
        tirada3.numeros[i][2]])
    return render(request, 'ruleta/grafico.html', {'data': data})


def dispersion(request):
    return False