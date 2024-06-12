import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_sales_order_via_rest_api(data):
    try:
        data = frappe.parse_json(data)
        sales_order = frappe.get_doc({
            "doctype": "Sales Order",
            "customer": data.get("customer"),
            "items": [
                {
                    "item_code": data.get("item_code"),
                    # "description": data.get("description"),
                    "rate": data.get("rate"),
                    "qty": data.get("qty"),
                    "delivery_date":data.get("delivery_date")
                }
            ]
        })
        sales_order.insert(ignore_permissions=True)

        return {"status": "success", "message": _("Sales Order created successfully")}
    except Exception as e:
        frappe.log_error(e)
        print("Error------->",e)
        return {"status": "error", "message": _("Failed to create Sales Order")}
