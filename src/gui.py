"""
The GUI file creates the GUI and sends the input values to generate.py.
"""
#import necessary packages and python functions

import PySimpleGUI as sg
from generate import generate_invoice

# GUI
layout = [
    [sg.Text('Please enter all necessary invoice data:')],
    [sg.Text(' ')],
    [sg.Text('KLANTGEGEVENS')],
    [sg.Text('Naam Klant', size =(15, 1)), sg.Input(key='-CLIENT_NAME-')],
    [sg.Text('Adres', size =(15, 1)), sg.Input(key='-CLIENT_ADDRESS-')],
    [sg.Text('Postcode', size =(15, 1)), sg.Input(key='-CLIENT_ZIPCODE-')],
    [sg.Text('Plaats', size =(15, 1)), sg.Input(key='-CLIENT_CITY-')],
    [sg.Text('Land', size =(15, 1)), sg.Input(key='-CLIENT_COUNTRY-')],
    [sg.Text('BTW Nummer', size =(15, 1)), sg.Input(key='-CLIENT_VATID-')],
    [sg.Text(' ')],
    [sg.Text('LEVERANCIER GEGEVENS')],
    [sg.Text('Naam Leverancier', size =(15, 1)), sg.Input(key='-SUPPLIER_NAME-')],
    [sg.Text('Adres', size=(15, 1)), sg.Input(key='-SUPPLIER_ADDRESS-')],
    [sg.Text('Postcode', size=(15, 1)), sg.Input(key='-SUPPLIER_ZIPCODE-')],
    [sg.Text('Plaats', size=(15, 1)), sg.Input(key='-SUPPLIER_CITY-')],
    [sg.Text('Land', size=(15, 1)), sg.Input(key='-SUPPLIER_COUNTRY-')],
    [sg.Text('BTW Nummer', size=(15, 1)), sg.Input(key='-SUPPLIER_VATID-')],
    [sg.Text('IBAN', size=(15, 1)), sg.Input(key='-SUPPLIER_BANKACCOUNT-')],
    [sg.Text(' ')],
    [sg.Text('FACTUUR HEADER GEGEVENS')],
    [sg.Text('Factuurnummer', size =(15, 1)), sg.Input(key='-INVOICE_NUMBER-')],
    [sg.Text('PO nummer', size=(15, 1)), sg.Input(key='-PO-')],
    [sg.Text('Aangemaakt door', size=(15, 1)), sg.Input(key='-CREATOR-')],
    [sg.Text(' ')],
    [sg.Text('FACTUUR LINE ITEMS')],
    [sg.Text('Product', size=(15, 1)), sg.Input(key='-PRODUCT_DESCRIPTION-')],
    [sg.Text('Aantal', size=(15, 1)), sg.Input(key='-COUNT-')],
    [sg.Text('Stuksprijs', size=(15, 1)), sg.Input(key='-ITEM_PRICE-')],
    [sg.Text('BTW %', size=(15, 1)), sg.Input(key='-TAX-')],
    [sg.Text(' ')],
    [sg.Text('BESTANDSNAAM & FOLDERLOCATIE')],
    [sg.Text('Bestandsnaam', size=(15, 1)), sg.Input(key='-FILENAME-')],
    [sg.Text("Choose a file: "), sg.Input(key='-FILEFOLDER-'), sg.FolderBrowse()],
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
        v16 = values['-PRODUCT_DESCRIPTION-']
        v17 = values['-COUNT-']
        v18 = values['-ITEM_PRICE-']
        v19 = values['-TAX-']
        v20 = values['-CREATOR-']
        v21 = values['-FILENAME-']
        v22 = values['-FILEFOLDER-']
        generate_invoice(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v17, v18, v16, v19, v14, v15, v20, v21, v22)
        window.close()

window.close()
