from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import myweb.views
import jobs.views
import wordcounter.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', jobs.views.home, name='jobs'),
    path('blog/', include('blog.urls')),
    path('', myweb.views.my_web_home_page, name='home_page'),
    path('wordcounter/', wordcounter.views.wordcounter, name='wordcounter'),
    path('sandbox/', include('sandbox.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
