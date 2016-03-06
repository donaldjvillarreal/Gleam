# coding=utf-8
from django.conf.urls import url
from diagnostic import views


urlpatterns = [
    url(r'^hamd/$', views.hamd_survey, name='hamd_survey'),
    url(r'^bdi/$', views.bdi_survey_pagination, name='bdi_survey'),

    # Case conceptualization
    url(r'^case/$', views.case_index, name='case_index'),
    url(r'^case/problem/$', views.case_problem, name='case_problem'),
    url(r'^case/problem/description/$', views.case_problem_description, name='case_problem_description'),
    url(r'^case/problem/summary/$', views.case_problem_summary, name='case_problem_summary'),
]