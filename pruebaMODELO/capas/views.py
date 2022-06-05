from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Capa

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def index(request):
  capas = Capa.objects.all()

  # Con la linea de abajo se pueden obtener todos los permisos:
  # codename y name sacan el texto de los permisos
  # group creo que se refiere al groupID interno
  # opciones disponibles: codename, content_type, content_type_id, group, id, name, user
  perm = Permission.objects.filter().values_list('name', flat=True)
  # print(perm.count())-->28 con los que trae por defecto mas los CRUD de capas(4)
  
  ##############################################
  
  # NO EXISTIA EL GRUPO Y LO CREÓ Y LE AÑADIÓ EL PERMISO
  new_group, created = Group.objects.get_or_create(name='urbanismo')
  ct = ContentType.objects.get_for_model(Capa)
  
  permission = Permission.objects.create(codename='puede_hacer_cositas_plus', name='Puede hacer mas cositas', content_type=ct)
  new_group.permissions.add(permission) # Lo añade ya a los Chosen Permissions del group
  
   # con el siguiente comando podemos obtener los de un modelo determinado
  perm = Permission.objects.filter(content_type__app_label='capas', content_type__model='capa')
  # all_permissions = Permission.objects.filter(content_type=content_type)
  print(perm)

  # Permisos de un usuario? See line below
  # perm = Permission.objects.filter(user__username="pepa@1perez")

  """
    # class ReadOnlyAdminMixin:

  #     def has_add_permission(self, request):
  #         return False

  #     def has_change_permission(self, request, obj=None):

  #         if request.user.has_perm('inventory.change_product'):
  #             return True
  #         else:
  #             return False

  #     def has_delete_permission(self, request, obj=None):
  #         return False

  #     def has_view_permission(self, request, obj=None):
  #         return True

  # @admin.register(Product)
  # class ProductAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
  #     list_display = ("name", )

  #     # def get_form(self, request, obj=None, **kwargs):
  #     #     form = super().get_form(request, obj, **kwargs)
  #     #     is_superuser = request.user.is_superuser

  #     #     if not is_superuser:
  #     #         form.base_fields['name'].disabled = True
  #     #     return form
  """

  return render(request, "capas/index.html", {
    "capas": capas
  })

def capa_detail(request, slug):
  capa = get_object_or_404(Capa, slug=slug)
  return render(request, "capas/capa_detail.html", {
    "nombre": capa.nombre,
    "descripcion": capa.descripcion,
    "filtrada": capa.filtrada
  })