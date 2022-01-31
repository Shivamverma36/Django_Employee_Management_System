from django.urls import path
from . import views

urlpatterns = [
    path('addEmpPage',views.addEmpPage,name='addEmpPage'),
    path(' insertEmp',views. insertEmp,name=' insertEmp'),
    path('show',views.show,name='show'),
    path('editEmp/<int:eid>',views.editEmp,name="editEmp"),
    path('updateEmp/<int:eid>',views.updateEmp,name="updateEmp"),
    
]