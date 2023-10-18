from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.questions import urls as questions_url


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(questions_url))
]


if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)