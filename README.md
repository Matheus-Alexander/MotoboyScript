# Motoboy Script
For this project's documentation, access https://matheus-alexander.github.io/MotoboyScript/.

# Usage
Clone the repository or download, extract and ```cd``` into the lastest release, and run:
```python main.py```

main.py accepts a comma-separated list of int or a single int as a filter for the final generated Motoboys report.
The default behaviour when no parameters are provided is to list all Motoboys' processed data.

## No Parameters
```
python main.py
```
Returns:
```
Motoboy 1:
Terá 2 pedidos.
Ele entregará o(s) pedido(s) 4, 5.
O motoboy será pago R$9.00
Os pedidos serão da(s) loja(s) 2.

Motoboy 2:
Terá 2 pedidos.
Ele entregará o(s) pedido(s) 6, 7.
O motoboy será pago R$9.00
Os pedidos serão da(s) loja(s) 2.

Motoboy 3:
Terá 2 pedidos.
Ele entregará o(s) pedido(s) 8, 9.
O motoboy será pago R$19.00
Os pedidos serão da(s) loja(s) 3.

Motoboy 4:
Terá 3 pedidos.
Ele entregará o(s) pedido(s) 1, 2, 3.
O motoboy será pago R$13.50
Os pedidos serão da(s) loja(s) 1.

Motoboy 5:
Terá 1 pedidos.
Ele entregará o(s) pedido(s) 10.
O motoboy será pago R$18.00
Os pedidos serão da(s) loja(s) 3.
```
## Single Parameter
```
python main.py 1
```
Returns:
```
Motoboy 1:
Terá 2 pedidos.
Ele entregará o(s) pedido(s) 4, 5.
O motoboy será pago R$9.00
Os pedidos serão da(s) loja(s) 2.
```

## Multiple Parameters
```
python main.py 1,5
```
Returns:
```
Motoboy 1:
Terá 2 pedidos.
Ele entregará o(s) pedido(s) 4, 5.
O motoboy será pago R$9.00
Os pedidos serão da(s) loja(s) 2.

Motoboy 5:
Terá 1 pedidos.
Ele entregará o(s) pedido(s) 10.
O motoboy será pago R$18.00
Os pedidos serão da(s) loja(s) 3.
```
