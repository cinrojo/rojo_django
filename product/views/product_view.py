from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import get_object_or_404

from product.models import Category, Product
from product.repositories.product import ProductRepository
from product.forms import ProductForm
from django.http import HttpRequest

# Instancia del repositorio de productos
repo = ProductRepository()

# Vista para listar todos los productos
class ProductListView(View):
    def get(self, request, *args, **kwargs):
        
        productos = repo.get_all()
        return render(
            request,
            'products/list.html',
            {'products': productos}
        )

# Vista para mostrar el detalle de un producto
class ProductDetailView(View):
    def get(self, request, id, *args, **kwargs):
        
        producto = get_object_or_404(Product, id=id)
        return render(
            request,
            'products/detail.html',
            {'product': producto}
        )

# Vista para eliminar un producto

class ProductDeleteView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id, *args, **kwargs):
        producto = get_object_or_404(Product, id=id)
        repo.delete(producto)
        return redirect('product_list')

# Vista para actualizar un producto, requiere autenticación
class ProductUpdateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id, *args, **kwargs):
        """
        Método GET para obtener y mostrar el formulario de actualización de un producto por su ID.
        """
        product = get_object_or_404(Product, id=id)
        categorias = Category.objects.all()
        form = ProductForm(instance=product)
        return render(
            request,
            'products/update.html',
            {'categories': categorias, 'form': form}
        )

    @method_decorator(login_required(login_url='login'))
    def post(self, request, id, *args, **kwargs):
        """
        Método POST para procesar la actualización de un producto por su ID.
        """
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            producto_nuevo = repo.create(
                nombre=form.cleaned_data['name'],
                descripcion=form.cleaned_data['description'],
                precio=form.cleaned_data['price'],
                cantidades=form.cleaned_data['stock'],
                categoria=form.cleaned_data['category']
            )
            return redirect('product_detail', producto_nuevo.id)
        categorias = Category.objects.all()
        return render(
            request,
            'products/update.html',
            {'categories': categorias, 'form': form}
        )

# Vista para crear un nuevo producto

class ProductCreateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, *args, **kwargs):
        """
        Método GET para obtener y mostrar el formulario de creación de un nuevo producto.
        """
        categorias = Category.objects.all()
        form = ProductForm()
        return render(
            request,
            'products/create.html',
            {'categories': categorias, 'form': form}
        )

    def post(self, request, *args, **kwargs):
        """
        Método POST para procesar la creación de un nuevo producto.
        """
        form = ProductForm(request.POST)
        if form.is_valid():
            producto_nuevo = repo.create(
                nombre=form.cleaned_data['name'],
                descripcion=form.cleaned_data['description'],
                precio=form.cleaned_data['price'],
                cantidades=form.cleaned_data['stock'],
                categoria=form.cleaned_data['category']
            )
            return redirect('product_detail', producto_nuevo.id)
        categorias = Category.objects.all()
        return render(
            request,
            'products/create.html',
            {'categories': categorias, 'form': form}
        )


class ProductGTEStockListView(View):
    def get(self, request: HttpRequest):
        repo = ProductRepository()
        
        min_stock = 0
        max_stock = float('inf')
        
        if request.method == "GET":
            min_stock_str = request.GET.get('min_stock', '0')
            max_stock_str = request.GET.get('max_stock', 'inf')
            
            try:
                min_stock = int(min_stock_str)
                max_stock = int(max_stock_str)
            except ValueError:
                pass
        
        productos = repo.get_product_stock_range(min_stock, max_stock)
        
        return render(
            request,
            'products/list.html',
            {
                'products': productos,
                'min_stock': min_stock,
                'max_stock': max_stock
            }
        )

class ProductLTEStockListView(View):
    def get(self, request: HttpRequest):
        repo = ProductRepository()
        
        stock_threshold = 0  # Esto puede ser cualquier valor que desees
        productos = repo.get_product_lte_stock(stock_threshold)
        
        return render(
            request,
            'products/list.html',
            {
                'products': productos
            }
        )