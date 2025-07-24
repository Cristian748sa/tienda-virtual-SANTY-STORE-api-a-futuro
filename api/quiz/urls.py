from django.urls import path
from .views import home, CategoryList, QuizList, QuestionList

urlpatterns = [
    # Vista HTML
    path('', home, name='home'),
    path('api/categorias/', CategoryList.as_view(), name='api-categorias'),
    path('api/cuestionario/',   QuizList.as_view(),    name='api-cuestionario'),
    path('api/preguntas/', QuestionList.as_view(), name='api-preguntas'),
]
