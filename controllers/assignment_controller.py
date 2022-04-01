def assign_orders(motoboy, motoboy_list, pedidos_list, id_lojas_com_motoboy_exclusivo, avg_orders_per_motoboy):
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
