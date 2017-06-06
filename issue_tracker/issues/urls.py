from django.conf.urls import url, include
from issues import views
urlpatterns = [
    url(r'^clash/', views.home, name='home'),
]
