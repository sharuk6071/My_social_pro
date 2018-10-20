from django.conf.urls import url
from web_users import views as web_users_views

urlpatterns = [
    url(r'^register/',web_users_views.register,name='register'),
    url(r'^profile/',web_users_views.profile,name='profile'),
]
