#resources.py
from import_export import resources
from .models import db
 
class MemberResource(resources.ModelResource):
    class Meta:
        model = db