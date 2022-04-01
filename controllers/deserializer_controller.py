from classes.motoboy_class import Motoboy
from classes.pedidos_class import Pedido
from classes.lojas_class import Loja
import data.dict_data as dados

def deserialize_motoboys_from_data(motoboys_data):
    """
    Deserializes a list variable containing dicts with values "id", "exclusive_stores" and "fare_price",
    instantiating a class Motoboy for each value.

    Parameters
    ----------
    motoboys_data : list[dict]
        dict should contain 
        { 
            "id": int,
            "exclusive_stores": list[int],
            "fare_price": float
        }
    Returns
    -------
    list[Motoboy]
        A list of instantiated Motoboy classes.
    """
    return [
        Motoboy(
            motoboy_data.get("id"), 
            motoboy_data.get("exclusive_stores"), 
            motoboy_data.get("fare_price"),
            []
        ) for motoboy_data in motoboys_data
    ]

def deserialize_lojas_from_data(lojas_data):
    """
    Deserializes a list variable containing dicts with values "id", and "comission",
    instantiating a class Loja for each value.

    Parameters
    ----------
    lojas_data : list[dict]
        dict should contain 
        { 
            "id": int,
            "comission": float
        }
    Returns
    -------
    list[Loja]
        A list of instantiated Motoboy classes.
    """
    return [
        Loja(
            loja_data.get("id"), 
            loja_data.get("comission")
        ) for loja_data in lojas_data
    ]

def deserialize_pedidos_from_data(pedidos_data):
    """
    Deserializes a list variable containing dicts with values "id", "id_loja", and "price",
    instantiating a class Pedido for each value.

    Parameters
    ----------
    pedidos_data : list[dict]
        dict should contain 
        { 
            "id": int,
            "id_loja": int,
            "price": float
        }
    Returns
    -------
    list[Pedido]
        A list of instantiated Motoboy classes.
    """
    return [
        Pedido(
            pedido_data.get("id"), 
            pedido_data.get("id_loja"),
            pedido_data.get("price")
        ) for pedido_data in pedidos_data
    ]

def deserialize_class_data(data = dados) -> tuple:
    """
    Deserializes a tuple of list[dict] containing data for Motoboy, Pedido, and Loja values
    calling each class' deserialization method.

    Parameters
    ----------
    data : tuple(list[dict], list[dict], list[dict])
        First list[dict] should contain a list of dict, with each dict containing values { 
            "id": int,
            "exclusive_stores": list[int],
            "fare_price": float
        }. These will be assigned to Motoboy classes.
        Second list[dict] should contain a list of dict, with each dict containing values { 
            "id": int,
            "comission": float
        }. These will be assigned to Loja classes.
        Third list[dict] should contain a list of dict, with each dict containing values { 
            "id": int,
            "id_loja": int,
            "price": float
        }. These will be assigned to Pedido classes.
    Returns
    -------
    tuple(list[Motoboy], list[Loja], list[Pedido])
        A tuple containing a list of instantiated Motoboy classes, a list of instantiated Loja classes,
        and a list of instantiated Pedido classes.
    """
    motoboys_data_list = data.motoboys
    lojas_data_list = data.lojas
    pedidos_data_list = data.pedidos
    motoboys_list = deserialize_motoboys_from_data(motoboys_data_list)
    lojas_list = deserialize_lojas_from_data(lojas_data_list)
    pedidos_list = deserialize_pedidos_from_data(pedidos_data_list)

    return motoboys_list, lojas_list, pedidos_list
