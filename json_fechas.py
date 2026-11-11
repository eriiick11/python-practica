import asyncio
from asyncio.tasks import gather
import json
from datetime import datetime
from json.decoder import JSONDecodeError
import logging
from time import sleep


class DatosInvalidosError(Exception):
    pass

def nombres_por_fecha(texto_json: str) -> list[str]:
    try:
        data = json.loads(texto_json)
    except json.JSONDecodeError as e:
        raise DatosInvalidosError from e

    ordenados = sorted(data, key=lambda d: datetime.fromisoformat(d["fecha"]))

    return  [n["nombre"] for n in ordenados]



def ordenar_por_ultima_letra(palabras: list[str]) -> list[str]:
    return sorted(palabras, key=lambda p: p[-1])

def mas_caros(productos: list[dict]) -> list[str]:
    prods = sorted(productos, key=lambda p: p["precio"], reverse=True)
    return [p["nombre"] for p in prods]

def nombres_por_edad(texto_json: str) -> list[str]:
    try:
        data = json.loads(texto_json)
    except json.JSONDecodeError as e:
        raise DatosInvalidosError from e

    ordenado = sorted(data, key=lambda d: d["edad"], reverse=True)
    return [d["nombre"] for d in ordenado]





def leer_edad(texto: str) -> int:
    try:
        return int(texto)
    except ValueError as e:
        raise DatosInvalidosError("La edad debe ser un número") from e

def procesar_edades(textos: list[str]) -> list[int]:
    resultados = []
    
    for t in textos:
        try:
            n = leer_edad(t)
        except DatosInvalidosError:
            logging.warning("Fallo el texto %s", t)
        else:
            resultados.append(n)


    logging.info("%s edades validas", len(resultados))   
    return resultados 

def contar_palabras(palabras: list[str]) -> dict[str, int]:
    conteo = {}
    for palabra in palabras:
        if palabra not in conteo:
            conteo[palabra] = 0
        conteo[palabra] += 1
    return conteo

import asyncio
import time

async def descargar(nombre: str, segundos: float) -> str:
    print(f"inicio {nombre}")
    await asyncio.sleep(segundos)
    print(f"fin {nombre}")
    return f"{nombre} descargado"

async def main_secuencial() -> list[str]:
    res1 = await descargar("a", 1)
    res2 = await descargar("b", 2)
    res3 = await descargar("c", 3)

    return [res1, res2, res3]

async def main_concurrent() -> tuple[str, str, str]:
    resultado = await asyncio.gather(descargar("a", 1), descargar("b", 2), descargar("c", 3))
    return resultado 

def prueba() -> int:
    return int