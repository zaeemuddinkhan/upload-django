from django.urls import path
from . import views
urlpatterns = [
    path("",views.starting_post,name="starting-page"),
    path("posts",views.post,name="post-page"),
    path("posts/<slug:slug>",views.post_detail.as_view(),name="post-detail-page"),
    path("read-later",views.Readlater.as_view(),name="read-later")
]
