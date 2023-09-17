from django.contrib import admin
from django.urls import path, include  # Import include to include your app's URLs
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create_student, name='create_student'),
    path('list/', views.student_list, name='student_list'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]
