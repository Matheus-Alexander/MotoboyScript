from classes.motoboy_class import Motoboy
from classes.pedidos_class import Pedido
from classes.lojas_class import Loja
import data.dict_data as dados

def deserialize_motoboys_from_data(motoboys_data):
    return [
        Motoboy(
            motoboy_data.get("id"), 
            motoboy_data.get("exclusive_stores"), 
            motoboy_data.get("fare_price"),
            []
        ) for motoboy_data in motoboys_data
    ]

def deserialize_lojas_from_data(lojas_data):
    return [
        Loja(
            loja_data.get("id"), 
            loja_data.get("comission")
        ) for loja_data in lojas_data
    ]

def deserialize_pedidos_from_data(pedidos_data):
    return [
        Pedido(
            pedido_data.get("id"), 
            pedido_data.get("id_loja"),
            pedido_data.get("price")
        ) for pedido_data in pedidos_data
    ]

def deserialize_class_data(data = dados) -> tuple:
    motoboys_data_list = data.motoboys
    lojas_data_list = data.lojas
    pedidos_data_list = data.pedidos
    motoboys_list = deserialize_motoboys_from_data(motoboys_data_list)
    lojas_list = deserialize_lojas_from_data(lojas_data_list)
    pedidos_list = deserialize_pedidos_from_data(pedidos_data_list)

    return motoboys_list, lojas_list, pedidos_list
