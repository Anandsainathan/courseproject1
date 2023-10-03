import os
from django.shortcuts import redirect, render
from .models import product_list
def file(request):
    return render(request,'add_product.html')

def add_prod(request):
    if request.method == 'POST':
        productname=request.POST['productname']
        price=request.POST['price']
        qnty=request.POST['qnty']        
        image=request.FILES.get('file')
        prd = product_list(Product_name=productname,Product_price=price,Product_quantity=qnty,Image=image)
        print("Save data...")
        prd.save()
        return redirect('showprod')
    
def showprod(request):
    qr = product_list.objects.all()
    return render(request,'show_product.html',{'qr':qr})

def prod_edit(request,px):
    qr = product_list.objects.get(id=px)
    return render(request,'edit_product.html',{'qr':qr})

def edit(request,px):    
    if request.method=='POST':
        prdcts = product_list.objects.get(id=px)
        prdcts.Product = request.POST.get('product')
        prdcts.Price = request.POST.get('price')
        prdcts.Quantity = request.POST.get('qnty')
        if len( request.FILES)!=0:
            if len (prdcts.Image)>0:
                os.remove(prdcts.Image.path)
        prdcts.Image = request.FILES.get('file')
        prdcts.save()
        return redirect('showprod')
    return render(request, 'edit_product.html',)
    
def delete(request,px):
    p = product_list.objects.filter(id=px)
    p.delete()
    return redirect('showprod')
