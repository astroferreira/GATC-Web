from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pgc_id>[0-9]+)/$', views.detail, name='detail'),
<<<<<<< HEAD
	url(r'^sampleStats/$', views.sampleStats, name='sampleStats'),
=======
>>>>>>> 1f39f57a11adb7b38e50bc2e4a0c0feb1ff1eb6f
]
