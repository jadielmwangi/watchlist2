es (3 sloc)  90 Bytes
 
from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views,forms