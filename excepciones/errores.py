class SoftwareFJError(Exception):
    """Clase base para las excepciones propias del sistema Software FJ."""

    pass


class ClienteInvalidoError(SoftwareFJError):
    """Se genera cuando los datos de un cliente no son válidos."""

    pass


class ServicioInvalidoError(SoftwareFJError):
    """Se genera cuando los datos de un servicio son incorrectos."""

    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Se genera cuando se intenta reservar un servicio no disponible."""

    pass


class ReservaInvalidaError(SoftwareFJError):
    """Se genera cuando una reserva contiene datos inválidos."""

    pass


class OperacionNoPermitidaError(SoftwareFJError):
    """Se genera cuando el estado actual impide realizar una operación."""

    pass