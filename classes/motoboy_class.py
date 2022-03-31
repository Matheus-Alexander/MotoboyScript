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

    def print_motoboy_data(self, loja_ids):
            print("Motoboy {id_motoboy}:".format(id_motoboy=self.id))

            formatted_pedido_ids = ", ".join([str(id) for id in self.assigned_orders])
            print("Terá {qty_pedidos} pedidos.".format(qty_pedidos=len(self.assigned_orders)))
            print("Ele entregará o(s) pedido(s) {display_pedido_ids}.".format(display_pedido_ids=formatted_pedido_ids))
            print("O motoboy será pago R${profit:.2f}".format(profit=self.profit))

            loja_ids_formatted = ", ".join([str(num) for num in loja_ids])
            print("Os pedidos serão da(s) loja(s) {display_loja_ids}.\n".format(display_loja_ids=loja_ids_formatted))