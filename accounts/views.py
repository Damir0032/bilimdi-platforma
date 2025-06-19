from django.http import HttpResponse
from django.shortcuts import render, redirect
from .firebase_config import auth, db
from django.contrib import messages
import os
from django.http import HttpRequest

def check_key(request):
    key = os.getenv("OPENAI_API_KEY")
    return HttpResponse(f"Done: {key[:8]}...")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')

        try:
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            # Firestore-ге жазу
            db.collection('users').document(uid).set({
                'name': name,
                'email': email,
                'city': city,
                'role': 'student'  # немесе 'teacher', 'moderator' – ролдерге қарай
            })
            messages.success(request, 'Тіркелу сәтті аяқталды. Енді жүйеге кіріңіз.')
            return redirect('login')
        except:
            messages.error(request, 'Тіркелу кезінде қате шықты.')
    return render(request, 'register.html')


from django.shortcuts import render, redirect
from django.contrib import messages
import pyrebase
from firebase_admin import firestore
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_firebase = auth.sign_in_with_email_and_password(email, password)
            uid = user_firebase['localId']
            request.session['uid'] = uid

            # Django-да тіркелген қолданушыны табамыз немесе жасаймыз
            user, created = User.objects.get_or_create(username=uid, defaults={'email': email})
            django_login(request, user)  # Django сессиясына енгізу

            return render(request, 'base.html')

        except:
            messages.error(request, 'Қате email немесе құпиясөз')

    return render(request, 'login.html')


def base_view(request):
    return render(request, 'base.html')

def home(request):
    uid = request.session.get('uid')
    if uid:
        user_doc = db.collection('users').document(uid).get()
        user_data = user_doc.to_dict() if user_doc.exists else {}
        return render(request, 'home.html', {'user': user_data})
    return redirect('login')


def logout_view(request):
    request.session.flush()
    return redirect('login')

def courses_view(request):
    user = request.user

    # Мұғалім екенін тексеру (егер топ қолдансаңыз)
    is_teacher = user.groups.filter(name='Teacher').exists()

    # Firestore-дан курстарды алу
    db = firestore.client()
    courses_ref = db.collection('courses')
    docs = courses_ref.stream()

    courses = []
    for doc in docs:
        data = doc.to_dict()
        courses.append({
            'title': data.get('title'),
            'description': data.get('description'),
            'author': data.get('author', 'Белгісіз'),
            'date': data.get('date', '')
        })

    return render(request, 'courses.html', {
        'is_teacher': is_teacher,
        'courses': courses
    })

def tests_view(request):
    return render(request, 'tests.html')

def results_view(request):
    return render(request, 'results.html')