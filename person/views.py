from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import FamousSerializers






class Famous(APIView):
    def get(self,request):
        list1 = Person.objects.all().values()
        return Response({'famous': list(list1)})
    def post(self,requests):
        posts = Person.objects.create(
            name=requests.data["name"],
            cat_id=requests.data["cat_id"],
        )
        return Response({"posts": model_to_dict(posts)})




# class Famous(generics.ListAPIView):
#     queryset = Person.objects.all()
