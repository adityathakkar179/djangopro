from django.contrib import admin
from .models import info



# Register your models here.
@admin.register(info)
class infoAdmin(admin.ModelAdmin):
    list_display = ('title','headertext')

  #  def has_add_permission(self, request,obj=None):
  #      return False

    def has_delete_permission(self, request,obj=None):
        return False


