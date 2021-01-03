from django.urls import path
from .views import *
app_name = 'calculation'
urlpatterns = [
    path('sequential', Sequential.as_view()),
    path('comprehension', Comprehension.as_view()),
    path('generators', Generators.as_view()),
    path('multiprocessing', Generators.as_view())
]