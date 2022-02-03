"""contoso_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from course.views import CourseListCreateView, CourseView
from department.views import DepartmentListCreateView, DepartmentView
from enrollment.views import EnrollmentListCreateView, EnrollmentView
from person.views import PersonListCreateView, PersonView

urlpatterns = [
    path('course', CourseListCreateView.as_view()),
    path('course/<int:pk>', CourseView.as_view()),
    path('department', DepartmentListCreateView.as_view()),
    path('department/<int:pk>', DepartmentView.as_view()),
    path('enrollment', EnrollmentListCreateView.as_view()),
    path('enrollment/<int:pk>', EnrollmentView.as_view()),
    path('person', PersonListCreateView.as_view()),
    path('person/<int:pk>', PersonView.as_view()),

]
