"""
The GUI file creates the GUI and sends the input values to generate.py.
"""
#import necessary packages and python functions

import PySimpleGUI as sg
import datetime
from generate import generate_invoice

# GUI
layout = [
    [sg.Radio('Normal Invoice', 1, enable_events=True, default=True, key='-NORMAL_INVOICE-'), sg.Radio('Credit Nota',1, enable_events=True, key='-CREDIT_NOTA-')],
    [sg.Text('Please enter all necessary invoice data:')],
    [sg.Text(' ')],
    [sg.Text('CUSTOMER DETAILS')],
    [sg.Text('Client name', size =(15, 1)), sg.Input(key='-CLIENT_NAME-')],
    [sg.Text('Address', size =(15, 1)), sg.Input(key='-CLIENT_ADDRESS-')],
    [sg.Text('Zip code', size =(15, 1)), sg.Input(key='-CLIENT_ZIPCODE-')],
    [sg.Text('City', size =(15, 1)), sg.Input(key='-CLIENT_CITY-')],
    [sg.Text('Country', size =(15, 1)), sg.Input(key='-CLIENT_COUNTRY-')],
    [sg.Text('VAT ID (BTW)', size =(15, 1)), sg.Input(key='-CLIENT_VATID-')],
    [sg.Text(' ')],
    [sg.Text('SUPPLIER DETAILS')],
    [sg.Text('Supplier name', size =(15, 1)), sg.Input(key='-SUPPLIER_NAME-')],
    [sg.Text('Address', size=(15, 1)), sg.Input(key='-SUPPLIER_ADDRESS-')],
    [sg.Text('Zip code', size=(15, 1)), sg.Input(key='-SUPPLIER_ZIPCODE-')],
    [sg.Text('City', size=(15, 1)), sg.Input(key='-SUPPLIER_CITY-')],
    [sg.Text('Country', size=(15, 1)), sg.Input(key='-SUPPLIER_COUNTRY-')],
    [sg.Text('VAT ID (BTW)', size=(15, 1)), sg.Input(key='-SUPPLIER_VATID-')],
    [sg.Text('IBAN', size=(15, 1)), sg.Input(key='-SUPPLIER_BANKACCOUNT-')],
    [sg.Text(' ')],
    [sg.Text('INVOICE HEADER DETAILS')],
    [sg.Text('Invoice Date', size =(15, 1)), sg.Input(key='-INVOICE_DATE-', default_text=f"{datetime.datetime.now():%d-%m-%Y}",do_not_clear=False),
     sg.Text('DD-MM-YYYY', size=(15,1))],
    [sg.Text('Invoice number', size =(15, 1)), sg.Input(key='-INVOICE_NUMBER-', do_not_clear=False)],
    [sg.Text('PO number', size=(15, 1)), sg.Input(key='-PO-', do_not_clear=False)],
    [sg.Text('Coding Sring', size=(15, 1)), sg.Input(key='-CODING_STRING-', do_not_clear=False)],
    [sg.Text('Created by', size=(15, 1)), sg.Input(key='-CREATOR-')],
    [sg.Text('Use Tax?', size=(15,1)), sg.Radio('Yes', 2, enable_events=True, default=True, key='-YES_TAX-'), sg.Radio('No',2, enable_events=True, key='-NO_TAX-')],
    [sg.Text(' ')],
    [sg.Text('ONLY FILL IF CREDIT NOTA')],
    [sg.Text('Original Invoice number', size=(15, 1)), sg.Input(key='-ORIGINAL_INVOICE-')],
    [sg.Text('Reason Credit nota', size=(15, 1)), sg.Input(key='-REASON-')],
    [sg.Text(' ')],
    [sg.Text('FACTUUR LINE ITEMS')],
    [sg.Text('Product', size=(15, 1)), sg.Input(key='-PRODUCT_DESCRIPTION-'), sg.Text('# Items', size=(5, 1)), sg.Input(size=(5, 1), key='-COUNT-'),
    sg.Text('Item price', size=(10, 1)), sg.Input(size=(5, 1),key='-ITEM_PRICE-'), sg.Text('VAT %', size=(5, 1)), sg.Input(size=(5,1), key='-TAX-')],
    [sg.Text('Currency', size=(15,1)), sg.Input(key='-CURRENCY-', default_text="€")],
    [sg.Text(' ')],
    [sg.Text('FILE NAME & FOLDER LOCATIION')],
    [sg.Text('File Name', size=(15, 1)), sg.Input(key='-FILENAME-', do_not_clear=False)],
    [sg.Text("Choose a folder: "), sg.Input(key='-FILEFOLDER-'), sg.FolderBrowse()],
    [sg.Button('SUBMIT'), sg.Button('CANCEL')]
]

window = sg.Window('PDF Invoice Creator for VIM', layout)

# pylint: disable=no-else-break
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'CANCEL'):
        break
    elif event == 'SUBMIT':
        v1 = values['-CLIENT_NAME-']
        v2 = values['-CLIENT_ADDRESS-']
        v3 = values['-CLIENT_ZIPCODE-']
        v4 = values['-CLIENT_CITY-']
        v5 = values['-CLIENT_COUNTRY-']
        v6 = values['-CLIENT_VATID-']
        v7 = values['-SUPPLIER_NAME-']
        v8 = values['-SUPPLIER_ADDRESS-']
        v9 = values['-SUPPLIER_ZIPCODE-']
        v10 = values['-SUPPLIER_CITY-']
        v11 = values['-SUPPLIER_COUNTRY-']
        v12 = values['-SUPPLIER_VATID-']
        v13 = values['-SUPPLIER_BANKACCOUNT-']
        v14 = values['-INVOICE_NUMBER-']
        v15 = values['-PO-']
        v30 = values['-CODING_STRING-']
        v16 = values['-PRODUCT_DESCRIPTION-']
        v17 = values['-COUNT-']
        v18 = values['-ITEM_PRICE-']
        v19 = values['-TAX-']
        v20 = values['-CREATOR-']
        v21 = values['-FILENAME-']
        v22 = values['-FILEFOLDER-']
        v26 = values['-CURRENCY-']
        v28 = values['-ORIGINAL_INVOICE-']
        v29 = values['-REASON-']

        #condition to determine invoice type
        if values['-NORMAL_INVOICE-'] == True:
            v23 = 'Normal'
        elif values['-CREDIT_NOTA-'] == True:
            v23 = 'Credit'

        #condition to determine invoice date
        if values['-INVOICE_DATE-'] == "":
            v25 = values['-INVOICE_DATE-']
        else:
            v25 = datetime.datetime.strptime(values['-INVOICE_DATE-'], "%d-%m-%Y")

        #conition to determine to use tax or not
        if values['-YES_TAX-'] == True:
            v27 = True
        elif values['-NO_TAX-'] == True:
            v27 = False

        generate_invoice(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v13, v12, v17, v18, v16, v19, v14, v15, v30, v20, v21, v22, v23, v25, v26, v27, v28, v29)
        #window.close()

window.close()
