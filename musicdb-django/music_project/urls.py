"""
URL configuration for music_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return HttpResponse(
        '''
          <div style="min-height:calc(100vh - 1rem); background-color: #7a888c; display:flex; flex-direction:column; gap: 0.5rem; justify-content:center; align-items:center">
            <h1 style="text-align: center; color: #00dcf5">Welcome To Music Database</h1>
            <p style="color: #fff; font-style:italic">Use <a href='http://127.0.0.1:8000/music/'>/music URL</a> to access the restricted database management interface.</p>
          </div>
        '''
    )


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('music/', include('music_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
