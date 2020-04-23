from django.views.generic import TemplateView,ListView

from user.models import InfoModel


class DataUser(TemplateView):
    template_name = 'data_admin/data_user.html'

class Index(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class InfoLoker(ListView):
    model = InfoModel
    template_name = 'info_loker.html'
    context_object_name = 'info'
   

        
    