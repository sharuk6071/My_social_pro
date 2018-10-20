from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from web_app import views as web_app_views

urlpatterns = [
    url(r'^$',web_app_views.home , name='web_app-home'),
    url(r'^api/',web_app_views.employeeList.as_view()),
    ]
