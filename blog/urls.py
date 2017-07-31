from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^posts/', views.post_list, name='post_list'),
]
