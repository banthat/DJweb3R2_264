from django.shortcuts import render

# Create your views here.
def testbt(request):
    return render(request, 'productApp/testbt.html')