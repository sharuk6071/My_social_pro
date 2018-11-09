from django.conf.urls import url
from web_app import views as web_app_views

urlpatterns = [
    url(r'^$',web_app_views.home , name='web_app-home'),
    url('<int:question_id>/', web_app_views.detail, name='detail'),
    # ex: /polls/5/results/
    url('<int:question_id>/results/', web_app_views.results, name='results'),
    # ex: /polls/5/vote/
    url('<int:question_id>/vote/', web_app_views.vote, name='vote'),
    ]
