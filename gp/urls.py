from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.index),
    
    #SIRVE
    #url(r'^$', 'django.contrib.auth.views.login'),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    
    url(r'^$', views.index),
    #url(r'^login/$',  views.login_view),
    url(r'^login/$',  views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^register/$', views.register_view),
    
    url(r'^edit/profile/',views.edit_profile),
    url(r'^home/', views.home),
    url(r'^games/', views.games),
    url(r'^myprofile/',views.profile),
    url(r'^tournaments/upcoming/', views.upcoming),
    url(r'^game/(?P<pk>[0-9]+)/$', views.detailed_game),
]
