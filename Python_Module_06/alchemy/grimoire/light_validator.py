from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    if any(item in lowered for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
