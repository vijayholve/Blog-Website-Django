from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views  as BlogsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', BlogsView.blogs, name='blogs'),
    path('blog/search/', BlogsView.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', include('dashboards.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # Add this

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)