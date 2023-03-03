from flask import Blueprint

from ..social import models

bp = Blueprint('main', __name__)

from . import routes, forms