from odoo import models, fields


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    partner_delivery_id = fields.Many2one(comodel_name ="res.partner", string='Entrega')
