import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice

def check_custom_condition(self):
    return frappe.db.get_value("Customer", self.customer, "send_whatsapp_notifications")
    
def monkey_patch_notifications():
    SalesInvoice.send_notification = property(check_custom_condition)