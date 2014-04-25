# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from ruleta import views

urlpatterns = patterns('',
    url(r'^(?P<tirada_id>\d+)/grafico/$', views.grafico, name='grafico'),
)
