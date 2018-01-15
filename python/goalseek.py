from sympy import *
import math
import numpy as np
import pandas as pd
import datetime


#---------------------------------------------

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

kwota_netto = 100000.00
okres_kredytowania = 30*12
prowizja = 5
oprocentowanie = 9.99
stawka_ubezpieczenia = 0.25
ubezpieczenie = false
kwota_brutto = round(kwota_netto + kwota_netto * prowizja / 100, 2)
data_uruchomienia_kredytu = datetime.date(2017,12,12)
data_platnosci_pierwszej_raty = datetime.date(2018,1,12)
dni_w_roku = 365
okres_oprocentowania = 12

rata_pmt = round(abs(np.pmt(oprocentowanie / okres_oprocentowania / 100, okres_kredytowania, kwota_brutto)), 2)
print("rata pmt %f" % rata_pmt)

def calculate_loan(rata_lacznie):
    df = pd.DataFrame({ 'Data' : pd.date_range(data_uruchomienia_kredytu, periods=okres_kredytowania, freq='MS').shift( data_platnosci_pierwszej_raty.day - 1, freq='D') })
    for rata in df.itertuples():
        if rata.Index == 0:
            liczba_dni = (data_platnosci_pierwszej_raty - data_uruchomienia_kredytu).days
            kapital = kwota_brutto
        else:
            poprzednia_rata = df.loc[rata.Index - 1]
            liczba_dni = (rata.Data - poprzednia_rata['Data']).days
            kapital = poprzednia_rata['Kapitał_pozostały']
#            if abs(kapital) == 0:
#                return kwota_brutto + rata_lacznie

        rata_odsetkowa = round(kapital * oprocentowanie / dni_w_roku / 100 * liczba_dni, 2) 
        rata_kapitalowa = rata_lacznie - rata_odsetkowa
        if rata_kapitalowa > kapital:
            rata_kapitalowa = kapital
        df.loc[ rata.Index, 'Liczba_dni'] = liczba_dni
        df.loc[ rata.Index, 'Kapitał'] = kapital
        df.loc[ rata.Index, 'Rata_kapitałowa'] = rata_kapitalowa
        df.loc[ rata.Index, 'Rata_odsetkowa'] = rata_odsetkowa
        df.loc[ rata.Index, 'Rata_łącznie'] = rata_kapitalowa + rata_odsetkowa 
        df.loc[ rata.Index, 'Kapitał_pozostały'] = kapital - rata_kapitalowa  
    #df.index = df.index + 1
    #print(df[df.Kapitał_pozostały < 1])
    return df['Rata_kapitałowa'].sum()

def rata_korekta(gap_size):
    return 0.01

#print(round(kwota_brutto - df['Rata_kapitałowa'].sum(), 2))
rata_kandydat = rata_pmt
kwota_brutto_gap_prev = None
nr_przyblizenia = 0
while True:
    kwota_brutto_gap = round(kwota_brutto - calculate_loan(rata_kandydat),2)
    print("%s: Test dla raty '%.2f' -> różnica na kapitale '%.2f'" % (datetime.datetime.now().isoformat(), rata_kandydat, kwota_brutto_gap))
    if kwota_brutto_gap > 0:
        rata_kandydat = rata_kandydat + rata_korekta(kwota_brutto_gap)
        nr_przyblizenia = nr_przyblizenia + 1
    elif kwota_brutto_gap < 0:
        rata_kandydat = rata_kandydat - rata_korekta(kwota_brutto_gap)
        nr_przyblizenia = nr_przyblizenia + 1

    if abs(kwota_brutto_gap) == 0 or nr_przyblizenia > 100:
        break


