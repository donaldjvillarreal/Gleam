# coding=utf-8
from django.conf.urls import url
from caseconcept import views

urlpatterns = [
    url(r'^$', views.case_index, name='case_index'),
    url(r'^problem/$', views.case_problem, name='case_problem'),
    url(r'^problem/description/$', views.case_problem_description, name='case_problem_description'),
    url(r'^problem/summary/$', views.case_problem_summary, name='case_problem_summary'),
    url(r'^problem/goals/$', views.case_goals, name='case_goals'),
    url(r'^problem/goals/rank/$', views.case_goals_rank, name='case_goals_rank'),
    url(r'^problem/goals/rank/confirm/$', views.case_goal_rank_confirm, name='case_goal_rank_confirm'),
    url(r'^calendar/$', views.cal, name='calendar'),
]