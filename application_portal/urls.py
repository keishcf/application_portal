from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path('', include('apply.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
