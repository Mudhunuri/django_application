from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import db
 
@admin.register(db)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ("WO","CUName")
    pass