from odoo import models, fields, api

class CustomDeliveryNote(models.Model):
    _inherit = 'stock.picking'

    delivery_note_number = fields.Char(string='Delivery Note #', readonly=True, copy=False)
    customer_id = fields.Char(related='partner_id.ref', string='Customer ID', store=True)
    despatch_date = fields.Date(string='Despatch Date')
    delivery_method = fields.Char(string='Delivery Method')

    @api.model
    def create(self, vals):
        if vals.get('picking_type_id'):
            picking_type = self.env['stock.picking.type'].browse(vals['picking_type_id'])
            if picking_type.code == 'outgoing':
                vals['delivery_note_number'] = self.env['ir.sequence'].next_by_code('custom.delivery.note')
        return super(CustomDeliveryNote, self).create(vals)

    def write(self, vals):
        if 'picking_type_id' in vals:
            picking_type = self.env['stock.picking.type'].browse(vals['picking_type_id'])
            if picking_type.code == 'outgoing':
                vals['delivery_note_number'] = self.env['ir.sequence'].next_by_code('custom.delivery.note')
        return super(CustomDeliveryNote, self).write(vals)

    def get_move_lines_with_qty(self):
        return [(move, move.product_uom_qty, sum(move.move_line_ids.mapped('quantity'))) for move in self.move_ids_without_package]