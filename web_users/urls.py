from django.conf.urls import url
from web_users import views as web_users_views

urlpatterns = [
    url(r'',web_users_views.register,name='register'),
]
