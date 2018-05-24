str = str(input("enter the string:\n"))
try:
    i = float(str)
except (ValueError, TypeError):
    print('no')
else:
  print('yes')
