from django.urls import path,include
from.import views
from rest_framework.routers import DefaultRouter
#from django.views import Article_list

router=DefaultRouter()
router.register('article',views.ArticleViewSet,basename='article')


urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('',views.Article_list,name='articles'),
    path('data/<int:pk>',views.DeleteObject),
    path('articleapi/',views.articleAPI.as_view()),
    path('articleWork/<int:id>/',views.articleWork.as_view()),
    path('generic/',views.genericView.as_view()),
    path('generic/<int:id>/',views.genericView.as_view()),
]