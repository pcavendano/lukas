# Create your views here.
# pages/views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "templates/home.html"