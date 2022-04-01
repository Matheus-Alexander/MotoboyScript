# ZAX - Motoboy Script
For this project's documentation, access https://matheus-alexander.github.io/ZAX_MotoboyScript/.

# Usage
Clone the repository or download, extract and ```cd``` into the lastest release, and run:
```python main.py```

main.py accepts a comma-separated list of int or a single int as a filter for the final generated Motoboys report.

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