from django.contrib import admin
from django.urls import path
from main.views import home, field_detail 

urlpatterns = [
    path('admin/', admin.site.urls),  # URL สำหรับหน้า admin
    path('', home, name='home'),  # URL สำหรับหน้าแรก
    path('field/', field_detail, name='field_detail'),  # URL สำหรับหน้ารายละเอียดสนาม
]
