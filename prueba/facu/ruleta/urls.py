# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from ruleta import views

urlpatterns = patterns('',
    url(r'^(?P<tirada_id>\d+)/graficoMedia/$',
         views.graficoMedia, name='graficoMedia'),
    url(r'^(?P<tirada_id>\d+)/graficoDispersion/$',
        views.graficoDispersion, name='graficoDispersion'),
    url(r'^(?P<tirada_id>\d+)/graficoFRelativa/$',
        views.graficoFRelativa, name='graficoFRelativa')
)
