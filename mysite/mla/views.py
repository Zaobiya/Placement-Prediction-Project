from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from aimz.models import Course, Job
 
def pre(request):
    return render(request, 'aimz/prediction.html')

def predict_placements(request):
    df = pd.read_csv('C:/Users/Zaobiya Khan/Desktop/Project/mysite/staticfiles/collegePlace.csv')
    
    x = df.drop(['PlacedOrNot', 'Age', 'Hostel'], axis='columns')
    y = df['PlacedOrNot']
    le = preprocessing.LabelEncoder()
    x['Gender'] = le.fit_transform(x['Gender'])
    x['Stream'] = le.fit_transform(x['Stream'])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

    classify = RandomForestClassifier(n_estimators=10, criterion="entropy")
    classify.fit(x_train, y_train)

    # Save the model using Django's file storage
    with open('C:/Users/Zaobiya Khan/Desktop/Project/mysite/staticfiles/model.pkl', 'wb') as f:
        pickle.dump(classify, f)

    # Load the model
    with open('C:/Users/Zaobiya Khan/Desktop/Project/mysite/staticfiles/model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Make predictions
    prediction = model.predict([[1, 1, 1, 0, 0]])

    return render(request, 'aimz/prediction.html', {'prediction': prediction})


def predict(request):
    if request.method == 'POST':
        # Retrieve user input from POST request

        gender = request.POST.get('gender')
        stream = request.POST.get('stream')
        internship = request.POST.get('internship')
        cgpa = request.POST.get('cgpa')
        backlogs = request.POST.get('backlogs')

        # Convert user input to a numpy array
        input_data = np.array([gender, stream, internship, cgpa, backlogs], dtype=float)

        # Load the trained model
        with open('C:/Users/Zaobiya Khan/Desktop/Project/mysite/staticfiles/model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Make prediction
        prediction = model.predict([input_data])[0]
        
        if prediction == 1:
            # User has high chances of getting placed
            jobs = Job.objects.all()
            return render(request, 'aimz/predsuc.html', {'jobs': jobs})
        else:
            # User has low chances of getting placed
            courses = Course.objects.all()
            return render(request, 'aimz/predfail.html', {'courses': courses})

    # If request method is not POST, render the form template
    return render(request, 'aimz/prediction.html')
