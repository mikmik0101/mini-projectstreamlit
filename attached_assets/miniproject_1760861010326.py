name=input("Enter your name: ")
print(f"Hiiiii, {name}!🌟 I'm so happy to have you here. Its always a pleasure to meet someone new—get comfy, take your time, and enjoy the experience.")
print("wadduyuwant to try, pick a number  " \
"[1]: age checker" \
"[2]: mini tusoktusok" \
"[3]: jackempoy")
user=int(input("enter the number: "))
if user==1:
    print("okay, let's check your age")
    print("")
    year=int(input('what year are you '))
    age=2025-year
    print(f"you are currently {age} years old")
    print(f"and next year you are going to {age+1}")
    if age>=18:
     print('legal age')
    else:
     print('minor')
elif user==2:
 print(f"Hi poooo, {name}! Welcome sa aking mini store, Wadduyuwant to buy?\n")

 print("HERE'S THE MENU:")
 print("FISHBALL = 10.00 per stick")
 print("KIKIAM   = 10.00 per stick")
 print("HOTDOG   = 15.00 per piece")
 print("KWEKWEK  = 20.00 per stick\n")
 print("Quantity only\n")


 fball = int(input("How many sticks of fishball do you want?: "))
 print()
 kikiam = int(input("How many sticks of kikiam do you want?: "))
 print()
 hotdog = int(input("How many pieces of hotdogs do you want?: "))
 print()
 egg = int(input("How many sticks of kwekwek do you want?: "))
 print()
 pera = int(input("Magkano pera mo?: "))

 print("\n\n")


 total = (fball * 10) + (kikiam * 10) + (hotdog * 15) + (egg * 20)
 print(f"The total amount of your order is: {total} pesos\n")


 change = pera - total

 if pera > total:
    print(f"Thank you for buying! Here's your change: {change} pesos")
 elif pera == total:
    print("Thank you for buying, You have no change hehe")
 else:
    print("KULANG PERA MO, LUMAYAS KA DITO!!!")
elif user==3:
  print("numbers only(1 try only): [1]rock, [2]paper, [3]scissor")
  you=int(input("pick your number: "))
  if you==1:
    print(f"you: {you}(rock) vs. "\
          " me: 2(paper)")
    print("aww you lose, better luck next time")
  elif you==2:
    print(f"you: {you}(paper) vs."\
         " me: 3(scissor)" )
    print("aww you lose, better luck next time")
  elif you==3:
    print(f"you: {you}(scissor) vs." \
          " me: 1(rock)")
    print("aww you lose, better luck next time")
  else:
    print("opps wala yan sa option")
else:
 print("wala yan sa option tih")
