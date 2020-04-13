"""
百分制成绩转换为等级制成绩

如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
"""

grade = int(input("your grade is "))

if grade < 60 :
    print("E")
elif grade < 70 :
    print("D")
elif grade < 80 :
    print("C")
elif grade < 90 :
    print("B")
else :
    print("A")