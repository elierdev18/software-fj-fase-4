from modelos import Cliente
from excepciones import ClienteInvalidoError


try:

    cliente = Cliente(
        "abc123",
        "Elier",
        "elier@email.com",
        "3001234567"
    )

    print(
        cliente.mostrar_datos()
    )

except ClienteInvalidoError as error:

    print(
        f"Client error: {error}"
    )