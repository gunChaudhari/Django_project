from django.urls import path
from. import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
