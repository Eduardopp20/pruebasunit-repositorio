def sumar(a, b):
    """Suma dos números."""
    if isinstance(a, str) or isinstance(b, str):
        return "Error: no se puede sumar una letra con un número"
    return a + b
