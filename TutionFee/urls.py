from django.conf.urls import url
from . import views

app_name = 'TutionFee'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^home/(?P<subject>\w+)/$', views.subject_wise, name='subject_wise'),
    url(r'^home/(?P<subject>\w+)/(?P<division>\w+)/$', views.division_wise, name='division_wise'),
]
