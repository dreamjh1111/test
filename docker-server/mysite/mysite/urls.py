from django.contrib import admin
from django.urls import include, path
import portfolio.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('todos/', include('apis.urls')),
]
