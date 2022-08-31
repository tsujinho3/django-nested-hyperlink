from rest_framework import serializers


class NestedHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    """
    NestedHyperlinkedIdentityField

    This field handle nested path converters
        ex) /book/<publiser_slug>/<book_slug>/
    """

    def get_url(self, obj, view_name, request, format):
        """
        Given an object, return the URL that hyperlinks to the object.
        May raise a `NoReverseMatch` if the `view_name` and `lookup_field`
        attributes are not configured to correctly match the URL conf.
        """
        # Unsaved objects will not yet have a valid URL.
        if hasattr(obj, "pk") and obj.pk in (None, ""):
            return None

        # split a nested field by "."
        #   ex) "book.publisher"
        lookup_fields = self.lookup_field.split(".")

        # corresponding a url pattern
        #   ex) /book/<publisher_id>/
        lookup_url_kwarg = self.lookup_url_kwarg

        # analyse a nested field and get the related field
        for lookup_field in lookup_fields:
            obj = getattr(obj, lookup_field)

        lookup_value = obj
        lookup_kwargs = {lookup_url_kwarg: lookup_value}

        # get all keywords in request to solve a nested url pattern
        #   ex) /book/<publisher_id>/<book_id>/
        request_kwargs = request.resolver_match.kwargs

        kwargs = dict(lookup_kwargs, **request_kwargs)

        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)


# class ComplexHyperlinkedSerializer(serializers.Serializer):
#     pass
