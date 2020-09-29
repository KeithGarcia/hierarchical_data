from django.shortcuts import render

from genre.models import Genre

def index_view(request):
    return render(request, 'index.html', {'all_files': Genre.objects.all()})