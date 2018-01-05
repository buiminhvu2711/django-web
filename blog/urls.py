from django.conf.urls import url
from . import views

urlpatterns =  [
    #/blog/
    url(r'^$',views.list, name="list"),
    #/blog/2
    url(r'^(?P<post_id>\d+)$',views.post, name="viewDetail"),
    #category
]

