import sys
from math import ceil
import data.dict_data as dados
from classes.motoboy_class import motoboy
from classes.pedidos_class import pedido
from classes.lojas_class import loja

# Class Initialization Functions
def initialize_motoboys_from_data(motoboys_data):
    return [
        motoboy(
            motoboy_data.get("id"), 
            motoboy_data.get("exclusive_stores"), 
            motoboy_data.get("fare_price")
        ) for motoboy_data in motoboys_data
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

def initialize_class_data(data = dados):
    motoboys_data_list = data.motoboys
    lojas_data_list = data.lojas
    pedidos_data_list = data.pedidos
    motoboys_list = initialize_motoboys_from_data(motoboys_data_list)
    lojas_list = initialize_lojas_from_data(lojas_data_list)
    pedidos_list = initialize_pedidos_from_data(pedidos_data_list)

    return motoboys_list, lojas_list, pedidos_list

# Utility Functions
def get_loja_comission_by_loja_id(lojas_list, id_loja):
    loja_comission = [loja.comission for loja in lojas_list if loja.id == id_loja]
    if loja_comission:
        return loja_comission[0]
    else:
        raise ValueError('ID Loja {id} not found.'.format(id=id_loja))

def get_loja_ids_by_pedido_ids(lojas_list, pedidos_list, pedido_ids):
    pedido_ids = [pedido.id_loja for pedido in pedidos_list if pedido.id in pedido_ids]
    loja_ids = [loja.id for loja in lojas_list if loja.id in pedido_ids]

    return loja_ids

# Data Processing Functions
def distribute_pedidos(motoboys_list, pedidos_list):
    [id_lojas_com_motoboy_exclusivo] = [
        motoboy.exclusive_stores for motoboy in motoboys_list 
        if motoboy.exclusive_stores
    ]

    avg_orders_per_motoboy = ceil(len(pedidos_list) / len(motoboys_list))
    
    for motoboy in motoboys_list:
        motoboy.assign_orders(pedidos_list, id_lojas_com_motoboy_exclusivo, avg_orders_per_motoboy)

def calculate_motoboy_profit(motoboys_list, lojas_list, pedidos_list):
    for motoboy in motoboys_list:
        motoboy_assigned_pedidos_list = [
            pedido for pedido in pedidos_list if pedido.id in motoboy.assigned_orders
        ]

        for assigned_pedido in motoboy_assigned_pedidos_list:
            loja_comission = get_loja_comission_by_loja_id(lojas_list, assigned_pedido.id_loja)
            motoboy_profit = (assigned_pedido.price * loja_comission) + motoboy.fare_price

            motoboy.profit += motoboy_profit

def display_motoboys_profit(motoboys_list, motoboy_ids=None):
    filtered_motoboys_list = [
        motoboy for motoboy in motoboys_list if not motoboy_ids or motoboy.id in motoboy_ids
    ]
    for motoboy in filtered_motoboys_list:
        loja_ids = get_loja_ids_by_pedido_ids(lojas_list, pedidos_list, motoboy.assigned_orders)
        motoboy.print_motoboy_data(loja_ids)


if __name__ == "__main__":
    motoboy_ids = None
    if len(sys.argv) > 1:
        motoboy_ids = sys.argv[1].split(",")
        motoboy_ids = list(map(int, motoboy_ids))
        
    motoboys_list, lojas_list, pedidos_list = initialize_class_data()
        
    distribute_pedidos(motoboys_list, pedidos_list)
    calculate_motoboy_profit(motoboys_list, lojas_list, pedidos_list)
    display_motoboys_profit(motoboys_list, motoboy_ids)
