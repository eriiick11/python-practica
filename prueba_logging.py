import logging

logging.basicConfig(
    level=logging.INFO,                                    # muestra INFO y lo más grave
    format="%(asctime)s %(levelname)s: %(message)s",       # hora, nivel y mensaje
)
logger = logging.getLogger(__name__)

def dividir(a: float, b: float) -> float | None:
    logger.info("dividiendo %s entre %s", a, b)
    if b == 0:
        logger.warning("divisor cero, devuelvo None")
        return None
    return a / b

logger.info("programa iniciado")
print(dividir(10, 2))
print(dividir(5, 0))

try:
    int("abc")
except ValueError:
    logger.exception("falló la conversión")     # registra el mensaje y el traceback

logger.debug("este no se ve")                   # DEBUG está por debajo de INFO