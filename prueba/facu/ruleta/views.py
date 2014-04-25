from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.http import Http404
from ruleta.models import Tirada
from django.views import generic
import math
# Create your views here.


def graficoMedia(request, tirada_id):
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
    return render(request, 'ruleta/graficoMedia.html', {'data': data})


def graficoDispersion(request, tirada_id):
    tirada = get_object_or_404(Tirada, pk=tirada_id)
    media = tirada.numeros[4999][2]
    data = []
    for i in range(0, 4999):
        dispersion = (tirada.numeros[i][1] - media) ** 2
        dispersion = math.sqrt(dispersion)
        data.append([i, dispersion])
    return render(request, 'ruleta/graficoDispersion.html', {'data': data})


def graficoFRelativa(request, tirada_id):
    tirada = get_object_or_404(Tirada, pk=tirada_id)
    data = []
    for i in range(0, 37):
        data.append([i, 0])
    for i in range(0, 4999):
        numero = tirada.numeros[i][1]
        for j in range(0, 37):
            if(numero == data[j][0]):
                data[j][1] += 1
                break
    return render(request, 'ruleta/graficoFRelativa.html', {'data': data})

