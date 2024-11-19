from django.shortcuts import render
from django.views.generic import View


class HomePageView(View):
    template_name = 'core/home.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
