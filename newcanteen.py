import getpass  # pasword invisible 

list1 = [[101, 15], [102, 35], [103, 50], [104, 20], [105, 10], [106, 15], [107, 10], [108, 15], [109, 15], [110, 30], [111, 30], [112, 10], [113, 10], [114, 30], [115, 15], [116, 20], [117, 25], [118, 50], [119, 30], [120, 10]]
list2 = [[101, 'samosa'], [102, 'veg puf'], [103, 'Cheeze puf'], [104, 'Lays'], [105, 'kurkure'], [106, 'biscuits'], [107, 'tea'], [108, 'onion paratha'], [109, 'aloo paratha'], [110, 'Paneer biryani'], [111, 'Paneer fried rice'], [112, 'milk'], [113, 'coffee'], [114, 'Sambhar vada '], [115, 'veg cutlet'], [116, 'plain maggie'], [117, 'Cheeze maggie'], [118, 'Masala Dosa'], [119, 'Paneer noodles'], [120, 'cold drinks']]
name = ''
def declare():
  print("\n          IIT Canteen system ")
  print("             Canteen Menu\n")
  print("101. samosa                  -  Rs15")
  print("102. veg puf                 -  Rs35")  
  print("103. Cheeze puf              -  Rs50")   
  print("104. lays                    -  Rs20")   
  print("105. kurkure                 -  Rs10")    
  print("106. biscuits                -  Rs15")      
  print("107. tea                     -  Rs10")      
  print("108. onion paratha           -  Rs15")
  print("109. aloo paratha            -  Rs15")   
  print("110. Paneer biryani          -  Rs30")
  print("111. Paneer fried rice       -  Rs30")
  print("112. milk                    -  Rs10")
  print("113. coffee                  -  Rs10")  
  print("114. Sambhar vada            -  Rs30")    
  print("115. veg cutlet              -  Rs15")    
  print("116. plain maggie            -  Rs20")     
  print("117. Cheeze maggie           -  Rs25")       
  print("118. Masala Dosa             -  Rs50")       
  print("119. Paneer noodles          -  Rs30")         
  print("120. cold drinks             -  Rs10")
  print("150. Exit")

def input_function():
  name = input('\nEnter ur name: ')
  while(1):
    print('Enter password: ',end='')
    pwd = getpass.getpass()  # use of predefined function
    # pwd = input('Enter password: ')
    if(pwd == '123'):
      print('Welcome ',name)
      break
    else:
      print("Incorrect input ... pls try again!!!")

def find_item(mylist,ch): # list2 and ch=106
  for i in range(len(mylist)):
    if ch == mylist[i][0]:
      return mylist[i][1]

def order_food():
  choice = []
  items = []
  bill = 0
  while(1):
    ch = int(input('\nEnter ur choice: '))
    if(ch == 150):
      print(name,'thanks for visiting ... ')
      break
    elif ch < 101 or ch > 120:
      print("Incorrect input ... pls try again!!!")
    else:
      
      print('You order is  ',find_item(list2,ch)) # ch = 101, 103, 105
      bill = bill + find_item(list1,ch)
      print('Bill is  ',bill)
      choice.append(ch)
      items.append(find_item(list2,ch)) # samosa, 
  if bill > 0:
    print("\nSummary of your order")    
    print(f"{'Item No' : <10}{'Item Name' : ^15}{'Amount': ^15}")    
    for i in range(len(choice)):
      print(f"{choice[i] : <10}{items[i] : ^15}{find_item(list1,choice[i]): ^15}")    
  print('\nTotal bill is: ',bill,'Rs')  


declare()
input_function()
order_food()