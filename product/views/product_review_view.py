# Importaciones necesarias de Django y de otros módulos del proyecto
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from product.models import ProductReview, Product  # Importa los modelos ProductReview y Product
from product.repositories.product import ProductRepository  # Importa el repositorio de productos
from product.repositories.product_reviews import ProductReviewRepository  # Importa el repositorio de reseñas de productos
from product.forms import ProductReviewForm  # Importa el formulario de reseñas de productos


# Vista para listar todas las reseñas de productos
class ProductReviewView(View):
    def get(self, request, *args, **kwargs):
        repo = ProductReviewRepository()  # Instancia el repositorio de reseñas de productos
        reviews = repo.get_all()
        if request.user.is_authenticated and not request.user.is_staff:
            reviews = reviews.filter(author=request.user)
        reviews = repo.get_all()  # Obtiene todas las reseñas
        return render(
            request,
            'product_reviews/list.html',  # Renderiza la plantilla 'list.html'
            dict(
                reviews=reviews  # Pasa las reseñas a la plantilla
            )
        )


# Vista para crear una nueva reseña de producto

class ProductReviewCreateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, *args, **kwargs):
        repo = ProductRepository()  # Instancia el repositorio de productos
        products = repo.get_all()  # Obtiene todos los productos
        return render(
            request,
            'product_reviews/create.html',  # Renderiza la plantilla 'create.html'
            dict(
                products=products  # Pasa los productos a la plantilla
            )
        )
    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        repo = ProductReviewRepository()  # Instancia el repositorio de reseñas de productos

        # Obtiene los datos del formulario
        product_id = request.POST.get('id_producto')
        review = request.POST.get('opinion')
        value = request.POST.get('valoracion')
        user = request.user

        # Crea una nueva reseña usando el repositorio
        repo.create(
            product_id=product_id,
            author=user,
            text=review,
            rating=value,
        )
        return redirect('product_reviews')  # Redirige a la lista de reseñas


# Vista para mostrar el detalle de una reseña de producto
class ProductReviewDetailView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)  # Obtiene la reseña o devuelve un 404 si no existe
        return render(
            request,
            'product_reviews/detail.html',  # Renderiza la plantilla 'detail.html'
            dict(review=review)  # Pasa la reseña a la plantilla
        )


# Vista para actualizar una reseña de producto

class ProductReviewUpdateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)  # Obtiene la reseña o devuelve un 404 si no existe
        form = ProductReviewForm(instance=review)  # Crea un formulario con los datos de la reseña existente
        return render(
            request,
            'product_reviews/update.html',  # Renderiza la plantilla 'update.html'
            dict(
                form=form  # Pasa el formulario a la plantilla
            )
        )
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        review = get_object_or_404(ProductReview, id=id)  # Obtiene la reseña o devuelve un 404 si no existe
        form = ProductReviewForm(request.POST, instance=review)  # Crea un formulario con los datos del POST y de la reseña existente
        if form.is_valid():
            form.save()  # Guarda los cambios en la reseña
            return redirect('product_reviews')  # Redirige a la lista de reseñas
        return render(
            request,
            'product_reviews/update.html',  # Si el formulario no es válido, renderiza la plantilla 'update.html' de nuevo
            dict(
                form=form  # Pasa el formulario (con errores) a la plantilla
            )
        )

# Vista para eliminar una reseña de producto

class ProductReviewDeleteView(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        repo = ProductReviewRepository()  # Instancia el repositorio de reseñas de productos
        review = get_object_or_404(ProductReview, id=id)  # Obtiene la reseña o devuelve un 404 si no existe
        repo.delete(review)  # Elimina la reseña usando el repositorio
        return redirect('product_reviews')  # Redirige a la lista de reseñas