from controllers.utilities_controller import get_loja_comission_by_loja_id

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

def display_motoboys_profit(lojas_list, motoboys_list, motoboy_ids=None):
    filtered_motoboys_list = [
        motoboy for motoboy in motoboys_list if not motoboy_ids or motoboy.id in motoboy_ids
    ]

    for motoboy in filtered_motoboys_list:
        loja_ids = get_loja_comission_by_loja_id(lojas_list, motoboy.assigned_orders)
        generate_report(loja_ids)