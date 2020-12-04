from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('user/', include('person.urls', namespace="person")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # login/forgot password etc.
 ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
