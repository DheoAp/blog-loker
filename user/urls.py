from django.urls import path, re_path

from .views import (
            InputFomrs,
            KonfrimData,
            UpdateData,
            DataUser,
            DetailUser,
            Delete,
            DataLoker,
            UpdateInfo,
            DetailLoker,
            InputLoker
        )

urlpatterns = [
    # crud info loker
    path('dataloker/',DataLoker.as_view(), name='data_loker'),            
    path('input/',InputLoker.as_view(), name='tambah_info'),    
    re_path('updateinfo/(?P<pk>\d+)', UpdateInfo.as_view(), name='Update'),
    re_path('detail_loker/(?P<pk>\d+)',DetailLoker.as_view(), name='detail_loker'),

    # untuk data user(pelamar)
    re_path('detail/(?P<pk>\d+)',DetailUser.as_view(), name='detail'),
    re_path('delete/(?P<pk>\d+)',Delete.as_view(), name='delete'),
    path('login/',DataUser.as_view(), name='login'), # masuk login dulu baru ke table data user

    # untuk pelamar
    re_path('update/(?P<pk>\d+)/',UpdateData.as_view(),name='update'),# ubah data pelamar yang sudah di input karyawan
    re_path('konfrim/(?P<slug>[\w-]+)/',KonfrimData.as_view(), name='konfrim'), # konfrim data pelamar
    path('',InputFomrs.as_view(), name='inputforms') # untuk input form karyawan
]