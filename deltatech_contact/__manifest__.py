# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
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
{
    "name": "Deltatech Contacts",
    'version': '10.0.1.3.0',
    "author": "Dorin Hongu",
    "website": "www.terrabit.ro",
    "description": """

Functionalitati:
 - Adaugare campuri suplimentare in datele de contact: birthdate, CNP,  nr carte de identitate

   
    """,

    "category": "Generic Modules/Base",
    "depends": ["base"],

    "data": ['views/res_partner_view.xml',
             'security/partner_security.xml',
             'security/ir.model.access.csv'],

    "active": False,
    "installable": True,
}



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
