from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import FinanzasPersonales
from .serializador import serializarCampos

def home(request):
    return HttpResponse('Hello people, welcome in your finances')


@csrf_exempt
def finanzas_metodos(request):
    if request.method == 'GET':
        campos = FinanzasPersonales.objects.all()
        serializer = serializarCampos(campos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        datos = JSONParser().parse(request)
        serializer = serializarCampos(data=datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)