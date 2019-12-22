from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from shopping import views
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^additem/$',views.addditem, name='addditem'),
    url(r'^$',views.Home, name='home'),
    url(r'^SignUp/$', views.SignUp, name = 'signup'),
    url(r'^Login/$', views.Login, name = 'login'),
    url(r'^Logout/$', views.Logout, name = 'logout'),
    url(r'^ChangePassword/$', views.ChangePassword, name = 'changepassword'),
    url(r'^home/$', views.Home, name = 'Home'),
    url(r'^Logout/home/$', views.Home, name = 'Home'),
    path('admin/', admin.site.urls),
    url(r'^nav/$', views.nav , name = 'nav'),
    url(r'^index/$', views.index , name = 'index'),
  ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
