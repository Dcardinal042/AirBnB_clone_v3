from flask import Blueprint


app_views = Blueprint("/api/vi", import_name="api.v1.views.index")
