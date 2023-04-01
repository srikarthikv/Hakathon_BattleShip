import random

#function to print the map format
def printmap(map):
  for i in map:
    for j in i:
      print("\t",j,end="")
    print("\n")  
#returns a random between vertical and horizontal
def randomhoriverti():
  ch=random.randint(0,1)
  if ch==0:
    return "horizontal"
  else:
    return "vertical"
#print("map2 \n")
'''player1_ship_row=[1,2,3,4,5,6,7,8,9,10]
player1_ship_column=[1,2,3,4,5,6,7,8,9,10]

player2_ship_row=[1,2,3,4,5,6,7,8,9,10]
# player2_ship_column=[1,2,3,4,5,6,7,8,9,10]'''

#making ship rows for player 1 
ship_row1 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row2 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row3 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row4 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row5 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row6 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row7 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row8 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row9 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
ship_row10=[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]

#making attack map rows for player 1
map_row1 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row2 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row3 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row4 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row5 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row6 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row7 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row8 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row9 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
map_row10=[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]

#making ship rows for player 2
two_ship_row1 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row2 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row3 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row4 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row5 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row6 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row7 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row8 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row9 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_ship_row10=[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]

#making attack map rows for player 2 
two_map_row1 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row2 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row3 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row4 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row5 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row6 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row7 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row8 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row9 =[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]
two_map_row10=[" |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "," |_| "]

player1shipmap1=[ship_row1,ship_row2,ship_row3,ship_row4,ship_row5,ship_row6,ship_row7,ship_row8,ship_row9,ship_row10]
player1map1=[map_row1,map_row2,map_row3,map_row4,map_row5,map_row6,map_row7,map_row8,map_row9,map_row10]
player2shipmap=[two_ship_row1,two_ship_row2,two_ship_row3,two_ship_row4,two_ship_row5,two_ship_row6,two_ship_row7,two_ship_row8,two_ship_row9,two_ship_row10]
player2map=[two_map_row1,two_map_row2,two_map_row3,two_map_row4,two_map_row5,two_map_row6,two_map_row7,two_map_row8,two_map_row9,two_map_row10]



number_of_yourships=7
number_of_opponentships=7


'''#fleetnumbers={
    "Aircraft Carrier": 1, 
    "Battleship": 1,
    "Cruiser":1,
    "Destroyer": 2,
    "Sub-marine": 2
}'''

#placing ships on users side
AircraftCarrier=1 
Battleship=1
Cruiser=1
Destroyer=2
Submarine=2
printmap(player1shipmap1)
totalshipsremaining=7
while totalshipsremaining>0:
  print("\t\t\t\tPlease dont place a ship where already a ship is present")
  print("\t\tPlace your ships")
  choice=int(input("Enter choice\n1=AircraftCarrier\n2=Battleship\n3=Cruiser\n4=Destroyer\n5=Submarine\n"))
  
  #to place aircraft ship
  if choice==1 and AircraftCarrier>0:
    row=int(input("Enter the rownumber in the map where you want to place the Aircraft carrier\n It takes 5 boxes \nNote:from this point it faces right\n"))
    col=int(input("Enter the Column number in the map where you want to place the Aircraft carrier\n It takes 5 boxes\nNote:from this point it faces down\n"))
    alignment=input("Enter how you want to place it (horizontal/vertical)\n")
    totalshipsremaining=totalshipsremaining-1
    if alignment=="horizontal" and col<=6:
      for i in range(0,5):
        
        #underbeta testing - the following 3 lines
        #if player1shipmap1[row-1][col+i-1]=="  A  " or   player1shipmap1[row-1][col+i-1]=="  B  " or  player1shipmap1[row-1][col+i-1]=="  C  " or player1shipmap1[row-1][col+i-1]=="  D  " or  player1shipmap1[row-1][col+i-1]=="  S  ":
         #print("a Ship is already present")
        #else:

        player1shipmap1[row-1][col+i-1]="  A  "        
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    
    elif alignment=="vertical" and row<=6:
      for i in range(0,5):
        player1shipmap1[row+i-1][col-1]="  A  "       
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    else:
      print("No space to place ship")
    AircraftCarrier=AircraftCarrier-1
    printmap(player1shipmap1)
  
  #to place Battleship
  elif choice==2 and Battleship>0 :
    row=int(input("Enter the rownumber in the map where you want to place the Battleship\nIt takes 4 boxes \nNote:from this point it faces right\n"))
    col=int(input("Enter the Column number in the map where you want to place the Battleship\nIt takes 4 boxes\nNote:from this point it faces down\n"))
    alignment=input("Enter how you want to place it (horizontal/vertical)\n")
    totalshipsremaining=totalshipsremaining-1
    if alignment=="horizontal" and col<=5:
      for i in range(0,4):
        player1shipmap1[row-1][col+i-1]="  B  "
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    
    elif alignment=="vertical" and row<=5:
      for i in range(0,4):
        player1shipmap1[row+i-1][col-1]="  B  "
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    else:
      print("No space to place ship")
    Battleship=Battleship-1
    printmap(player1shipmap1)

  #to Place Cruiser
  elif choice==3 and Cruiser>0 :
    row=int(input("Enter the rownumber in the map where you want to place the Cruiser\nIt takes 3 boxes \nNote:from this point it faces right\n"))
    col=int(input("Enter the Column number in the map where you want to place the Cruiser\nIt takes 3 boxes\nNote:from this point it faces down\n"))
    alignment=input("Enter how you want to place it (horizontal/vertical)\n")
    totalshipsremaining=totalshipsremaining-1
    if alignment=="horizontal" and col<=4:
      for i in range(0,3):
        player1shipmap1[row-1][col+i-1]="  C  "
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    
    elif alignment=="vertical" and row<=4:
      for i in range(0,3):
        player1shipmap1[row+i-1][col-1]="  C  "
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    else:
      print("No space to place ship")
    Cruiser=Cruiser-1
    printmap(player1shipmap1)

  #to place Destroyer
  elif choice==4 and Destroyer>0:
    row=int(input("Enter the rownumber in the map where you want to place the Destroyer\nIt takes 2 boxes \nNote:from this point it faces right\n"))
    col=int(input("Enter the Column number in the map where you want to place the Destroyer\nIt takes 2 boxes\nNote:from this point it faces down\n"))
    alignment=input("Enter how you want to place it (horizontal/vertical)\n")
    totalshipsremaining=totalshipsremaining-1
    if alignment=="horizontal" and col<=3:
      for i in range(0,2):
        player1shipmap1[row-1][col+i-1]="  D  "
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    
    elif alignment=="vertical" and row<=3:
      for i in range(0,2):
        player1shipmap1[row+i-1][col-1]="  D  "
        
      print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    else:
      print("No space to place ship")
      Destroyer=Destroyer-1
    printmap(player1shipmap1)

  #to place Submarine
  elif choice==5 and Submarine>0:
    row=int(input("Enter the rownumber in the map where you want to place the Submarine\nIt takes 1 box \n"))
    col=int(input("Enter the Column number in the map where you want to place the Submarine\nIt takes 1 box\n"))
    player1shipmap1[row-1][col-1]="  S  "
    totalshipsremaining=totalshipsremaining-1 
    print(f"\t\t\t\t\tRemaining ships={totalshipsremaining}")
    printmap(player1shipmap1)
    Submarine=Submarine-1 
  
  #no ships available
  else:
    print("No ships available or Invalid entry")

'''






#randomly placing Computer side ships







'''
#placing ships on Computers side

#
AircraftCarrier=1 
Battleship=1
Cruiser=1
Destroyer=2
Submarine=2

totalshipsremaining=7
while totalshipsremaining>0:
  
  choice=1
  
  #to place aircraft ship
  if choice==1 and AircraftCarrier>0:
    row=random.randint(1,10)
    col=random.randint(1,10)
    alignment=randomhoriverti()
    totalshipsremaining=totalshipsremaining-1
    if alignment=="horizontal" and col<=6:
      for i in range(0,5):
        
        #underbeta testing - the following 3 lines
        #if player1shipmap1[row-1][col+i-1]=="  A  " or   player1shipmap1[row-1][col+i-1]=="  B  " or  player1shipmap1[row-1][col+i-1]=="  C  " or player1shipmap1[row-1][col+i-1]=="  D  " or  player1shipmap1[row-1][col+i-1]=="  S  ":
         #print("a Ship is already present")
        #else:

        player2shipmap[row-1][col+i-1]="  A  "        
      
    
    elif alignment=="vertical" and row<=6:
      for i in range(0,5):
        player2shipmap[row+i-1][col-1]="  A  "       
      
   
      
    AircraftCarrier=AircraftCarrier-1
   
  
  #to place Battleship
  elif choice==2 and Battleship>0 :
    row=random.randint(1,10)
    col=random.randint(1,10)
    alignment=randomhoriverti()
    totalshipsremaining=totalshipsremaining-1
    if alignment=="horizontal" and col<=5:
      for i in range(0,4):
        player2shipmap[row-1][col+i-1]="  B  "
      
    
    elif alignment=="vertical" and row<=5:
      for i in range(0,4):
        player2shipmap[row+i-1][col-1]="  B  "
     
         
    Battleship=Battleship-1
   

  #to Place Cruiser
  elif choice==3 and Cruiser>0 :
    row=random.randint(1,10)
    col=random.randint(1,10)
    alignment=randomhoriverti()
    totalshipsremaining=totalshipsremaining-1
    if alignment=="horizontal" and col<=4:
      for i in range(0,3):
        player2shipmap[row-1][col+i-1]="  C  "
     
    
    elif alignment=="vertical" and row<=4:
      for i in range(0,3):
        player2shipmap[row+i-1][col-1]="  C  "
     
  
     
    Cruiser=Cruiser-1
    
  #to place Destroyer
  elif choice==4 and Destroyer>0:
    row=random.randint(1,10)
    col=random.randint(1,10)
    alignment=randomhoriverti()
    if alignment=="horizontal" and col<=3:
      for i in range(0,2):
        player2shipmap[row-1][col+i-1]="  D  "
      
    
    elif alignment=="vertical" and row<=3:
      for i in range(0,2):
        player2shipmap[row+i-1][col-1]="  D  "
        
     
    
    Destroyer=Destroyer-1
    

  #to place Submarine
  elif choice==5 and Submarine>0:
    row=random.randint(1,10)
    col=random.randint(1,10)
    
    player2shipmap[row-1][col-1]="  S  "
    totalshipsremaining=totalshipsremaining-1 
    
    Submarine=Submarine-1 
  choice=choice+1

print("Genearated computerside ship map")
printmap(player2shipmap)





#later
while True:
  if number_of_yourships<1:
    print("game Over , you lost")
    break
  elif number_of_opponentships<1:
    print("you won ")
    break
