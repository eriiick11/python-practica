import asyncio
import time

async def cocinar(plato: str, segundos: int) -> None:
    print(f"empiezo {plato}")
    await asyncio.sleep(segundos)      # aquí "espera" el plato
    print(f"{plato} listo")

async def uno_tras_otro() -> None:
    await cocinar("arroz", 3)
    await cocinar("huevo", 2)

async def a_la_vez() -> None:
    await asyncio.gather(cocinar("arroz", 3), cocinar("huevo", 2))

for nombre, funcion in [("uno tras otro", uno_tras_otro), ("a la vez", a_la_vez)]:
    inicio = time.perf_counter()
    asyncio.run(funcion())
    print(f"{nombre}: {time.perf_counter() - inicio:.0f}s\n")