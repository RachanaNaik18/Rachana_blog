"""
URL configuration for project_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name='home'),
    path('thoughts/', views.Creation, name='thoughts'),
    path('my_thoughts/', views.my_page, name="my_thoughts"),
    path('update/<int:id>', views.update, name='update'),
    path("<int:id>", views.delete, name='delete'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='logout'),
    path('posts/<int:id>', views.Comment_detail, name='posts')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
