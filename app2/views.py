from django.shortcuts import render,redirect

# Create your views here.

from .models import Hostel,Tenant

def manager_dashboard(request):

    hostels = Hostel.objects.all()

    total_hostels = hostels.count()

    total_tenants = sum(i.tenants for i in hostels)

    total_revenue = sum(i.rent for i in hostels)

    context = {
        "hostels":hostels,
        "total_hostels":total_hostels,
        "total_tenants":total_tenants,
        "total_revenue":total_revenue
    }

    return render(request,"manager.html",context)




def add_hostel(request):

    if request.method == "POST":

        name = request.POST.get("name")
        location = request.POST.get("location")
        rooms = request.POST.get("rooms")
        rent = request.POST.get("rent")

        Hostel.objects.create(
            name=name,
            location=location,
            rooms=rooms,
            rent=rent
        )

        return redirect("dashboard")

    return render(request,"add_hostel.html")


def add_tenant(request):

    hostels = Hostel.objects.all()

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        hostel_id = request.POST.get("hostel")
        room = request.POST.get("room")

        hostel = Hostel.objects.get(id=hostel_id)

        Tenant.objects.create(
            name=name,
            phone=phone,
            hostel=hostel,
            room_number=room
        )

        hostel.tenants += 1
        hostel.save()

        return redirect("dashboard")

    return render(request,"add_tenant.html",{"hostels":hostels})