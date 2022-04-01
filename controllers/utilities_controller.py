def get_loja_comission_by_loja_id(lojas_list, id_loja):
    loja_comission = [loja.comission for loja in lojas_list if loja.id == id_loja]
    if loja_comission:
        return loja_comission[0]
    else:
        raise ValueError('ID Loja {id} not found.'.format(id=id_loja))