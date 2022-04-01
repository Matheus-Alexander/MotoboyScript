import sys
import controllers.deserializer_controller as data_deserialize
from classes.data_processing_class import DataProcessing

if __name__ == "__main__":
    motoboys_list, lojas_list, pedidos_list = data_deserialize.deserialize_class_data()
    data_processing_class = DataProcessing(motoboys_list, lojas_list, pedidos_list)

    data_processing_class.distribute_pedidos(motoboys_list, pedidos_list)
    data_processing_class.calculate_motoboy_profit()

    if len(sys.argv) > 1:
        motoboy_ids = sys.argv[-1].split(",")
        motoboy_ids = list(map(int, motoboy_ids))
        data_processing_class.display_motoboys_profit(motoboy_ids)
    else:
        data_processing_class.display_motoboys_profit()
