from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product.repositories.category import CategoryRepository
from product.repositories.product import ProductRepository
from product.forms import CategoryForm  # Importa el formulario de categoría
from product.models import Category  # Importa el modelo de categoría



# Vista basada en clase para listar todas las categorías
class CategoryListView(View):
    def get(self, request):
        # Instancia del repositorio de categorías
        category_repository = CategoryRepository()
        # Obtiene todas las categorías desde el repositorio
        categories = category_repository.get_all()
        # Renderiza la plantilla 'list.html' con las categorías obtenidas
        return render(
            request,
            'categories/list.html',
            {'categories': categories}
        )


# Vista basada en clase para mostrar el detalle de una categoría
class CategoryDetailView(View):
    def get(self, request, id):
        # Instancias de los repositorios de categorías y productos
        category_repository = CategoryRepository()
        product_repository = ProductRepository()
        # Obtiene la categoría por su ID desde el repositorio de categorías
        category = category_repository.get_by_id(id)
        # Filtra los productos por la categoría obtenida
        products = product_repository.filter_by_category(category)
        # Renderiza la plantilla 'detail.html' con la categoría y los productos obtenidos
        return render(
            request,
            'categories/detail.html',
            {'category': category, 'products': products}
        )


# Vista basada en clase para eliminar una categoría
class CategoryDeleteView(View):
    
    def get(self, request, id):
        # Instancia del repositorio de categorías
        category_repository = CategoryRepository()
        # Obtiene la categoría por su ID desde el repositorio
        category = category_repository.get_by_id(id)
        # Elimina la categoría usando el método delete del repositorio
        category_repository.delete(category)
        # Redirige a la vista de listado de categorías después de la eliminación
        return redirect('category_list')


# Vista basada en clase para actualizar una categoría
class CategoryUpdateView(View):
    
    def get(self, request, id):
        # Instancia del repositorio de categorías
        category_repository = CategoryRepository()
        # Obtiene la categoría por su ID desde el repositorio
        category = category_repository.get_by_id(id)
        # Crea un formulario con los datos de la categoría obtenida
        form = CategoryForm(instance=category)
        # Renderiza la plantilla 'update.html' con el formulario de categoría
        return render(
            request,
            'categories/update.html',
            {'form': form}
        )
    
   
    def post(self, request, id):
        
        # Instancia del repositorio de categorías
        category_repository = CategoryRepository()
        # Obtiene la categoría por su ID desde el repositorio
        category = category_repository.get_by_id(id)
        # Crea un formulario con los datos del POST y la instancia de la categoría
        form = CategoryForm(request.POST, instance=category)
        # Verifica si el formulario es válido
        if form.is_valid():
            # Guarda los cambios en la categoría si el formulario es válido
            form.save()
            # Redirige a la vista de listado de categorías después de la actualización
            return redirect('category_list')
        # Si el formulario no es válido, renderiza de nuevo la plantilla 'update.html' con el formulario
        return render(
            request,
            'categories/update.html',
            {'form': form}
        )


# Vista basada en clase para crear una nueva categoría
class CategoryCreateView(View):
    
    def get(self, request):
        # Crea un formulario vacío de categoría
        form = CategoryForm()
        # Renderiza la plantilla 'create.html' con el formulario vacío
        return render(
            request,
            'categories/create.html',
            {'form': form}
        )
    
    def post(self, request):
        
        # Crea un formulario con los datos del POST
        form = CategoryForm(request.POST)
        # Verifica si el formulario es válido
        if form.is_valid():
            # Guarda la nueva categoría si el formulario es válido
            form.save()
            # Redirige a la vista de listado de categorías después de la creación
            return redirect('category_list')
        # Si el formulario no es válido, renderiza de nuevo la plantilla 'create.html' con el formulario y errores
        return render(
            request,
            'categories/create.html',
            {'form': form}
        )
