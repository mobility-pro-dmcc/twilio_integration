# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

from twilio_integration.overrides.sales_invoice import monkey_patch_notifications
monkey_patch_notifications()

