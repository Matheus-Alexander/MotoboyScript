from math import ceil
from controllers.assignment_controller import assign_orders

class DataProcessing:
    def __init__(self, motoboys_list, lojas_list, pedidos_list):
        self.lojas_list = lojas_list
        self.pedidos_list = pedidos_list
        self.motoboys_list = motoboys_list

    def get_loja_comission_by_loja_id(self, id_loja):
        """
        Get a Loja.comission value from a Loja.id value.

        Parameters
        ----------
        id_loja : int
            The ID of the desired Loja.

        Returns
        -------
        int
            The Loja.comission value of the specific Loja.id value.
        """
        loja_comission = [loja.comission for loja in self.lojas_list if loja.id == id_loja]
        if loja_comission:
            return loja_comission[0]
        else:
            raise ValueError(f'ID Loja {id_loja} not found.')

    def distribute_pedidos(self, motoboys_list, pedidos_list):
        """
        Separates the Loja.id values that are related to Motoboy which have an exclusive store,
        calculates a desired amount of orders per Motoboy based on the number of Motoboys and
        Pedidos and calls assignment_controller.assign_orders for each Motoboy.

        Parameters
        ----------
        motoboys_list : list[Motoboy]
            A list of instanced Motoboy classes.
        pedidos_list : list[Motoboy]
            A list of instanced Pedidos classes.
        """
        [id_lojas_com_motoboy_exclusivo] = [
            motoboy.exclusive_stores for motoboy in motoboys_list 
            if motoboy.exclusive_stores
        ]

        avg_orders_per_motoboy = ceil(len(pedidos_list) / len(motoboys_list))
        
        for motoboy in motoboys_list:
            assign_orders(motoboy, pedidos_list, id_lojas_com_motoboy_exclusivo, avg_orders_per_motoboy)

    def calculate_motoboy_profit(self):
        """
        Calculate and assign Motoboy.profit values for all instanced values in self.motoboys_list,
        based on (Loja.comission * Pedido.value) + Motoboy.fare.
        """
        for motoboy in self.motoboys_list:
            motoboy_assigned_pedidos_list = [
                pedido for pedido in self.pedidos_list if pedido.id in motoboy.assigned_orders
            ]

            for assigned_pedido in motoboy_assigned_pedidos_list:
                loja_comission = self.get_loja_comission_by_loja_id(assigned_pedido.id_loja)
                motoboy_profit = (assigned_pedido.price * loja_comission) + motoboy.fare_price

                motoboy.profit += motoboy_profit
