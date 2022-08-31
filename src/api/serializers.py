from nested_hyperlink.models import NestedHyperlinkedIdentityField
from rest_framework import serializers


class PublisherSerializer(serializers.ModelSerializer):
    url = NestedHyperlinkedIdentityField(
        view_name="posts-detail",
        read_only=True,
        lookup_field="post.slug",
        lookup_url_kwarg="slug",
    )
