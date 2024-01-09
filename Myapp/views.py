import sys
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime


import pickle
import string
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')  
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

ps = PorterStemmer()
# tfidf = pickle.load(open('vectorizer.pkl','rb'))
# model = pickle.load(open('model.pkl','rb'))
try:
    with open('vectorizer.pkl', 'rb') as file:
        tfidf = pickle.load(file)
except FileNotFoundError:
    # Handle the case where the file is not found
        tfidf = None 
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    # Handle the case where the file is not found
        model = None 

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)



# 1. preprocess

# 2. vectorize

# 3. predict

# 4. Display
  

def homepage(request):
    return render( request ,'homepage.html')

def Predict(request):
    input =request.GET['temp']
    transformed_sms = transform_text(input)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    if result == 1 :
         return HttpResponse("SPAM")
    else :
         return HttpResponse(transformed_sms)
        
def login(request):
    return render( request ,'loginpage.html');
def fun1(request):
      email=request.POST['email']
      password=request.POST['password']
      try :
            return HttpResponse('<b>Email :- </b>'+email+'<br> <b>Password :- </b>' + password +' <br> ')
      except:
           return HttpResponse(email)
def fun2(request):
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      address_line1=request.POST['address_line1']
      city=request.POST['city']
      state=request.POST['state']
      pincode=request.POST['pincode']
      return HttpResponse('<b>First Name :- </b>'+first_name+'<br> <b>last_name:- </b>' +last_name +' <br> <b>Email :- </b>'+email+'<br> <b>Password :- </b>' + password +' <br> <b>username :- </b>'+username+'<br> <b>Address :- </b>' + address_line1+',' +city+',' +state+','+pincode+' <br> ')
