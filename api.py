BASE_LOGO = "https://logotypes.dev/"

def obtener_url_logo(nombre: str) -> str:
    nombre = nombre.strip().lower()
    return f"{BASE_LOGO}{nombre}"