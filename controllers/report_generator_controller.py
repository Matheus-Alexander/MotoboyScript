from controllers.utilities_controller import get_loja_ids_by_pedido_ids

def generate_report(motoboy, loja_ids):
    """
    Prints out a report of relevant values from Motoboy class.

    Parameters
    ----------
    motoboy : Motoboy
        an instantiated Motoboy class.
    loja_ids : list[int]
        a list of Loja.loja_ids related to Pedido.id_loja for each Pedido assigned to 
        Motoboy.assigned_orders
    """
    formatted_pedido_ids = ", ".join([str(id) for id in motoboy.assigned_orders])
    loja_ids_formatted = ", ".join([str(num) for num in loja_ids])

    print(f"Motoboy {motoboy.id}:")

    formatted_pedido_ids = ", ".join([str(id) for id in motoboy.assigned_orders])
    print(f"Terá {len(motoboy.assigned_orders)} pedidos.")
    print(f"Ele entregará o(s) pedido(s) {formatted_pedido_ids}.")
    print(f"O motoboy será pago R${motoboy.profit:.2f}")

    loja_ids_formatted = ", ".join([str(num) for num in loja_ids])
    print(f"Os pedidos serão da(s) loja(s) {loja_ids_formatted}.\n")

def display_motoboys_profit(motoboys_list, pedidos_list, lojas_list, motoboy_ids=None):
    """
    Fetches necessary data for each Motoboy in motoboys_list to be correctly displayed in generate_report().
    Calls generate_report() with the necessary parameters.

    Parameters
    ----------
    motoboys_list : list[Motoboy]
        a list of instantiated Motoboy classes.
    pedidos_list : list[Pedido]
        a list of instantiated Pedido classes.
    lojas_list : list[Loja]
        a list of instantiated Loja classes.
    motoboy_ids : list[int] (optional)
        an optional value receiving a list of Motoboy.id values to be displayed in the generated report.
    """
    for motoboy in motoboys_list:
        loja_ids = get_loja_ids_by_pedido_ids(pedidos_list, lojas_list, motoboy.assigned_orders)
        generate_report(motoboy, loja_ids)
    