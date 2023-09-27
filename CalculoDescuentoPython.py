def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en una compra en función del monto total y el porcentaje de descuento.

    Args:
        monto_total: El monto total de la compra.
        porcentaje_descuento: El porcentaje de descuento.

    Returns:
        El monto del descuento.
    """

    return monto_total * porcentaje_descuento / 100

def main():
    # Llamada a la función calcular_descuento con el monto total de la compra y el porcentaje de descuento por defecto.
    monto_total = 1000
    porcentaje_descuento = 10
    monto_descuento = calcular_descuento(monto_total, porcentaje_descuento)
    monto_final = monto_total - monto_descuento
    print("El monto del descuento es de $", monto_descuento)
    print("El monto final a pagar es de $", monto_final)

    # Llamada a la función calcular_descuento con el monto total de la compra y un porcentaje de descuento personalizado.
    monto_total = 2000
    porcentaje_descuento = 20
    monto_descuento = calcular_descuento(monto_total, porcentaje_descuento)
    monto_final = monto_total - monto_descuento
    print("El monto del descuento es de $", monto_descuento)
    print("El monto final a pagar es de $", monto_final)

if __name__ == "__main__":
    main()

