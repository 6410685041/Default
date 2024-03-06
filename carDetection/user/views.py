from django.shortcuts import render
from user.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from process.models import Task

# Create your views here.


def view_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }

    return render(request, "index.html", data)


def view_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/profile.html", data)

def view_my_queue(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    tasks = Task.objects.all()
    data = {
        "profile": profile,
        "tasks": tasks,
    }
    return render(request, "user/my_queue.html", data)

def view_edit_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/edit_profile.html", data)


def submit_edit_profile(request):
    if request.method == "POST":
        profile = Profile.objects.get(id=request.user.id)
        profile.first_name = request.POST["first_name"]
        profile.last_name = request.POST["last_name"]
        profile.email = request.POST["email"]
        profile.phone_number = request.POST["phone_number"]
        profile.bio = request.POST["bio"]
        profile.save()

        return HttpResponseRedirect(reverse("profile"))
