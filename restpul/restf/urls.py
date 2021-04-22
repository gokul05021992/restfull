from django.urls import path
from.import views
#from django.views import Article_list

urlpatterns = [
    path('',views.Article_list,name='articles'),
    path('data/<int:pk>',views.DeleteObject),
    path('articleapi/',views.articleAPI.as_view()),
    path('articleWork/<int:id>/',views.articleWork.as_view()),
    path('generic/',views.genericView.as_view()),
    path('generic/<int:id>/',views.genericView.as_view()),
]