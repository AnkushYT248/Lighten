from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, custom_404
from registration import views
from django.contrib.auth.views import LogoutView

admin.site.site_title = 'Lighten Site Admin Panel'


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
]

handler404 = custom_404

# Add static and media URL patterns for development
if settings.DEBUG:
    #urlpatterns++static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)