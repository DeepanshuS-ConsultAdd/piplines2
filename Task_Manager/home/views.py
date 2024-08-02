import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this for demonstration purpose

# Create your views here.

def home(request):
    return HttpResponse("<h1>Heyh! I am Django Server.<h1>")

def myhome(request):
    print("*" * 10)
    return HttpResponse("""
                        <h1>Heyh! sssecond Page<h1>
                        <h1>This is second line<h1>
                        """)

def mypages23(request):
    return render(request, "index.html")

def myhome12(request):
    mylist = [
        {"name": "Deep", "Age": 20 },
        {"name": "Pooja", "Age": 25 }
    ]
    print("*" * 10)
    return JsonResponse(mylist, safe=False)
    # return HttpResponse("""
    #                     <h1>Heyh! sssecond Page<h1>
    #                     <h1>This is second line<h1>
    #                     """)


@csrf_exempt  # Note: Use CSRF protection appropriately in production
def objectdispl(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))   # Assuming 'data' is the key name for JSON in POST request
        # Process the JSON data as needed
        name= data.get('name')
        age= data.get('age')
        print("Received JSON data:")
        print(data)
        return JsonResponse([{'message': 'Received JSON data successfully.'},
                              {"Name": name, "Age" : age },
                             ], safe=False)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    

from rest_framework import viewsets

from .models import TaskDetails
from .serializers import TaskDetailSerializer

class TaskDetailViewSet(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class = TaskDetailSerializer

@csrf_exempt
def checks1(request):
    return HttpResponse("heyhhh from second page")