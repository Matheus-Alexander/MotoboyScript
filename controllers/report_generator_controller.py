from controllers.utilities_controller import get_loja_ids_by_pedido_ids

def generate_report(motoboy, loja_ids):
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
    filtered_motoboys_list = [
        motoboy for motoboy in motoboys_list if not motoboy_ids or motoboy.id in motoboy_ids
    ]

    if not filtered_motoboys_list:
        raise ValueError(f"O motoboy {motoboy_ids} não existe.")

    for motoboy in filtered_motoboys_list:
        loja_ids = get_loja_ids_by_pedido_ids(pedidos_list, lojas_list, motoboy.assigned_orders)
        generate_report(motoboy, loja_ids)