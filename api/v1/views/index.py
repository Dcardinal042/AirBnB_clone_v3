#!/usr/bin/python3xx
"""api status"""
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def returnstuff():
    """return stuff"""
    return jsonify(status="OK")


@app_views.route("/stats", strict_slashes=False)
def stuff():
    """JSON Responses"""
    todos = {
        "states": models.State,
        "users": models.User,
        "amenities": models.Amenity,
        "cities": models.City,
        "places": models.Place,
        "reviews": models.Review,
    }
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
