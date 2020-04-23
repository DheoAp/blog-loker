from django.forms import ModelForm
from django import forms

from .models import ModelData,InfoModel

class FormLoker(forms.ModelForm):
    class Meta:
        model = ModelData
        fields = [
            'nama_lengkap',
            'jenis_kelamin',
            'tanggal_lahir',
            'tempat_lahir',
            'alamat',
            'no_tlp',
            'email',
            'posisi'
        ]

        widgets = {
            'nama_lengkap': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'planceholder':'isi nama lengkap'
                }
            ),

            'jenis_kelamin':forms.RadioSelect(
                attrs={
                    'class':'custom-control-input custom-control-label'
                }
            ),

            'tanggal_lahir':forms.DateInput(
                attrs={'id':'datetimepicker12'}
            ),

            'tempat_lahir': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'planceholder':'isi tempat lahir'
                }
            ),

            'alamat': forms.Textarea(
                attrs={
                    'class':'form-control col-sm-4',
                }
            ),

            'posisi':forms.RadioSelect(
                attrs={
                    'class':'custom-control-input custom-control-label'
                }
            ),        
 }

class FormInfo(forms.ModelForm):
    class Meta:
        model = InfoModel
        fields = [
            'posisi',
            'syarat1',
            'syarat2',
            'syarat3',
            'syarat4',
            'deskripsi',
            'benefit',
            'kontak',
        ]

        widgets = {
            'posisi': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'planceholder':'posisi'
                }
            ),

            'syarat1': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'planceholder':'Usia'
                }
            ),

            'syarat2': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'planceholder':'Pedidikan'
                }
            ),

            'syarat3': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'planceholder':'Kualifikasi Khusus'
                }
            ),

            'syarat4': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'planceholder':'Kualifikasi Khusus'
                }
            ),

            'deskripsi': forms.Textarea(
                attrs={
                    'class':'form-control col-sm-4',
                }
            ),

            'benefit': forms.Textarea(
                attrs={
                    'class':'form-control col-sm-4',
                }
            ),
            
            'kontak': forms.Textarea(
                attrs={
                    'class':'form-control col-sm-4',
                }
            ),        
        }