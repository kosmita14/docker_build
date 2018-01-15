from sympy import *
import math
import numpy as np
import pandas as pd
from datetime import date
import decimal

def myround(float_to_round, placeholder):
    myfloat = float_to_round
    myfloat *= 100 # cost = 555.66
    myfloat += 0.5 # cost = 556.16
    myfloat = int(myfloat) # cost = 556
    myfloat /= float(100) # cost =  5.56
    return myfloat

d = Symbol('d')
b=77
c=57
e=(b+c+d)/3
print(solve(e-75))

decimal.getcontext().prec = 2
rate = 0.0999
start_amount = 10500.0
end_amount = 0.0 
diff_amount = start_amount - end_amount
# nr_years = 4
payment_frequency = int (12)
nr_months = 96 # = nr_years * payment_frequency
per_np = np.arange (nr_months) + 1 # +1 because index starts with 1 here
#per_np = [31 2891] + 1
#per_np = np.arange (0, nr_months, 30) + 1
#print(per_np)

pay_b = rate / payment_frequency * end_amount
ipmt_np = np.ipmt (rate / payment_frequency, per_np, nr_months, diff_amount) - pay_b
ppmt_np = np.ppmt (rate / payment_frequency, per_np, nr_months, diff_amount)

#print(np.fabs(ppmt_np) + np.fabs(ipmt_np))

for payment in per_np:
    idx = payment - 1
    principal = math.fabs (ppmt_np [idx])
    start_amount = start_amount - principal
    interest = math.fabs (ipmt_np [idx])
    instalment = principal + interest
    print (payment, "\t", principal, "\t", interest, "\t\t", instalment, "\t\t", start_amount)


print (np.sum (ipmt_np))
print (np.sum (ppmt_np))
print (np.sum (ipmt_np) + np.sum (ppmt_np))


print("PMT 1: '%f'" % np.pmt(0.0999/12, 96, 10500.00))
print("PMT 2: '%f'" % np.pmt(rate/payment_frequency, nr_months, diff_amount))

p = rate/payment_frequency
print("p: %f" % p)
nr_months = (2922 / 365) * 12
print("nr_months: %f" % nr_months)

R = diff_amount * (p * math.pow((1 + p), nr_months) / (math.pow((1 + p), nr_months) -1)) 

print(R)

#---------------------------------------------

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

kwota_netto = 10000.00
okres_kredytowania = 96
prowizja = 5
oprocentowanie = 9.99
stawka_ubezpieczenia = 0.25
ubezpieczenie = false
kwota_brutto = round(kwota_netto + kwota_netto * prowizja / 100, 2)
data_uruchomienia_kredytu = date(2017,12,12)
data_platnosci_pierwszej_raty = date(2018,1,12)
dni_w_roku = 365
okres_oprocentowania = 12

rata_lacznie = round(abs(np.pmt(oprocentowanie / okres_oprocentowania / 100, okres_kredytowania, kwota_brutto)), 2) 
print("rata łącznie %f" % rata_lacznie)

df = pd.DataFrame({ 'Data' : pd.date_range(data_uruchomienia_kredytu, periods=okres_kredytowania, freq='MS').shift( data_platnosci_pierwszej_raty.day - 1, freq='D') })

for rata in df.itertuples():
    if rata.Index == 0:
        liczba_dni = (data_platnosci_pierwszej_raty - data_uruchomienia_kredytu).days
        kapital = kwota_brutto
    else:
        poprzednia_rata = df.loc[rata.Index - 1]
        liczba_dni = (rata.Data - poprzednia_rata['Data']).days
        kapital = poprzednia_rata['Kapitał_pozostały']

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

df.index = df.index + 1
print(df)
print(round(kwota_brutto - df['Rata_kapitałowa'].sum(), 2))
