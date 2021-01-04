from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
##from .models import PredResults

# Create your views here.

def predict(request):
  return render(request, 'predict.html')

def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        title = request.POST.get('title')
        body = request.POST.get('body')

        # Unpickle model
        #model = pd.read_pickle('predict/new_model_two.pickle')
        # Make prediction
        #result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        #classification = result
        classification = 9

        ##PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   #petal_width=petal_width, classification=classification)

        return JsonResponse({'result': classification, 'title': title, 'body': body}, safe=False)


#def view_results(request):
    # Submit prediction and show all
    #data = {"dataset": PredResults.objects.all()}
    #return render(request, "results.html", data)
