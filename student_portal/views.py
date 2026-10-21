from django.http import HttpResponse

# Create your views here.
def student_home(request):
    return HttpResponse("<h1>Welcome to the Student Home Page</h1>")
def student_profile(request):
    return HttpResponse("Welcome to the Student Profile Page")
def student_courses(request):
    return HttpResponse("Welcome to the Student Courses Page")

