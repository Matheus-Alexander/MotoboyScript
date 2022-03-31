import sys
import data.dict_data as dados
from classes.motoboy_class import motoboy
from classes.pedidos_class import pedido
from classes.lojas_class import loja

def initialize_motoboys_from_data(motoboys_data, selected_motoboy_ids = None):
    return [
        motoboy(
            motoboy_data.get("id"), 
            motoboy_data.get("exclusive_stores"), 
            motoboy_data.get("fare_price")
        ) for motoboy_data in motoboys_data
          if selected_motoboy_ids and motoboy_data.get("id") in selected_motoboy_ids
          or not selected_motoboy_ids
    ]

def initialize_lojas_from_data(lojas_data):
    return [
        loja(
            loja_data.get("id"), 
            loja_data.get("comission")
        ) for loja_data in lojas_data
    ]

def initialize_pedidos_from_data(pedidos_data):
    return [
        pedido(
            pedido_data.get("id"), 
            pedido_data.get("price"), 
            pedido_data.get("id_loja")
        ) for pedido_data in pedidos_data
    ]

def initialize_class_data_by_motoboy_ids(motoboy_ids = None, data = dados):
    motoboys_data_list = data.motoboys
    lojas_data_list = data.lojas
    pedidos_data_list = data.pedidos
    motoboys_list = initialize_motoboys_from_data(motoboys_data_list, motoboy_ids)
    lojas_list = initialize_lojas_from_data(lojas_data_list)
    pedidos_list = initialize_pedidos_from_data(pedidos_data_list)

    return motoboys_list, lojas_list, pedidos_list

def distribute_pedidos(motoboys_list, pedidos_list):
    dict_id_motoboy_and_id_lojas_exclusiva = [
        {
            "id_motoboy": motoboy.id,
            "id_lojas_exclusiva": motoboy.exclusive_stores
        } for motoboy in motoboys_list 
        if motoboy.exclusive_stores
    ]

    assigned_orders_ids = []

    for pedido in pedidos_list:
        for motoboy in motoboys_list:
            motoboy.assigned_orders.append(pedido.id)
            assigned_orders_ids.append(pedido.id)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        motoboy_ids = sys.argv[1].split(",")
        motoboy_ids = list(map(int, motoboy_ids))
        motoboys_list, lojas_list, pedidos_list = initialize_class_data_by_motoboy_ids(
            motoboy_ids
        )
    else:
        motoboys_list, lojas_list, pedidos_list = initialize_class_data_by_motoboy_ids()
        distribute_pedidos(motoboys_list, pedidos_list)
    