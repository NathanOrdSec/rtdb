from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register)
]
