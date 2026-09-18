from django.http import HttpResponse, JsonResponse
from .models import Question, Choice, Project, Employee


def index(request):
    return HttpResponse("Hello, this is the Polls app!")


def questions(request):
    questions = Question.objects.all()

    data = []

    for question in questions:
        data.append({
            "id": question.id,
            "question_text": question.question_text,
            "pub_date": question.pub_date,
        })

    return JsonResponse(data, safe=False)


def choices(request):
    choices = Choice.objects.all()

    data = []

    for choice in choices:
        data.append({
            "id": choice.id,
            "choice_text": choice.choice_text,
            "votes": choice.votes,
            "question": choice.question.question_text,
        })

    return JsonResponse(data, safe=False)


def projects(request):
    projects = Project.objects.all()

    data = []

    for project in projects:
        data.append({
            "id": project.id,
            "project_name": project.project_name,
            "description": project.description,
        })

    return JsonResponse(data, safe=False)


def employees(request):
    employees = Employee.objects.all()

    data = []

    for employee in employees:
        data.append({
            "id": employee.id,
            "employee_name": employee.employee_name,
            "email": employee.email,
            "phone": employee.phone,
            "designation": employee.designation,
            "salary": employee.salary,
            "project": employee.project.project_name,
        })

    return JsonResponse(data, safe=False)