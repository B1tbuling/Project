from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import *


class ObjectsListMixin:
    model = None
    template = None

    def get(self, request):
        objs = self.model.objects.all()
        return render(request, self.template , context={self.model.__name__.lower() + 's': objs})


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={ 'form': form })

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})