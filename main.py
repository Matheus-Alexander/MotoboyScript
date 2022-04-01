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
        display_motoboys_profit(motoboys_list, pedidos_list, lojas_list, motoboy_ids)
    else:
        display_motoboys_profit(motoboys_list, pedidos_list, lojas_list)
