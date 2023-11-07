
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls. static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('', include('app.urls')),
    #url(r'^media/(?P<path>.*)$', serve,{'document_root':   settings.MEDIA_ROOT}),
    #url (r'^static/(?P<path>.*)$', serve, {'document_root':   settings.MEDIA_ROOT}),
]
    

urlpatterns += staticfiles_urlpatterns() # new
