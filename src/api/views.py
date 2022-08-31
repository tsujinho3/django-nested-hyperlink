from django.shortcuts import render
from rest_framework import views


class RootAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        pass
