# Importa el módulo forms de Django
from django import forms
# Importa los modelos Category, Product, Supplier, ProductReview, PriceHistory, y ProductImage desde el módulo actual
from .models import Category, Product, Supplier, ProductReview, PriceHistory, ProductImage

# Definición de un formulario basado en el modelo Category
class CategoryForm(forms.ModelForm):
    # Configuración adicional del formulario
    class Meta:
        # Especifica que este formulario usa el modelo Category
        model = Category
        # Incluye todos los campos del modelo Category en el formulario
        fields = '__all__'


# Definición de un formulario basado en el modelo Product
class ProductForm(forms.ModelForm):
    # Configuración adicional del formulario
    class Meta:
        # Especifica que este formulario usa el modelo Product
        model = Product
        # Incluye los campos específicos del modelo Product en el formulario
        fields = ['name', 'category', 'price', 'stock', 'description']
        # Especifica widgets personalizados para los campos del formulario
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),  # Input de texto con clases CSS personalizadas
            'category': forms.Select(attrs={'class': 'form-control custom-class'}),  # Dropdown de selección con clases CSS personalizadas
            'price': forms.NumberInput(attrs={'class': 'form-control custom-class'}),  # Input numérico con clases CSS personalizadas
            'stock': forms.NumberInput(attrs={'class': 'form-control custom-class'}),  # Input numérico con clases CSS personalizadas
        }


# Definición de un formulario basado en el modelo Supplier
class SupplierForm(forms.ModelForm):
    # Configuración adicional del formulario
    class Meta:
        # Especifica que este formulario usa el modelo Supplier
        model = Supplier
        # Incluye todos los campos del modelo Supplier en el formulario
        fields = ['name','address','phone',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),  # Input de texto con clases CSS personalizadas
            'address': forms.Select(attrs={'class': 'form-control custom-class'}),  # Dropdown de selección con clases CSS personalizadas
            'phone': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            }



# Definición de un formulario basado en el modelo ProductReview
class ProductReviewForm(forms.ModelForm):
    # Configuración adicional del formulario
    class Meta:
        # Especifica que este formulario usa el modelo ProductReview
        model = ProductReview
        # Incluye campos específicos del modelo ProductReview en el formulario
        fields = [
            "product",   # Campo para el producto que se está revisando
            "author",    # Campo para el autor de la reseña
            "text",      # Campo para el texto de la reseña
            "rating",    # Campo para la calificación del producto
        ]
        # Especifica widgets personalizados para los campos del formulario
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control custom-class'}),
            'author': forms.Select(attrs={'class': 'form-control custom-class'}),
            'text': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
        }


# Definición de un formulario basado en el modelo PriceHistory
class PriceHistoryForm(forms.ModelForm):
    # Configuración adicional del formulario
    class Meta:
        # Especifica que este formulario usa el modelo PriceHistory
        model = PriceHistory
        # Incluye todos los campos del modelo PriceHistory en el formulario
        fields = '__all__'


# Definición de un formulario basado en el modelo ProductImage
class ProductImageForm(forms.ModelForm):
    # Configuración adicional del formulario
    class Meta:
        # Especifica que este formulario usa el modelo ProductImage
        model = ProductImage
        # Incluye todos los campos del modelo ProductImage en el formulario
        fields = '__all__'
