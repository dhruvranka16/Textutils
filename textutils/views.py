#i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse("HOME")

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc= request.GET.get('removepunc','off')
    Capitalized= request.GET.get('Capitalized','off')

    print(djtext)


    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for i in range(1):
        if removepunc == 'on':
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char

        else:
            analyzed=djtext


    for i in range(1):
        if Capitalized == 'on':
            analyzed1 = ""

            for char in analyzed:
                analyzed1 = analyzed1 + char.upper()

        else:
            analyzed1=analyzed

    params = {'purpose': 'The operations', 'analyzed_text': analyzed1}
    return render(request, 'analyze.html', params)




