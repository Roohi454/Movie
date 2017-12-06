from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Movie
from . serializers import MovieSerializer

def index(request):
    queryset = Movie.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, 'movieapp/index.html', context)

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        Q(name__icontains = query)
        ).distinct()

class movieList(APIView):

    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many= True)
        return Response(serializer.data)
