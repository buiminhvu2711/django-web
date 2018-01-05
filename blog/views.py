from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from blog.models import Blog,Category
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from cart.forms import CartAddProductForm

# Create your views here.
def list(request):
    queryset_list=Blog.objects.all()
    catetogry=Category.objects.all()
    query = request.GET.get("q")
    query_catetogry = request.GET.get('t',None)
    if query_catetogry:
        category = get_object_or_404(Category, pk = query_catetogry)  
    if query:   
        queryset_list = Blog.objects.filter(ten__icontains=query)   
    if query_catetogry:
        queryset_list = Blog.objects.filter(category__name__icontains=category.name)
        # if not queryset_list:
        #     return render(request,'http404.html'
    #phân trang
    paginator = Paginator(queryset_list,6)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    Data = {
        'Blogs': queryset,
        'Categories':  catetogry,    
    }
    return render(request,'blog.html',Data)
 
def post(request, post_id):
    cart_product_form = CartAddProductForm() 
    try:
        Blog.objects.get(pk=post_id)
    except Blog.DoesNotExist :
        # raise Http404("Bài viết không tồn tại.")
        return render(request,'http404.html')
    return render(request,'post.html',{'product':Blog.objects.get(pk=post_id),
                                        'cart_product_form': cart_product_form})
