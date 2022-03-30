import sys
import data.dict_data as dados
from classes.motoboy_class import motoboy
from classes.pedidos_class import pedidos
from classes.lojas_class import lojas

def initialize_motoboys_from_data(motoboys_data, selected_motoboy_ids):
    return [
        motoboy(
            motoboy_data.get("id"), 
            motoboy_data.get("stores"), 
            motoboy_data.get("fare_price")
        ) for motoboy_data in motoboys_data
          if motoboy_data.get("id") in selected_motoboy_ids
    ]

def initialize_lojas_from_data(lojas_data):
    return [
        lojas(
            loja_data.get("id"), 
            loja_data.get("comission")
        ) for loja_data in lojas_data
    ]

def initialize_pedidos_from_data(pedidos_data):
    return [
        pedidos(
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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        motoboy_ids = sys.argv[1].split(",")
        motoboy_ids = [int(motoboy_id) for motoboy_id in motoboy_ids]
        initialize_class_data_by_motoboy_ids(motoboy_ids)
    else:
        initialize_class_data_by_motoboy_ids()