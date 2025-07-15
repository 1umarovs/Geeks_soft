from django.contrib import admin
from .models.main_model import *
# Register your models here.


admin.site.site_header = "Geeks Soft Admin"
admin.site.site_title = "Geeks Soft Admin Portal"

admin.site.register(CustomerOpinion)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(FAQ)
admin.site.register(OurContact)