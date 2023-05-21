def FizzfckngBuzz ():
  for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
      print("fizz fucking buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzzz")
    else:
        print(i)
 
FizzfckngBuzz()
