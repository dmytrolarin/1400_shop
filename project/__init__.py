from .urls import * 
from .settings import project
import shop


project.register_blueprint(blueprint= shop.shop)