from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render
from django.urls import URLPattern


def index(request):
    return HttpResponse('<h1> Hello World!</h1>')

from bookmarkapp.models import Bookmark
def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()
    context = {'bookmark_list' :bookmark_list}
    return render(request, 'bookmark_list.html', context)

from django.shortcuts import get_object_or_404
def bookmark_detail(request, pk):
    # bookmark = Bookmark.objects.get(id=pk)
    bookmark = get_object_or_404(Bookmark, id=pk)
    context = {'bookmark' : bookmark}
    return render(request, 'bookmark_detail.html', context)

def bookmark_update(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    # context={'bookmark' :bookmark}
    # if request.method == 'POST':
    #     bookmark.title = request.POST['title']
    #     bookmark.url = request.POST['url']
    #     bookmark.memo = request.POST['memo']
    #     bookmark.save()
    #     return redirect(f'/bookmark/{bookmark.id}')
    # return render(request, 'bookmark_update.html', context)
    context = {}

    if request.method == 'POST':
        form = BookmarkFrom(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark = form.save()
            return redirect('bookmarkapp:detail', bookmark.id)
    else:
        form = BookmarkFrom(instance=bookmark)
        context['form'] = form
    return render(request, 'bookmark_update.html',context)

def bookmark_delete(request,pk):
    bookmark = Bookmark.objects.get(id=pk)
    context = {'haha' : bookmark}
    if request.method == 'POST':
        bookmark.delete()
        return redirect('/bookmark/')
    return render(request, 'bookmark_delete.html', context)

from .forms import BookmarkFrom

def bookmark_create(request):
    # bookmark = Bookmark()
    # if request.method == 'POST':
    #     bookmark.title = request.POST['title']
    #     bookmark.url = request.POST['url']
    #     bookmark.memo = request.POST['memo']

    #     bookmark.save()
    #     return redirect(f'/bookmark/{bookmark.id}')
    # return render(request, 'bookmark_create.html')
    context = {}

    if request.method == 'POST':
        form = BookmarkFrom(request.POST)
        if form.is_valid():
            bookmark = form.save()
            return redirect('bookmarkapp:detail', bookmark.id)
    else:
        form = BookmarkFrom()
        context['form'] = form
    return render(request, 'bookmark_create.html',context)

def bookmark_delete(request,pk):
    bookmark = Bookmark.objects.get(id=pk)
    context = {'haha' : bookmark}
    if request.method == 'POST':
        bookmark.delete()
        return redirect('/bookmark/')
    return render(request, 'bookmark_delete.html', context)



from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
class BookmarkListView(ListView):  #(상속받을 값을 적음)
        model = Bookmark           #모델 정하기
        context_object_name = 'bookmark_list'   #context(변수명) 정하기
        # tmeplate_name = 'bookmark_list.html'  #어떤 templates연결한건지 정하기


class BookmarkDetailView(DetailView):
    model = Bookmark
    context_object_name = 'bookmark'
    # template_name = 'bookmark_detail.html'

from django.urls import reverse_lazy
class BookmarkCreateView(CreateView):
    model = Bookmark
    form_class = BookmarkFrom
    # template_name = 'bookmark_create.html'  
    success_url = reverse_lazy('bookmarkapp:list')

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    # template_name = 'bookmark_update.html'
    form_class = BookmarkFrom
    success_url = reverse_lazy('bookmarkapp:list')
    context_object_name = 'bookmark'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    # template_name = 'templates/bookmarkapp/bookmark_delete.html'
    form_class = BookmarkFrom
    success_url = reverse_lazy('bookmarkapp:list')
    context_object_name = 'bookmark'