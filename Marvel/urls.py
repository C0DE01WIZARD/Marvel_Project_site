"""Marvel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # импортируем из django.counf из settings
from django.conf.urls.static import static
from Marvels_Studio.views import MovieAPI
import debug_toolbar
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Marvels_Studio.urls')), # подключаем URL нашего приложения
    path('hello/', views.hello, name='hello'),
    path('error/', views.error, name='error'),
    path('api/v1/MovieAPI/', MovieAPI.as_view()),
    path('__debug__/', include(debug_toolbar.urls))
]

# Джанго будет раздавть медия при включенном DEBUG
handler404 = "Marvel.views.page_not_found_view"

if settings.DEBUG: # если наш DEBUG включен, то
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # ДЖАНГО будет раздавть наши
    # файлы при включенном Debug режиме для работы со статическими данными


# таким образом Django будет раздавать файлы при включенном Debug режиме