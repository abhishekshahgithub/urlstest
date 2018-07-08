from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create), # Alternative way ,from posts import views "views.post_home"
    #    url(r'^posts/$', "<appname>.views.<function_name>""),
    url(r'^detail/$', post_detail), 
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),

]