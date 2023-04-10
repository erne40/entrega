# entrega
Pre-entrega 3, base de la entrega final

Existen 3 URLs configuradas:
    ''
    libro/
    buscar/

[Los puntos I), II) y III) heredan de "base.html" (que es un template básico de HTML)]

I) Si accedes a "http://127.0.0.1:8000" puedes ver la página de bienvenida a la página

II) Si accedes a "http://127.0.0.1:8000/libro/" puedes crear una entrada en la base de datos de libros
    Los atributos de este son:
    1.- titulo
    2.- autor
    3.- publicacion (año de)
    4.- editorial
    
    (Los atributos están en "models.py")

III) Si accedes a "http://127.0.0.1:8000/buscar/" puedes buscar un libro por título.
        Si se encuentra un título que contenga lo que buscas se mostrarán todas las coincidencias,
        de otra manera sólo aparecerá el mensaje "No hay coincidencias"
