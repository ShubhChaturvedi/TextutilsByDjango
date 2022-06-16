# this file is created by shubh

from turtle import title
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request , 'index.html')

def analyseResult(request):
    text = request.GET.get('text' , 'no text found')
    removepun = request.GET.get('removePunctuation' , 'off')
    removeWhiteSpace = request.GET.get('removeWhiteSpace' , 'off')
    title = request.GET.get('title' , 'off')
    analysed = text
    
    if removepun=='on':
        analysed = ''
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in text:
            if char not in punc:
                analysed = analysed + char
    temp = analysed.split()
    count = len(temp)
    if removeWhiteSpace=='on':
        analysed = " ".join(temp)
    if title == 'on':
        analysed = analysed.title()
    if title=='off' and removepun=='off' and removeWhiteSpace=='off':
        return HttpResponse("<h2>Select an operation</h2>")
    params = {'text' : analysed ,'count' : count}
    return render(request , 'analyse.html' , params)

