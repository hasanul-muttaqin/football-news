from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406413331',
        'name': 'Hasanul Mutttaqin',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)



# Create your views here.
