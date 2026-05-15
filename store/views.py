from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from .models import Extension, Category

def home(request):
    popular = Extension.objects.order_by('-download_count')[:8]
    new = Extension.objects.order_by('-created_at')[:8]
    categories = Category.objects.annotate(ext_count=Count('extension'))
    
    return render(request, 'store/home.html', {
        'popular': popular,
        'new': new,
        'categories': categories,
    })

def extension_detail(request, slug):
    ext = get_object_or_404(Extension, slug=slug)
    return render(request, 'store/detail.html', {'extension': ext})

def search(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', 'downloads')
    
    extensions = Extension.objects.all()
    
    if query:
        extensions = extensions.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    
    if category:
        extensions = extensions.filter(category__slug=category)
    
    if sort == 'downloads':
        extensions = extensions.order_by('-download_count')
    elif sort == 'rating':
        extensions = extensions.order_by('-rating')
    elif sort == 'new':
        extensions = extensions.order_by('-created_at')
    
    categories = Category.objects.all()
    
    return render(request, 'store/search.html', {
        'extensions': extensions,
        'query': query,
        'category': category,
        'sort': sort,
        'categories': categories,
    })

def download_extension(request, slug):
    ext = get_object_or_404(Extension, slug=slug)
    ext.increment_downloads()
    
    if ext.file:
        return redirect(ext.file.url)
    
    return render(request, 'store/download.html', {'extension': ext})