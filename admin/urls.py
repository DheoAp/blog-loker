from django.contrib import admin
from django.urls import path, include

from .views import(
            About,
            Index,
            DataUser,
            InfoLoker
        )

urlpatterns = [
    path('info/',InfoLoker.as_view(), name='info'),
    path('user/',include(('user.urls','app_name'), namespace='user')),
    path('about/',About.as_view(), name='about'),
    path('',Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
