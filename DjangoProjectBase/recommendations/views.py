from django.shortcuts import render
from .models import Recommendation

# Create your views here.
def recommendation(request):
    newss = Recommendation.objects.all()
    return render(request, 'recommendations.html', {'newss':newss})