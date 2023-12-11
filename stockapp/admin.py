from django.contrib import admin
from .models.json_models import JsonModel  # Adjust the import statement
from .models.sql_models import SqlModel

#register model
admin.site.register(JsonModel)
admin.site.register(SqlModel)