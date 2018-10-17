from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from web_app import views

urlpatterns = [
    url(r'^$',views.index , name='index')
]
