import sys
import controllers.deserializer_controller as data_deserialize
from classes.data_processing_class import DataProcessing
from controllers.report_generator_controller import display_motoboys_profit

if __name__ == "__main__":
    motoboys_list, lojas_list, pedidos_list = data_deserialize.deserialize_class_data()
    data_processing_class = DataProcessing(motoboys_list, lojas_list, pedidos_list)

    data_processing_class.distribute_pedidos(motoboys_list, pedidos_list)
    data_processing_class.calculate_motoboy_profit()

    if len(sys.argv) > 1:
        motoboy_ids = sys.argv[-1].split(",")
        motoboy_ids = list(map(int, motoboy_ids))

        filtered_motoboys_list = [
            motoboy for motoboy in motoboys_list if not motoboy_ids or motoboy.id in motoboy_ids
        ]

        if not filtered_motoboys_list:
            raise ValueError(f"Nenhum dos motoboys {motoboy_ids} existe.")

        display_motoboys_profit(filtered_motoboys_list, pedidos_list, lojas_list, motoboy_ids)

        existing_motoboy_ids = [filtered_motoboys_list_item.id for filtered_motoboys_list_item in filtered_motoboys_list]
        non_existing_motoboy_ids = list(set(motoboy_ids) - set(existing_motoboy_ids))
        if non_existing_motoboy_ids:
            raise ValueError(f"O(s) motoboy(s) {non_existing_motoboy_ids} não existe(m).")
    else:
        display_motoboys_profit(motoboys_list, pedidos_list, lojas_list)
