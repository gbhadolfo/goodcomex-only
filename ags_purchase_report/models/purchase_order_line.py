from odoo import models, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    partner_delivery_id = fields.Many2one(comodel_name ="res.partner", string='Entrega')
    partner_delivery_fantasy_name = fields.Char(related='partner_delivery_id.fantasy_name',string=u'Nombre de fantasía',store=True)
    
    def getProductInfo(self, ProductProductID):
        return self.env['product.product'].browse(ProductProductID)
