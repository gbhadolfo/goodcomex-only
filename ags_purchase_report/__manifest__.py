{
    'name' : 'Purchase Order by Customer',
    'version' : '1.1',
    'author' : 'Adolfo Arbach',
    'description' : """
    Modulo que Incorpora en lineas en la orden de compra el campo cliente, para luego imprimir en el reporte de orden de compras un cuadro con cantidades por clientes, y agrupa en la vista los productos
    """,
    'depends' : ['purchase','oct_partner_fantasy_name'],
    'data' : ['views/purchase_order_view.xml'],
    'installable' : True,
    'application' : False,
}
