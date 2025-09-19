from .urls import * 
from .settings import project
import shop
from .loadenv import load_env
from .db import *
from shop.models import *


project.register_blueprint(blueprint= shop.shop)