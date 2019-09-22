from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('personal/', Personal, name='personal'),
    path('change/', Change.as_view(), name='change_profile'),
]
from django.conf.urls.static import static
from django.conf import settings
if  settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)