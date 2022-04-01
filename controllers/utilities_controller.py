def get_loja_ids_by_pedido_ids(pedidos_list, lojas_list, motoboy_pedido_ids):
    """
    Gets list[Loja.id] by relating Pedido.id_loja to Loja.id values, filtered by
    Pedido.id in Motoboy.assigned_orders.

    Parameters
    ----------
    pedidos_list : list[Pedido]
        a list of instantiated Pedido classes.
    lojas_list : list[Loja]
        a list of instantiated Pedido classes.
    motoboy_pedido_ids : list[int]
        a list of int to be matched to Pedido.id. 
        Expected value to be received comes from Motoboy.assigned_orders.
    Returns
    -------
    list[int]
        a list of int representing Loja.id values related to Pedido.loja_id where 
        Pedido.Id = Motoboy.assigned_orders.
    """
    pedido_ids = [pedido.id_loja for pedido in pedidos_list if pedido.id in motoboy_pedido_ids]
    loja_ids = [loja.id for loja in lojas_list if loja.id in pedido_ids]

    return loja_ids
