from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/',views.handleregister,name='register'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),

  #  path('userdata', views.userdata, name='userdata'),
    path('org_reg/', views.org_reg, name='org_reg'),
    path('food_new_search/',views.food_new_search,name='food_new_search'),
    path('edu_new_search/',views.edu_new_search,name='edu_new_search'),
    path('cloth_new_search/',views.cloth_new_search,name='cloth_new_search'),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)