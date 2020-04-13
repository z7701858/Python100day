"""
英制单位英寸和公制单位厘米互换
1英寸(in)=2.54厘米(cm)
"""
unit = input ("unit=(in/cm)")
value = float(input ("value="))

if unit == 'in' :
    valueNew = value * 2.54
    print("%.2f in = %.2f cm" % (value,valueNew))
elif unit == 'cm':
    valueNew = value/2.54
    print("%.2f cm = %.2f in" % (value,valueNew))
else :
    print("wrong unit!")