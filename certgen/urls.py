from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from certgen.core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
