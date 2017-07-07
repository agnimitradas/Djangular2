from django.conf.urls import url,include
from django.contrib import admin
from main import urls
from rest_framework.authtoken import views
from auth_api import views as auth_api_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^events/', include(urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^auth_api/login', auth_api_views.LoginView.as_view()),
    url(r'^auth_api/logout', auth_api_views.LogoutView.as_view()),
]
