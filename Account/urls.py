from django.contrib import admin
from django.urls import path
from Auth_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
