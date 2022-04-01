def assign_orders(motoboy, pedidos_list, id_lojas_com_motoboy_exclusivo, avg_orders_per_motoboy):
    """
    Validates if received Motoboy has reached avg_orders_per_motoboy pedidos or if it has exclusivity 
    with a Loja, then assigns Pedido from pedidos_list where Pedido.assigned = False, prioritizing
    assigning Pedido from Loja to Motoboy which matches Motoboy.exclusive_stores = Pedido.id_loja.
    Updates Motoboy.assigned_orders with Pedido that passes all checks, and changes Pedido.assigned to
    True.

    Parameters
    ----------
    motoboy : Motoboy
        An instantiated Motoboy class.
    pedidos_list : list[Pedido]
        A list containing instantiated Pedido classes.
    id_lojas_com_motoboy_exclusivo : list[int]
        A list of int containing id_loja based on all instantiated Motoboy.exclusive_stores.
    avg_orders_per_motoboy : int
        The result of the length of all instantiated Motoboy divided by all instantiated Pedido,
        rounded up.
    """
    for pedido in pedidos_list:
        if not motoboy.exclusive_stores and len(motoboy.assigned_orders) >= avg_orders_per_motoboy:
            break
        elif motoboy.exclusive_stores and pedido.id_loja not in motoboy.exclusive_stores:
            continue
        if pedido.id_loja in id_lojas_com_motoboy_exclusivo:
            if not motoboy.exclusive_stores:
                continue
            elif pedido.id_loja in motoboy.exclusive_stores:
                motoboy.assigned_orders.append(pedido.id)
                pedido.change_assigned_value(True)
        if pedido.assigned == False:
            motoboy.assigned_orders.append(pedido.id)
            pedido.change_assigned_value(True)
