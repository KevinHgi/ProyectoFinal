from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, UsuarioForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .mixins import SuperStaffMixin



def home(request):
    posts = Post.objects.all()
    context = {'post':posts}
    return render(request, "Post/post_page.html", context)

@login_required
def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'Post/post.html', context)

@login_required
def formulario(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect (home)
        
    context = {'form':form}
    return render(request, 'Post/form_post.html', context)


def deletepost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect(home)


    context = {'post': post}
    return render(request, 'delete_template.html', context)


def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    update = 1

    if request.method=='POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        form.save()
        return redirect('home')
    
    context = {"form":form, "update":update}
    return render(request,'Post/form_post.html', context)

def registro(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method=="POST":
        formulario=UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        data['form']=formulario

    return render(request, 'registration/registro.html', data)

def leerPost(request):    
    post = Post.objects.all()
    contexto = {'post': post}
    return render(request, "Post/leer_post.html", contexto)

def eliminar_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')
