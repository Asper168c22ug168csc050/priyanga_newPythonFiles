year = int(input("Enter year:"))
if year %4==0 and year%100 != 0:
  print(year,"is a leep year")
elif year %100 == 0:
  print(year,"is not a leep year")
elif year %400==0:
 print(year,"is a leep year")
else:
 print(year,"is not a leep year")
