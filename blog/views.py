from django.shortcuts import render
from .models import Publicacion
from django.utils import timezone

# Create your views here.
def listar_pub(request):
    pub=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request,'blog/listar_pub.html',{'pub':pub})