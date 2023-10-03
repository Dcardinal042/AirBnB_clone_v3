from flask import Blueprint


app_views = Blueprint("/api/vi")
from api.v1.views.index import *
