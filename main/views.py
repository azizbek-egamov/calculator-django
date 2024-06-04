from django.shortcuts import render

# Create your views here.

# def HomePage(request):
#     n1 = int(request.GET.get('n1'))
#     n2 = int(request.GET.get('n2'))
    
#     if request.GET.get("plus"):
        
def HomePage(request):
    if request.method == 'POST':
        res = request.POST
        
        n1 = int(res.get("n1"))
        n2 = int(res.get("n2"))
        
        plus = res.get("plus")
        minus = res.get("minus")
        bolish = res.get("bolish")
        kopaytir = res.get("kopaytir")
        
        if plus:
            m = n1 + n2
        elif minus:
            m = n1 - n2
        elif bolish:
            try:
                m = n1 / n2
            except ZeroDivisionError:
                m = "♾"
        elif kopaytir:
            m = n1 * n2
        
        return render(request, 'index.html', {'res': m, 'm1': n1, 'm2': n2})
        
        
    return render(request, 'index.html')