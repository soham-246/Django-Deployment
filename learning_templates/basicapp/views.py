from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello','number':24}
    return render(request,'basicapp/index.html',context_dict)

def other(request):
    return render(request,'basicapp/others.html')

def relative(request):
    return render(request,'basicapp/rel_url_temp.html') 
    
        