from django.http import HttpResponse
from django.shortcuts import render

def page1(request):
    return render(request,'page1.html')

def analyzer(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    ltou = request.GET.get('ltou','off')
    utol = request.GET.get('utol','off')
    removenewline = request.GET.get('removenewline','off')
    removespace = request.GET.get('removespace','off')

    if removepunc == "on" :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Removed Punctutions','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyzetext.html', params)
    if ltou == "on" :
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Convert to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyzetext.html',params)

    if utol == "on":
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose':'Convert to Lowercase','analyzed_text':analyzed}
        # return render(request,'analyzetext.html',params)
        djtext=analyzed
    if removenewline == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char


        params={'purpose':"New Line Removed",'analyzed_text':analyzed}
        # return render(request,'analyzetext.html',params)
        djtext=analyzed

    if (removespace == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on" and ltou != "on" and utol != "on" and removenewline !='on' and removespace != 'on'):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyzetext.html', params)
    # else:
    #      return HttpResponse(djtext)
