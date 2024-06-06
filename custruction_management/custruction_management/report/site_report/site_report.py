# Copyright (c) 2024, shivansh akshay abhinav and contributors
# For license information, please see license.txt
import frappe

def execute(filters=None):
    columns = [
        {"label": "Site Name", "fieldname": "site_name", "fieldtype": "Data", "width": 150},
        # {"label": "Tasks Overview", "fieldname": "tasks_overview", "fieldtype": "Data", "width": 200},
        {"label": "Start Date", "fieldname": "start_date", "fieldtype": "Date", "width": 100},
        {"label": "Expected End Date", "fieldname": "expected_end_date", "fieldtype": "Date", "width": 150},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120}
    ]
    
    data = []
    data1 = frappe.get_all("Site", filters=filters, fields=["site_name", "start_date", "end_date", "status"])
    for col in data1:
        data.append({
            "site_name": col.site_name,
            # "tasks_overview": col.tasks_overview,
            "start_date": col.start_date,
            "expected_end_date": col.end_date,  
            "status": col.status
        })

    return columns, data
