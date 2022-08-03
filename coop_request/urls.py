from django.urls import path,include,re_path
from .import views
#from django.conf.urls import url
urlpatterns = [
     path('',views.project_list,name='list'),
    path('request/',views.request_form,name='form'),
    path('<int:id>/', views.request_form,name='project_update'),
    path('delete/<int:id>/',views.project_delete,name='project_delete'),
re_path(r'^export-exl/$', views.export, name='export'),
#re_path(r'^search/$', views.search, name='search'),
#re_path(r'^export-csv/$', views.export, name='export')
]
