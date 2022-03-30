class Motoboy:
    def __init__(self, id, stores, fare_price):
        self.id = id
        self.stores = stores
        self.fare_price = fare_price

class Lojas:
    def __init__(self, id, comission):
        self.id = id
        self.comission = comission

class Pedidos:
    def __init__(self, id, valor, id_loja):
        self.id = id
        self.valor = valor
        self.id_loja = id_loja