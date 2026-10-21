from django.http import HttpResponse

def teaching_staff_home(request):
    return HttpResponse("<h1>Welcome to the Faculty Home Page</h1>")

def teaching_staff_profile(request):
    return HttpResponse("Faculty Profile Page")
