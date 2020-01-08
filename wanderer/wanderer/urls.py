from django.contrib import admin
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
]
