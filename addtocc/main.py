#!/usr/bin/env python
#
# Copyright (C) 2017 104 Corporation
# Copyright (C) 2017 Gea-Suan Lin <gslin@104.com.tw>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator

class AddToCc(Component):
    implements(ITicketManipulator)

    def prepare_ticket(self, req, ticket, fields, actions):
        pass

    def validate_ticket(self, req, ticket):
        if 'preview' in req.args:
            return []

        # When ticket created, ticket._old.get('cc', '') won't return '',
        # which will cause .split() failed.
        cc_old = ticket._old.get('cc')
        if not cc_old:
            cc_old = ''

        cc_list = [cc.strip().lower() for cc in cc_old.split(',')]
        username = req.authname.lower()

        if username not in cc_list:
            ticket['cc'] += ',' + username

        return []
