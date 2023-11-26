from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# from .views import *
# from woman.urls import *
# import home.urls as home_urls
# import about.urls as about_urls
# import contacts.urls as contacts_urls
# import market.urls as market_urls
# import service.urls as service_urls
# import search.urls as search_urls
# import useful.urls as useful_urls
# import works.urls as works_urls

# import useful


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('ckeditor/', include('ckeditor_uploader.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('contacts/', include('contacts.urls')),
    path('market/', include('market.urls')),
    path('service/', include('service.urls')),
    path('search/', include('search.urls')),
    path('useful/', include('useful.urls')),
    path('works/', include('works.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
# handler404 = pageNotFound  