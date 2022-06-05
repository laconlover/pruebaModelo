from django.views import View
from .models import Farmacia
from django.http import JsonResponse
from django.forms.models import model_to_dict

class FarmaciaListView(View):
    def get(self, request):
        fa_list = Farmacia.objects.all()
        return JsonResponse(list(fa_list.values()), safe=False)
        # get..
class FarmaciaDetailView(View):
    def get(self, request, pk):
        farmacia = Farmacia.objects.get(pk=pk)
        return JsonResponse(model_to_dict(farmacia), safe=False)
        # get..

