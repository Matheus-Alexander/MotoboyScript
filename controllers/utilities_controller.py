def get_loja_ids_by_pedido_ids(pedidos_list, lojas_list, motoboy_pedido_ids):
    pedido_ids = [pedido.id_loja for pedido in pedidos_list if pedido.id in motoboy_pedido_ids]
    loja_ids = [loja.id for loja in lojas_list if loja.id in pedido_ids]

    return loja_ids
