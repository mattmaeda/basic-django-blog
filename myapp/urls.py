from django.conf.urls import url, include
from rest_framework import routers
from myapp.views import list_view, detail_view, create_view, PostViewSet

router = routers.DefaultRouter()
router.register(r'/posts', PostViewSet)

urlpatterns = [
    url(r'^posts/new/$', create_view, name="blog_new"),
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^post-api', include(router.urls)),
    url(r'^$', list_view, name="blog_index"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
