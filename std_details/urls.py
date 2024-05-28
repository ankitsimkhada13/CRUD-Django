from django.urls import path
from . import views

urlpatterns = [
    path('', views.std_list, name="std_list"),
    path('delete/<int:id>', views.std_delete, name="std_delete"),
    path('<int:id>', views.std_edit, name="std_edit"),
    

    # Add other URL patterns as needed
]
