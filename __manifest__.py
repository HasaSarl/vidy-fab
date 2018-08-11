# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2012 HASA (http://www.hasa.ch) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    "name" : "VIDY-FAB Modification",
    "version" : "2.0",
	"author" : "Alexandre, Hasa",
    "website" : "http://www.hasa.ch",
    "category" : "calendar",
    "license" : "LGPL-3",
    "description": """ """,
    "depends" : ["web", "document", "account", "base", "product", "calendar", "smartcab"],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
		"views/calendar_event_view.xml",
		"views/vidy_assets.xml",
        "views/partner_view.xml"
	],
	'css' : [
			],
	'js' : [
		"static/src/js/datepicker.js"
		],
	'qweb' : [
    ],
    "installable": True
}
