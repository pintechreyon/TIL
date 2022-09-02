from django.shortcuts import render, redirect

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        audience = request.POST.get('audience')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie()
        movie.title = title
        movie.audience = audience
        movie.release_date = release_date
        movie.genre = genre
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        movie.save()
        return redirect('movies:detail', movie.pk)

    return render(request, 'movies/new.html')

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def delete(request,movie_pk): # 단일 영화 데이터 삭제 및 index로 redirect
  movie = Movie.objects.get(pk=movie_pk)
  if request.method == 'POST':
    movie.delete()
  return redirect('movies:index')

def edit(request,movie_pk):#수정 대상 영화 조회 및 edit 렌더링
  movie = Movie.objects.get(pk=movie_pk)
  return render(request, 'movies/edit.html',{'movie':movie})

def update(request, movie_pk):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie= Movie.objects.get(pk=movie_pk)
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    return redirect('movies:detail', movie.pk)