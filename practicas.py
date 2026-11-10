""" def ya_vi_duplicado(nums: list[int]) -> bool:
    vistos = set()
    for n in nums:
        if n in vistos:
            return True
        vistos.add(n)
    return False

         
def ya_vi_duplicado_v2(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums) 


def segundo_mayor(nums:list[int]) -> int:
    unicos = set(nums)
    if len(unicos) < 2:
        raise ValueError("La lista debe tener menos de 2 elementos")
    ordenados = sorted(unicos, reverse=True)
    return ordenados[1]

     """
""" 
def lineas_con_error(ruta:str):
    with open(ruta) as archivo:
        for linea in archivo:
            if "ERROR" in linea:
                yield linea """

def hacer_contador():
    i = 0
    def otra_funcion():
        nonlocal i
        i += 1
        return i
    
    return otra_funcion


from ast import Return, Try
from dataclasses import dataclass
from enum import nonmember
from multiprocessing import Value
from nt import getcwd

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio es menor a cero")

    def __init__(self) -> None:
        nombre = self.nombre
        precio = self.precio
        cantidad = self.cantidad
        total = self.preio * self.cantidad

    @property 
    def total(self):
        total = self.precio * self.cantidad
        return total 

def longitudes(palabras: list[str]) ->  list[int]:
    return [len(p) for p in palabras]

def solo_largas(palabras: list[str], minimo: int) -> list[str]:
    return [p for p in palabras if len(p) >= minimo]

def indexar_por_inicial(palabras: list[str]) -> dict[str, int]:
    return {palabra[0]:len(palabra)  for palabra in palabras}

def longitudes_unicas(palabras: list[str]) -> set[int]:
    return {len(palabra) for palabra in palabras}

def cuadrados_pares(nums: list[int]) -> list[int]:
    return [(n*n) for n in nums if n % 2 == 0]

def promedio(*numeros: float) -> float:
    if not numeros:
        raise ValueError("Debe haber numeros")
    return  sum(numeros) / len(numeros)
    
def resumen(nums: list[int]) -> tuple[int, int, float]:    
    return min(nums),  max(nums), (sum(nums) / len(nums))

def etiquetar(texto, **opciones):
    if opciones.get("mayusculas", False):
        return texto.upper()
    return texto

def a_entero(texto: str) -> int | None:
    try:
        return int(texto)
    except ValueError:
        return None

def dividir(a: float, b: float) -> float:
    try:
        c = a/b
        return c
    except ZeroDivisionError as e:
        raise ValueError("el divisor no puede ser 0")


def agregar(x, lista=[]):
    if lista is None:
        lista = []
    lista.append(x)
    return lista

def normalizar(texto: str) -> str:
    return texto.lower().strip()

def contar_letras(palabra: str) -> dict[str, int]:
    conteo = {}
    for l in palabra:
        if l not in conteo:
            conteo[l] = 0
        conteo[l] += 1
    return conteo

def contar_lineas_con(ruta: str, palabra: str) -> int:
    contador = 0
    with open(ruta, encoding="utf-8") as f:
        for l in f:
            if palabra in l:
                contador += 1
    return contador

def hacer_saludador(saludo: str):
    def saludar(nombre: str):
        return saludo + nombre
    return saludar 

def hacer_contador():
    conteo = 0
    def contador():
        nonlocal conteo
        conteo += 1
        return conteo
    return contador



 ############# DECORADORESSSSS ################
from functools import wraps 

def anunciar(f):
    @wraps(f)  ## para no borrar nombres de las funciones 
    def nueva(*args, **kwargs):
        print("empezando")
        resultado = f(*args, **kwargs)
        print("terminado")
        return resultado


    return nueva

@anunciar
def sumar(a, b):
    return a + b

print(sumar.__name__)

#---------------------------------------------------

import time
from functools import wraps

def cronometrar(f):
    @wraps(f)
    def nueva(*args, **kargs):
        hora = time.perf_counter()
        resultado = f(*args, **kargs)
        new_hora = time.perf_counter() - hora 
        print(f"tardó {new_hora:.2f} segundos")
        return resultado
    return nueva 

@cronometrar
def lenta():
    time.sleep(1)
    return "listo"

# print(lenta())            # tardó 1.00 segundos / listo

#-------------------------------
import os 
from contextlib import contextmanager

@contextmanager
def cambiar_dir(ruta: str):
    ruta_actual = os.getcwd()
    os.chdir(ruta)
    try:
        yield 
    finally:
        os.chdir(ruta_actual)

#+================
@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    @property
    def total(self) -> float:
        return self.precio * self.cantidad

    def __post_init__(self):
        if self.precio<0:
            raise ValueError("El precio no puede ser 0")
