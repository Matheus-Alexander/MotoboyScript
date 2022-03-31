class motoboy:
    def __init__(self, id, exclusive_stores, fare_price):
        self.id = id
        self.exclusive_stores = exclusive_stores
        self.fare_price = fare_price
        self.profit = 0.0
        self.assigned_orders = []

    def add_assigned_order(self, pedido):
        self.assigned_orders.append(pedido.id)
        pedido.assigned = True

    def assign_orders(self, pedidos_list, id_lojas_com_motoboy_exclusivo, avg_orders_per_motoboy):
        for pedido in pedidos_list:
            if not self.exclusive_stores and len(self.assigned_orders) >= avg_orders_per_motoboy:
                break
            elif self.exclusive_stores and pedido.id_loja not in self.exclusive_stores:
                continue
            if pedido.id_loja in id_lojas_com_motoboy_exclusivo:
                if not self.exclusive_stores:
                    continue
                elif pedido.id_loja in self.exclusive_stores:
                    self.add_assigned_order(pedido)
            if pedido.assigned == False:
                self.add_assigned_order(pedido)