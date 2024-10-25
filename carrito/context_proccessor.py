
## definimos el total de carrito 
def total_carrito(request):
    total = 0
   
    if "carrito" in request.session.keys():

        for key, value in request.session["carrito"].items():
           
            if isinstance(value, dict) and "acumulado" in value:
                total += int(value["acumulado"])
            else:
                print(f"El valor para la clave '{key}' no es un diccionario o no tiene 'acumulado': {value}")
    
    return {"total_carrito": total}  
