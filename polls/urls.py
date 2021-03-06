from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/choice/', views.choice, name='choice'),
    path('<int:question_id>/comment/', views.comment, name='comment'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
