from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from . models import Product
# from django.contrib import admin
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class Category(TemplateView):

    template_name = "category.html"


class About(TemplateView):

    template_name = "about.html"


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # slug = context.filter(category=context)
        print(self.kwargs)
        return context
