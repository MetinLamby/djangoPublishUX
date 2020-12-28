from django.urls import path
from . import views


app_name = 'predict'

urlpatterns = [
    path('', views.predict, name='predict'),
    path('predict/', views.predict_chances, name='submit_prediction'),
]

##path('', views.predict, name='prediction_page'),
##path('results/', views.view_results, name='results'),
