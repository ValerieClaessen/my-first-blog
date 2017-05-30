from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.stadt_suchen, name='stadt_suchen'),
    url(r'^$', views.stadt_suchen, name='stadt_speichern')
]
