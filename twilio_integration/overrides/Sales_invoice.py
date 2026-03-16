import frappe
from importlib import import_module
from frappe.model.base_document import get_controller


def check_custom_condition(self):
    return frappe.db.get_value("Customer", self.customer, "send_whatsapp_notifications")
    
def monkey_patch_notifications():
    SalesInvoice = get_controller("Sales Invoice")
    SalesInvoice.send_notification = property(check_custom_condition)
