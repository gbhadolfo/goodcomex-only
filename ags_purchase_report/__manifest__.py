{
    'name' : 'Purchase Order by Customer',
    'version' : '1.0',
    'author' : 'Adolfo Arbach',
    'description' : """
    Este modulo incorpora en lineas en la orden de compra el campo cliente, para luego imprimir en el reporte de orden de compras con clientes por producto
    """,
    'depends' : ['purchase'],
    'data' : ['views/purchase_order_view.xml'],
    'installable' : True,
    'application' : False,
}