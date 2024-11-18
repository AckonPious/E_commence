from django.shortcuts import render
from django.views.generic import view


class HomePageView(view):
    template_name = 'core/home.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)