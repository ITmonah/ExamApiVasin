from .base_models import *
from typing import List, Dict

class CountScheme(CountBase):
    ingredient: IngredientBase
    system_of_calc:System_of_calculationBase

class RecipeScheme(RecipeBase):
    counts:List[CountScheme]