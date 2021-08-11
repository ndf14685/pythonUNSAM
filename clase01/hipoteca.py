# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
b=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    # if b >= 0 and b <= 11:
    #     saldo = saldo * (1+tasa/12) - pago_mensual - 1000
    #     total_pagado = total_pagado + pago_mensual + 1000
    # else: 
    #     saldo = saldo * (1+tasa/12) - pago_mensual
    #     total_pagado = total_pagado + pago_mensual    
    pago_total=pago_mensual + pago_extra
    if b >= pago_extra_mes_comienzo and b <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_total
        total_pagado = total_pagado + pago_total
    else: 
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    
    
    b=b+1
    if (saldo * (1+tasa/12)) <= pago_mensual:
        pago_mensual = saldo * (1+tasa/12)

# print('Total pagado ', round(total_pagado, 2), ' en ', b, ' meses')
    print(' mes',  b, 'Total pagado ', round(total_pagado, 2), ' resta pagar ', saldo )
print('Total pagado ', round(total_pagado, 2))
print(' meses ',  b )
