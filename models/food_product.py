from odoo import fields, models


class FoodProduct(models.Model):
    _inherit = "product.template"

    plu_code = fields.Integer(string="Plu code", required=False)
    ingredients = fields.Text(help="Beschrijving van de ingredienten.")
