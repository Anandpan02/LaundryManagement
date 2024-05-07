"""LaundryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from laundryapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login/', admin_login, name="admin_login"),
    path('admin_logout/', admin_logout, name="admin_logout"),
    path('user_logout/', user_logout, name="user_logout"),
    path('user_logout', user_logout, name="user_logout"),
    path('user_signin/', user_signin, name="user_signin"),
    path('user_signin', user_signin, name="user_signin"),
    path('user_signup', user_signup, name="user_signup"),
    path('user_signup/', user_signup, name="user_signup"),
    path('user_profile/', user_profile, name="user_profile"),
    path('user_dashboard/', user_dashboard, name="user_dashboard"),
    path('user_change_password/', user_change_password, name="user_change_password"),
    path('change_password/', change_password, name="change_password"),
    path('dashboard/', dashboard, name="dashboard"),
    path('laundry_request/', laundry_request, name="laundry_request"),
    path('requestlist/', requestlist, name="requestlist"),
    path('view_reg_user/', view_reg_user, name="view_reg_user"),
    path('add_laundry_price/', add_laundry_price, name="add_laundry_price"),
    path('view_laundry_price/', view_laundry_price, name="view_laundry_price"),
    path('between_dates/', between_dates, name="between_dates"),
    path('count_report/', count_report, name="count_report"),
    path('delete_request/<int:pid>', delete_request, name="delete_request"),
    path('delete_laundry_price/<int:pid>', delete_laundry_price, name="delete_laundry_price"),
    path('delete_user_detail/<int:pid>', delete_user_detail, name="delete_user_detail"),
    path('detail_request/<int:pid>', detail_request, name="detail_request"),
    path('edit_laundry_price/<int:pid>', edit_laundry_price, name="edit_laundry_price"),
    path('about/', edit_about, name="edit_about"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

