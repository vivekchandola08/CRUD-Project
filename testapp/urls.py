from django.conf.urls import url
from testapp import views
urlpatterns=[
   url('employee/',views.Employee_data),
   url('about/',views.about),
   url('contact/',views.showcontact),
]
