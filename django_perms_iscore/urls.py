# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^IsCorePerm/~create/$",
        view=views.IsCorePermCreateView.as_view(),
        name='IsCorePerm_create',
    ),
    url(
        regex="^IsCorePerm/(?P<pk>\d+)/~delete/$",
        view=views.IsCorePermDeleteView.as_view(),
        name='IsCorePerm_delete',
    ),
    url(
        regex="^IsCorePerm/(?P<pk>\d+)/$",
        view=views.IsCorePermDetailView.as_view(),
        name='IsCorePerm_detail',
    ),
    url(
        regex="^IsCorePerm/(?P<pk>\d+)/~update/$",
        view=views.IsCorePermUpdateView.as_view(),
        name='IsCorePerm_update',
    ),
    url(
        regex="^IsCorePerm/$",
        view=views.IsCorePermListView.as_view(),
        name='IsCorePerm_list',
    ),
	]
