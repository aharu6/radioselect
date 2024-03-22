from django.urls import path
from . import views

app_name = 'selectradioproject'
urlpatterns = [
    path("selectradioprojectPage/",views.selectradioprojectPage,name="selectradioprojectPage"),
    # ex: /selectradioproject/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /selectradioproject/5/
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    # ex: /selectradioproject/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /selectradioproject/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
