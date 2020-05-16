from django.shortcuts import render, HttpResponse
from .forms import HomePageForm

def homepage(request):
    if request.method == "POST":
        homepageform = HomePageForm(request.POST)
        try:
            homepageform.save()
        except:
            return render(request, 'homepage/homepage.html', {'form': homepageform})

        return HttpResponse("등록되었습니다")

    else:
        homepageform = HomePageForm()
        return render(request, 'homepage/homepage.html', {'form':homepageform})






# Create your views here.
