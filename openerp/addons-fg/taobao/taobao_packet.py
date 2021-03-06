# -*- coding: utf-8 -*-
##############################################################################
#    Taobao OpenERP Connector
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv, fields
from taobao_base import TaobaoMixin

class taobao_packet(osv.osv, TaobaoMixin):
    _name = "taobao.packet"
    _description = "Taobao Stream Packet"
    _columns = {
            'name': fields.char(u'名字', size=256),
            'taobao_app_key': fields.char('App Key', size=256),
            'data': fields.text(u'Taobao Stream Packet'),
            }
    _order = 'id DESC'

    def cron_flush(self, cr, uid, ids=False, context=None):
        self.unlink(cr, uid, self.search(cr, uid, [], offset = 1000))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
