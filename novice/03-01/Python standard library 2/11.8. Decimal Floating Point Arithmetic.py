from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))

Decimal('1.00') % Decimal('.10')
Decimal('0.00')
print(1.00 % 0.10)

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)
getcontext().prec = 36
print(Decimal(1) / Decimal(7))