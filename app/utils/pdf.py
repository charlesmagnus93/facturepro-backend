from io import BytesIO

from reportlab.lib.pagesizes import A4

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet


def generate_invoice_pdf(invoice):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=A4)

    elements = []

    styles = getSampleStyleSheet()

    title = Paragraph(f"FACTURE {invoice.invoice_number}", styles["Title"])

    elements.append(title)

    elements.append(Spacer(1, 20))

    client = Paragraph(f"Client: {invoice.client.name}", styles["Normal"])

    elements.append(client)

    elements.append(Spacer(1, 20))

    data = [["Description", "Qté", "Prix Unitaire", "Total"]]

    for item in invoice.items:

        data.append(
            [
                item.description,
                str(item.quantity),
                str(item.unit_price),
                str(item.total_price),
            ]
        )

    table = Table(data)

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ]
        )
    )

    elements.append(table)

    elements.append(Spacer(1, 20))

    total = Paragraph(f"Total: {invoice.total_amount} FCFA", styles["Heading2"])

    elements.append(total)

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
