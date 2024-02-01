from django.urls import path
from .views import Home, Profilelist, ProfileCreate, MovieList, MovieDetail, PlayMovie
from django.conf import settings
from django.conf.urls.static import static





app_name = 'accessmovies'

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profiles/', Profilelist.as_view(), name='profile-list'),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>/', MovieDetail.as_view(), name="movie-detail"),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name="play-movie"),

    
]
# Add URL patterns for serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

