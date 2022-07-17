import csv
import datetime

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse


class Employee:
    def __init__(self, id, first_name, last_name,
                birthdate, job, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
        self.job = job
        self.salary = int(salary)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Employee(id={self.id!r}, first_name={self.first_name!r})'


def read_db():
    employees = []
    with open('employees.csv', 'r') as f:
        rd = csv.DictReader(f, fieldnames=[
            'id',
            'first_name',
            'last_name',
            'birthdate',
            'job',
            'salary'
        ])
        next(rd)

        for row in rd:
            employees.append(Employee(**row))

    return employees


def home(request: HttpRequest) -> HttpResponse:
    employees = read_db()
    return render(request, "home.html", context={
        "employees": employees
    })


def about(request):
    content = render_to_string("page.html", {
        "content": "<h1>Founded in 1823</h1>"
    })
    return HttpResponse(content)


def get_profile_list(request):
    content = render_to_string("page.html", {
        "content": "list of profiles"
    })
    return HttpResponse(content)


def get_profile(request, username):
    content = render_to_string("page.html", context={
        'content': f"Hello, my name is: {username}"
    })
    return HttpResponse(content)


def add(request, x, y):
    content = render_to_string("page.html", context={
        'content': f"<strong>{x} + {y} = {x + y}</strong>."
    })
    return HttpResponse(content)
