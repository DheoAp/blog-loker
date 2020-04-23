from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class ModelData(models.Model): # untuk pelamar
    nama_lengkap     = models.CharField(max_length=50)

    Pilihan = (
        ('Laki-laki','Laki-laki'),
        ('Perempuan','Perempuan')
    )   
    jenis_kelamin    = models.CharField(
                                    max_length= 30,
                                    choices=Pilihan,
                                    default='Laki-laki'
                                )    
    tanggal_lahir    = models.CharField(max_length=50)
    tempat_lahir     = models.CharField(max_length=100)
    alamat           = models.TextField()
    no_tlp           = models.CharField(max_length=18)
    email            = models.EmailField()

    Pilih_Posisi =(
        ('Web Developer','Web Developer'),
        ('IT Support','IT Support'),
        ('Back-end','Back-end')
    )
    posisi           = models.CharField(
                                    max_length=50,
                                    choices=Pilih_Posisi,
                                    default=('Web Developer')
                                )
    date_input       = models.DateTimeField(auto_now_add=True)
    slug             = models.SlugField(blank=True, editable=False)


    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('user:konfrim',kwargs=url_slug)


    def save(self):
        self.slug = slugify (self.nama_lengkap)
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_lengkap)


class InfoModel(models.Model): # untuk info loker (admin)
    posisi      = models.CharField(max_length=50)
    syarat1     = models.CharField(max_length=100)
    syarat2     = models.CharField(max_length=100)
    syarat3     = models.CharField(max_length=100)
    syarat4     = models.CharField(max_length=100)
    deskripsi   = models.TextField()
    benefit     = models.TextField()
    kontak      = models.TextField()
    publish     = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField(blank=True, editable=False)


    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('user:data_loker',kwargs=url_slug)

    def save(self):
        self.slug = slugify(self.posisi)
        super().save()
    
    def __str__(self):
        return "{}. {}".format(self.id, self.posisi)
