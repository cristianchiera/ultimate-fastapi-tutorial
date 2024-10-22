from fastapi import FastAPI, APIRouter
from datetime import date
from datetime import datetime
import uuid


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, Policies"}


@api_router.get("/health", status_code=200)
def health() -> dict:
    """
    Health Check
    """
    return {"status": "ok"}

@api_router.get("/quiensos", status_code=200)
def health() -> dict:
    """
    Quien sos Check
    """
    return {"mensaje": "I'm a API an this is one endpoint"}

@api_router.get("/quiensos/{name}", status_code=200)
async def health(name: str) -> dict:
    """
    interactuando con un parametro Check
    """
    return {"mensaje": "I'm a FastAPI y vos " + name + " esta enviando un request al que estoy respondiendo"}


@api_router.get("/hoy", status_code=200)
async def get_cowsay() -> dict:
    """
    Fecha Check
    """
    #Día actual
    today = date.today()

    #Fecha actual
    now = datetime.now()

    return {"status": "ok", "today": today, "now": now}

@api_router.get("/fibo/{n}", status_code=200)
async def get_fibo(n: int) -> dict:
    """
    Devuelve un diccionario con la serie de Fibonacci hasta el n-ésimo término.

    :param n: El número de términos de la serie que se desea obtener.
    :return: Diccionario con los términos de la serie Fibonacci.
    """
    if n < 1:
        return {"error": "El número debe ser mayor o igual a 1"}

    fib_series = {0: 0, 1: 1}
    for i in range(2, n):
        fib_series[i] = fib_series[i - 1] + fib_series[i - 2]
    
    return {i: fib_series[i] for i in range(n)}


#uuid
def generate_uuid_from_number(number: int) -> str:
    """
    Genera un UUID basado en un número dado.

    :param number: Un número entero.
    :return: Un UUID generado a partir del número.
    """
    # Convertir el número a una cadena
    number_str = str(number)
    
    # Generar un UUID a partir del espacio de nombres y la cadena del número
    generated_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, number_str)
    
    return str(generated_uuid)


@app.get("/uuid/{number}")
async def get_uuid_from_number(number: int) -> dict:
    """
    Endpoint que recibe un número y devuelve un UUID generado a partir de ese número.
    
    :param number: Un número entero.
    :return: Un diccionario con el UUID generado.
    """
    generated_uuid = generate_uuid_from_number(number)
    return {"uuid": generated_uuid, "valid_period": "24 hours"}




app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
