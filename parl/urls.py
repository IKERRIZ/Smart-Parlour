from django.conf.urls import url
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^hairstyle/$', views.all_hairstyle, name='hairstyles'),
    url(r'^newprofile/$', views.profile,name = 'profile'),
    url(r'^showprofile/(?P<id>\d+)',views.display_profile,name = 'showprofile'),
    url(r'^newhairstyle/$', views.add_hairstyle,name='add_hairstyle'),
    url(r'^makeup/$', views.all_makeup, name='makeup'),
    url(r'^newmakeup/$', views.add_makeup,name='add_makeup'),
    url(r'^acrylix/$', views.all_acrylix, name='acrylix'),
    url(r'^newacrylix/$', views.add_acrylix, name='add_acrylix'),
    url(r'^skintherapy/$', views.all_therapy, name='skin_therapy'),
    url(r'^newtherapy/$', views.add_therapy, name='add_therapy'),
    url(r'^search/',views.search, name='search'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
