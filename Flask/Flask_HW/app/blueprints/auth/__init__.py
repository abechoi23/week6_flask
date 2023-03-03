from flask import Blueprint

from ..social import models

bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import routes, forms