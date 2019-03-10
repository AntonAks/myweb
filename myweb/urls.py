from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import myweb.views
import jobs.views
import control_panel.views


urlpatterns = [
    path('', myweb.views.my_web_home_page, name='home_page'),
    path('jobs/', jobs.views.home, name='jobs'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('controlpanel/', control_panel.views.control_panel, name='controlpanel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
