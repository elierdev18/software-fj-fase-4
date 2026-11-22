from excepciones import ClienteInvalidoError
from utilidades import logger


class Cliente:
    """
    Representa un cliente del sistema Software FJ.
    """

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        telefono
    ):
        self._identificacion = self._validar_identificacion(
            identificacion
        )

        self._nombre = self._validar_nombre(
            nombre
        )

        self._correo = self._validar_correo(
            correo
        )

        self._telefono = self._validar_telefono(
            telefono
        )

        logger.info(
            f"Client created successfully: {self._nombre}"
        )

    def _validar_identificacion(
        self,
        identificacion
    ):
        """
        Valida la identificación del cliente.
        """

        try:

            numero = int(
                identificacion
            )

        except ValueError as error_original:

            logger.error(
                f"Invalid client identification: {identificacion}"
            )

            raise ClienteInvalidoError(
                "The identification must be numeric."
            ) from error_original

        if numero <= 0:

            logger.error(
                f"Identification must be greater than zero: {identificacion}"
            )

            raise ClienteInvalidoError(
                "The identification must be greater than zero."
            )

        return str(numero)

    def _validar_nombre(
        self,
        nombre
    ):
        """
        Valida el nombre del cliente.
        """

        if len(
            nombre.strip()
        ) < 3:

            logger.error(
                f"Invalid client name: {nombre}"
            )

            raise ClienteInvalidoError(
                "The name must contain at least 3 characters."
            )

        return nombre.strip()

    def _validar_correo(
        self,
        correo
    ):
        """
        Valida la dirección de correo.
        """

        if "@" not in correo:

            logger.error(
                f"Invalid email address: {correo}"
            )

            raise ClienteInvalidoError(
                "Invalid email address."
            )

        return correo

    def _validar_telefono(
        self,
        telefono
    ):
        """
        Valida el número telefónico.
        """

        if not str(
            telefono
        ).isdigit():

            logger.error(
                f"Invalid phone number: {telefono}"
            )

            raise ClienteInvalidoError(
                "The phone number must contain only digits."
            )

        return str(
            telefono
        )

    def mostrar_datos(self):
        """
        Devuelve los datos del cliente en formato legible.
        """

        return (
            f"ID: {self._identificacion} | "
            f"Name: {self._nombre} | "
            f"Email: {self._correo} | "
            f"Phone: {self._telefono}"
        )

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono