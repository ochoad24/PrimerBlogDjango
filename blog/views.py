from django.shortcuts import render,get_object_or_404,redirect
from .models import Publicacion
from django.utils import timezone
from .forms import FormPub

# Create your views here.
def listar_pub(request):
    pub=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request,'blog/listar_pub.html',{'pub':pub})

def detalle_pub(request,pk):
    pub=get_object_or_404(Publicacion,pk=pk)
    return render(request,'blog/detalle_pub.html',{'pub':pub})

def nuevo_pub(request):
    if request.method == "POST":
        form = FormPub(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        form = FormPub()
    return render(request, 'blog/nuevo_pub.html', {'form': form})

def editar_pub(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = FormPub(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        form = FormPub(instance=post)
    return render(request, 'blog/editar_pub.html', {'form': form})
    
