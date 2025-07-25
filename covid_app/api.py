from django.http import JsonResponse

def trend_data(request):
    return JsonResponse({
        "labels": ['Jul 18','Jul 19','Jul 20','Jul 21','Jul 22','Jul 23'],
        "data": [1000, 1100, 900, 950, 1020, 980]
    })
