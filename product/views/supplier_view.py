from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from product.repositories.supplier import SupplierRepository
from product.models import Supplier
from product.forms import SupplierForm
from django.utils.decorators import method_decorator

class SupplierListView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        supplier_repo = SupplierRepository()
        suppliers = supplier_repo.get_all()
        return render(request, 'supplier/list.html', {'suppliers': suppliers})

class SupplierDetailView(LoginRequiredMixin, View):
    login_url = 'login'

    
    def get(self, request, id, *args, **kwargs):
        supplier = get_object_or_404(Supplier, id=id)
        return render(request, 'supplier/detail.html', 
        {'supplier': supplier}
        )

class SupplierDeleteView(View):
    login_url='login'
    def get(self, request, id, *args, **kwargs):
        supplier = get_object_or_404(Supplier, id=id)
        supplier_repo = SupplierRepository()
        supplier_repo.delete(id)
        return redirect('supplier_list')

class SupplierUpdateView(View):
    def get(self, request, id):
        supplier = get_object_or_404(Supplier, id=id)
        form = SupplierForm(instance=supplier)
        return render(request, 'supplier/update.html', {'form': form})

    def post(self, request, id):
        supplier = get_object_or_404(Supplier, id=id)
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
        return render(request, 'supplier/update.html', {'form': form})

class SupplierCreateView(View):
    def get(self, request):
        form = SupplierForm()
        return render(request, 'supplier/create.html', {'form': form})

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
        return render(request, 'supplier/create.html', {'form': form})