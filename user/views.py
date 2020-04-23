from django.views.generic import TemplateView,CreateView,DetailView,UpdateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy


from .models import ModelData,InfoModel
from .forms import FormLoker,FormInfo

# --------- untuk pelamar pekerjaan

class DataLoker(ListView):
    model = InfoModel
    context_object_name = 'info'
    template_name = 'admin/data_loker.html'

class DetailLoker(DetailView): # info loker
    model = InfoModel
    template_name= 'admin/detailloker.html'
    context_object_name = 'detail_loker'

class UpdateInfo(UpdateView):
    model = InfoModel
    form_class = FormInfo
    template_name = 'admin/update_info_loker.html'

class DataUser(ListView):
    model = ModelData
    context_object_name ='datauser'
    template_name = 'admin/data_user.html'

class DetailUser(DetailView):
    model = ModelData
    template_name= 'admin/detailuser.html'
    context_object_name = 'detail'

class InputLoker(CreateView):
    model = InfoModel
    form_class = FormInfo
    template_name = 'admin/input_loker.html'

class Delete(DeleteView):
    model = ModelData
    template_name ='admin/delete_user.html'
    success_url = reverse_lazy('user:login')






# --------- untuk pelamar pekerjaan
class InputFomrs(CreateView):
    model = ModelData
    form_class = FormLoker 
    template_name = 'pelamar/form_input_pelamar.html'

class KonfrimData(DetailView):
    model = ModelData
    template_name = 'pelamar/konfrim_data.html'
    context_object_name = 'konfrim'


class UpdateData(UpdateView):
    model = ModelData
    form_class = FormLoker
    template_name = 'pelamar/update_data.html'

