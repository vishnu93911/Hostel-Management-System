from django.urls import path
from .views import manager_dashboard, add_hostel, add_tenant

urlpatterns = [

    path("dashboard/", manager_dashboard, name="dashboard"),
    path("add-hostel/", add_hostel, name="add_hostel"),
    path("add-tenant/", add_tenant, name="add_tenant"),

]