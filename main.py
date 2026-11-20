from excepciones import ClienteInvalidoError


def probar_excepcion_cliente():
    """Demuestra el uso básico de una excepción personalizada."""

    try:
        raise ClienteInvalidoError(
            "The client email is invalid."
        )
    except ClienteInvalidoError as error:
        print(f"Controlled error: {error}")


if __name__ == "__main__":
    probar_excepcion_cliente()
    print("The program continues running.")