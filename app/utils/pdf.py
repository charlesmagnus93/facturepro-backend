import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))


def generate_invoice_pdf(invoice):
    template = env.get_template("invoice.html")

    owner = invoice.owner
    client = invoice.client

    date_str = (
        invoice.created_at.strftime("%d/%m/%Y")
        if invoice.created_at
        else datetime.utcnow().strftime("%d/%m/%Y")
    )

    html_content = template.render(
        company_name=owner.company_name or owner.full_name,
        company_address=owner.company_address or "",
        company_phone=owner.company_phone or "",
        company_email=owner.company_email or "",
        invoice_number=invoice.invoice_number,
        date=date_str,
        status=invoice.status.value if hasattr(invoice.status, "value") else invoice.status,
        client_name=client.name,
        client_address=client.address or "",
        client_phone=client.phone or "",
        client_email=client.email or "",
        items=invoice.items,
        total_amount=invoice.total_amount or 0,
        amount_paid=invoice.amount_paid or 0,
    )

    pdf = HTML(string=html_content).write_pdf()
    return pdf
