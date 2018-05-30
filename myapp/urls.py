from django.conf.urls import url
from myapp.views import list_view, detail_view, create_view

urlpatterns = [
    url(r'^posts/new/$', create_view, name="blog_new"),
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
]
