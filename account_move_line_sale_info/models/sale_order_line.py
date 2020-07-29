# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def name_get(self):
        result = []
        orig_name = dict(super(SaleOrderLine, self).name_get())
        for line in self:
            name = orig_name[line.id]
            if self.env.context.get("so_line_info", False):
                name = "[{}] {} ({})".format(line.order_id.name, name, line.order_id.state)
            result.append((line.id, name))
        return result
