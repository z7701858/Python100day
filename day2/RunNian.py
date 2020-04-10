""" 普通闰年:公历年份是4的倍数的，且不是100的倍数，为普通闰年。 """

year = int(input("the year is "))

isornot = year %4 == 0 and year % 1000 !=0
print(isornot)

# is_leap = year % 4 == 0 and year % 100 != 0 or \
#           year % 400 == 0
# print(is_leap)