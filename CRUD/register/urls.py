from django.urls import path
from register import views
urlpatterns = [
    path('', views.add_show, name="add_show"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('update/<int:id>/',views.update_stud,name="update"),
]
