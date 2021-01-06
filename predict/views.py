from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
##from .models import PredResults

# Create your views here.

def index(request):
  return render(request, 'index.html')

def predict(request):
  return render(request, 'predict.html')

def predict_chances(request):

    if request.POST.get('action') == 'post':

        ## Receive data from client
        title = request.POST.get('title')
        body = request.POST.get('body')

        ## First we need to unpickle the model
        ## the pickled model should be placed here 'predict/MODEL_NAME.pickle'
        ## code line 23 model = ... should initialize the model

        # model = pd.read_pickle('predict/new_model_two.pickle')
        model = pd.read_pickle('predict/rf.pkl')
        result = model.predict(body)


        ## after having initialized the model we will make a predictionMake prediction using the parameters received from JS (see above)

        #result = 80.37

        ## the result, title, and body parameters will then be sent to another page using JS again
        return JsonResponse({'result': result, 'title': title, 'body': body}, safe=False)


def technical_implementation(request):
  return render(request, 'technical_implementation.html')
