from django.shortcuts import render
from .models import Portfolio
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
class PortfolioDetailView(DetailView):
    model = Portfolio

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        return context

class PortflioListView(ListView):
    model = Portfolio
    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        return context


