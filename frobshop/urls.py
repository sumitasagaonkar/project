from django.apps import apps
from django.conf.urls import include, url  # < Django-2.0
# from django.urls import include, path  # > Django-2.0
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    url(r'^admin/', admin.site.urls),
    # path('admin/', admin.site.urls),  # > Django-2.0

    url(r'^', include(apps.get_app_config('oscar').urls[0])),
    # path('', include(apps.get_app_config('oscar').urls[0])),  # > Django-2.0
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)