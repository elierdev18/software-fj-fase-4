import logging
from pathlib import Path


def configurar_logger():
    """Configura y devuelve el logger principal de Software FJ."""

    # Determina la carpeta principal del proyecto.
    directorio_proyecto = Path(__file__).resolve().parent.parent

    # Define la carpeta donde se almacenará el archivo de eventos.
    directorio_logs = directorio_proyecto / "logs"

    # Crea la carpeta logs si todavía no existe.
    directorio_logs.mkdir(exist_ok=True)

    # Define la ubicación del archivo de log.
    archivo_log = directorio_logs / "software_fj.log"

    # Obtiene un logger identificado con el nombre del proyecto.
    logger = logging.getLogger("software_fj")

    # Establece el nivel mínimo de registros.
    logger.setLevel(logging.DEBUG)

    # Evita agregar manejadores repetidos cada vez que se importa.
    if not logger.handlers:
        manejador_archivo = logging.FileHandler(
            archivo_log,
            encoding="utf-8"
        )

        manejador_archivo.setLevel(logging.DEBUG)

        formato = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        manejador_archivo.setFormatter(formato)
        logger.addHandler(manejador_archivo)

    return logger


logger = configurar_logger()