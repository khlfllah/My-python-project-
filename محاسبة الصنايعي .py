#مشروع محاسبة الصنايعي
#ادخال الطول و العرض و قيمة المتر  من المستخدم 
length = float(input(" enter the length :\n"))
width = float(input(" enter the width : \n"))
money = float(input("how much the 1 meter : \n"))
#حساب المساحة و قيمة العمل 
area = length * width
all_money = area * money 
# طباعة المساحة و القيمة النهائية للعمل 
print (f"the area is : {area} " )
print (f"the money is :  {all_money}$")
