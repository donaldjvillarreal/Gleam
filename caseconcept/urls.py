# coding=utf-8
from django.conf.urls import url
from caseconcept import views

urlpatterns = [
    url(r'^$', views.case_index, name='index'),
    url(r'^problem/$', views.case_problem, name='problem'),
    url(r'^problem/description/$', views.case_problem_description, name='problem_description'),
    url(r'^problem/summary/$', views.case_problem_summary, name='problem_summary'),
    url(r'^problem/goals/$', views.case_goals, name='goals'),
    url(r'^problem/goals/rank/$', views.case_goals_rank, name='goals_rank'),
    url(r'^problem/goals/rank/confirm/$', views.case_goal_rank_confirm, name='goal_rank_confirm'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^course/start/$', views.start_course, name='start_course'),
    url(r'^calendar_upd/$', views.calendar_upd, name='calendar_upd')
]