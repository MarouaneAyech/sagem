# services.py

def add_numbers(*args):
    """Additionne tous les nombres passés en arguments."""
    return sum(args)

def greet_user(name, message="Hello"):
    """Affiche un message de salutation."""
    return f"{message}, {name}!"
