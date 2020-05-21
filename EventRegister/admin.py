from django.contrib import admin
from .models import Register

# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['reg_id', 'fullname', 'reg_date']
    list_filter = ['reg_type']
    search_fields = ['fullname', 'reg_id']
    change_list_template = 'change_list_graph.html'

    def changelist_view(self, request, extra_context=None):
        # Add extra context data to pass to change list template
        t1 = Register.objects.filter(reg_type='self')
        t2 = Register.objects.filter(reg_type='group')
        t3 = Register.objects.filter(reg_type='corporate')
        t4 = Register.objects.filter(reg_type='others')
        extra_context = {'self': len(t1), 'group': len(t2), 'corporate': len(t3), 'others': len(t4)}
        # Execute default logic from parent class changelist_view()
        return super(RegisterAdmin, self).changelist_view(
            request, extra_context=extra_context
        )


admin.site.register(Register, RegisterAdmin)
