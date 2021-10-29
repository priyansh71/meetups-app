from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='all-meetups'), # / so that meetups/something is not 404
    path('<slug:meetup_slug>/success', views.success, name='confirmation'),
    path('<slug:meetup_slug>', views.meetup_details , name='meetup-detail') # <> to load the page with a dynamic path but same content

]
