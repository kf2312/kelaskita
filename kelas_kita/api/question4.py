from django.shortcuts import render
from django.http import HttpResponse
from .models import PageView

# Create your views here.

#http://127.0.0.1:8000/question/2
#
def question2(request):
    i = 1
    number = []
    while i <= 100:
        temp3 = i/3
        temp5 = i/5
        tempStr = str(i)

        if(temp3 - int(temp3) == 0):
            tempStr = tempStr + 'Fizz'

        if(temp5 - int(temp5) == 0):
            tempStr = tempStr + 'Buzz'    

        number.append(tempStr + '<br>')
        i += 1

    #page view
    page_id = 2
    view_object = PageView.objects.get(page_id=page_id)
    view_object.page_views = view_object.page_views + 1
    view_object.save()

    return HttpResponse(number)

#http://127.0.0.1:8000/question/3
def question3(request):
    #page view
    page_id = 3
    view_object = PageView.objects.get(page_id = page_id)
    view_object.page_views = view_object.page_views + 1
    view_object.save()

    number = [0, 1]
    i = 2
    while i <= 8:
        number.append(number[i-1] + number[i-2])
        i += 1
    return HttpResponse(str(number))

    # numberStr = []
    # for x in number:
    #     numberStr.append(str(x) + ', ')
    # return HttpResponse(number)
    
#http://127.0.0.1:8000/question/4
def question4(request):
    #page view
    page_id = 4
    view_object = PageView.objects.get(page_id = page_id)
    view_object.page_views = view_object.page_views + 1
    view_object.save()

    temp2 = 'Question 2: ' + str(PageView.objects.get(page_id = 2).page_views) + ' views <br>'
    temp3 = 'Question 3: ' + str(PageView.objects.get(page_id = 3).page_views) + ' views <br>'
    temp4 = 'Question 4: ' + str(view_object.page_views) + ' views <br>'
    return HttpResponse(temp2 + temp3 + temp4)