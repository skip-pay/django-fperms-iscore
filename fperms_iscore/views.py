# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	IsCorePerm,
)


class IsCorePermCreateView(CreateView):

    model = IsCorePerm


class IsCorePermDeleteView(DeleteView):

    model = IsCorePerm


class IsCorePermDetailView(DetailView):

    model = IsCorePerm


class IsCorePermUpdateView(UpdateView):

    model = IsCorePerm


class IsCorePermListView(ListView):

    model = IsCorePerm

