from django.shortcuts import render

def courses_view(request):
    role = request.user.groups.first().name if request.user.is_authenticated else 'anonymous'
    return render(request, 'courses.html', {'user_role': role})

def course_list(request):
    return render(request, 'courses.html')  # Бұл шаблон /templates ішінде орналасқан
