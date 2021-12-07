from django.contrib import admin
from django.urls import path
from . import views
app_name = 'ytproject'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.y2s_down),
    path('download/',views.y2s_download),
    path('download/<resolution>/',views.yt_doanload_done , name='download_done')


]
