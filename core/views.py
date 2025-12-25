import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

from django.contrib.auth.hashers import check_password

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! Cybersecurity project is running.")

# FLAW 1: A01 Broken Access Control
def admin_panel(request):
   return HttpResponse("Welcome to the ADMIN PANEL. Sensitive data here!")

# FIX 1 (COMMENTED OUT)
# @login_required
# def admin_panel(request):
#    return HttpResponse("Welcome to the ADMIN PANEL. Sensitive data here!")

from django.db import connection

def search_notes(request):
    query = request.GET.get('q', '')

    cursor = connection.cursor()

# FLAW 2: A03 Injection
    cursor.execute(
        f"SELECT id, title, content FROM core_note WHERE title LIKE '%{query}%'"
    )
    
# FIX 2 (COMMENTED OUT: parameterized query)
#     cursor.execute(
#         "SELECT id, title, content FROM core_note WHERE title LIKE %s",
#         [f"%{query}%"]
#     )

    results = cursor.fetchall()

    response = ""
    for row in results:
        response += f"<p>{row[1]}: {row[2]}</p>"

    return HttpResponse(response)


def crash(request):
    return HttpResponse(1 / 0)
#FIX3 in project/settings.py

from core.models import InsecureUser

def insecure_login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

# FLAW 4: A07 Identification and Authentication Failures

    user = InsecureUser.objects.filter(
        username=username,
        password=password
    ).first()

    if user:
        return HttpResponse("Login successful!")
    else:

# FLAW 5: A09 Security Logging and Monitoring Failures        
        return HttpResponse("Login failed!")
    
# FIX 4 (COMMENTED OUT: hashed password verification)
#     user = InsecureUser.objects.filter(username=username).first()
#     if user and check_password(password, user.password):
#         return HttpResponse("Login successful!")
#     else:

# FIX 5 (COMMENTED OUT: log failed login attempt)
#         logger.warning(
#             f"Failed login attempt for username: {username} from IP: {request.META.get('REMOTE_ADDR')}"
#         )
#         return HttpResponse("Login failed!")
