from django.urls import path

urlpatterns = [
    path("", RootAPIView.as_view(), name="root"),
    # path("posts/", PostRootAPIView.as_view(), name="posts-root"),
    # path("posts/<language_code>/", PostListAPIView.as_view(), name="posts-list"),
    # path(
    #     "posts/<language_code>/<slug>/",
    #     PostAPIView.as_view(),
    #     name="posts-detail",
    # ),
]
