"""
The Generate file takes input from the GUI and creates the PDF.
"""

# import python libraries
import os
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice, CorrectingInvoice

# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def generate_invoice(client_name, client_address, client_zipcode, client_city, client_country, client_vatid,
                    supplier_name, supplier_address, supplier_zipcode, supplier_city, supplier_country,
                    supplier_bank_account, supplier_vatid, number_of_items, price, product_description, tax_perc, number, po_number,
                    coding_string, invoice_creator, filename, filefolder, invoice_type, invoice_date, currency, use_tax, original_invoice,
                     reason):
    """function to generate pdf invoice"""
    filestring = filefolder + '/' + filename + '.PDF'
    os.environ["INVOICE_LANG"] = "nl"
    client = Client(client_name, address=client_address, zip_code=client_zipcode, city=client_city,
                    country=client_country, vat_id=client_vatid)
    provider = Provider(supplier_name, address=supplier_address, zip_code=supplier_zipcode, city=supplier_city,
                        country=supplier_country, bank_account=supplier_bank_account, vat_id=supplier_vatid)
    creator = Creator(invoice_creator)
    invoice = Invoice(client, provider, creator)
    #invoice.add_item(Item(count=1, price="23.87", description="Pickwick Thee top 10", tax="21"))
    #invoice.add_item(Item(count=20, price="8.43", description="Kruimellade tbv brobankrat", tax="12"))
    invoice.add_item(Item(count=number_of_items, price=price, description=product_description, tax=tax_perc))
    invoice.currency = currency
    invoice.number = number
    invoice.purchase_order = po_number
    invoice.coding_string = coding_string
    invoice.taxable_date = invoice_date
    invoice.date = invoice_date
    invoice.generate_breakdown_vat()
    invoice.use_tax = use_tax

    # condition to determine invoice type
    if invoice_type == 'Normal':
        docu = SimpleInvoice(invoice)
    elif invoice_type == 'Credit':
        docu = CorrectingInvoice(invoice)
        invoice.original = original_invoice
        invoice.reason = reason

    docu.gen(filestring)
    #docu.gen(filestring, generate_qr_code=False)  # you can put QR code by setting the #qr_code parameter to ???True???
