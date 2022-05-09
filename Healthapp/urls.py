from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_patients),
    path('patient/<int:id>', views.get_patient),
    path('patient/create', views.create_patient),
    path('patient/update/<int:id>', views.update_patient),
    path('patient/delete/<int:id>/', views.delete_patient),
    path('login', views.login_verify),
]
