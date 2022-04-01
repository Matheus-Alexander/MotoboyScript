from math import ceil
from controllers.assignment_controller import assign_orders
from controllers.utilities_controller import get_loja_comission_by_loja_id

class DataProcessing:
    def __init__(self, motoboys_list, lojas_list, pedidos_list):
        self.lojas_list = lojas_list
        self.pedidos_list = pedidos_list
        self.motoboys_list = motoboys_list

    def get_loja_ids_by_pedido_ids(self, motoboy_pedido_ids):
        pedido_ids = [pedido.id_loja for pedido in self.pedidos_list if pedido.id in motoboy_pedido_ids]
        loja_ids = [loja.id for loja in self.lojas_list if loja.id in pedido_ids]

        return loja_ids

    def distribute_pedidos(self, motoboys_list, pedidos_list):
        [id_lojas_com_motoboy_exclusivo] = [
            motoboy.exclusive_stores for motoboy in motoboys_list 
            if motoboy.exclusive_stores
        ]

        avg_orders_per_motoboy = ceil(len(pedidos_list) / len(motoboys_list))
        
        for motoboy in motoboys_list:
            assign_orders(motoboy, motoboys_list, pedidos_list, id_lojas_com_motoboy_exclusivo, avg_orders_per_motoboy)

    def calculate_motoboy_profit(self):
        for motoboy in self.motoboys_list:
            motoboy_assigned_pedidos_list = [
                pedido for pedido in self.pedidos_list if pedido.id in motoboy.assigned_orders
            ]

            for assigned_pedido in motoboy_assigned_pedidos_list:
                loja_comission = get_loja_comission_by_loja_id(self.lojas_list, assigned_pedido.id_loja)
                motoboy_profit = (assigned_pedido.price * loja_comission) + motoboy.fare_price

                motoboy.profit += motoboy_profit

    def generate_report(self, loja_ids):
        for motoboy in self.motoboys_list:
            formatted_pedido_ids = ", ".join([str(id) for id in motoboy.assigned_orders])
            loja_ids_formatted = ", ".join([str(num) for num in loja_ids])

            print("Motoboy {id_motoboy}:".format(id_motoboy=motoboy.id))

            formatted_pedido_ids = ", ".join([str(id) for id in motoboy.assigned_orders])
            print("Terá {qty_pedidos} pedidos.".format(qty_pedidos=len(motoboy.assigned_orders)))
            print("Ele entregará o(s) pedido(s) {display_pedido_ids}.".format(display_pedido_ids=formatted_pedido_ids))
            print("O motoboy será pago R${profit:.2f}".format(profit=motoboy.profit))

            loja_ids_formatted = ", ".join([str(num) for num in loja_ids])
            print("Os pedidos serão da(s) loja(s) {display_loja_ids}.\n".format(display_loja_ids=loja_ids_formatted))

    def display_motoboys_profit(self, motoboy_ids=None):
        filtered_motoboys_list = [
            motoboy for motoboy in self.motoboys_list if not motoboy_ids or motoboy.id in motoboy_ids
        ]

        for motoboy in filtered_motoboys_list:
            loja_ids = self.get_loja_ids_by_pedido_ids(motoboy.assigned_orders)
            self.generate_report(loja_ids)
