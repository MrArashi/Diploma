import barcode #import Barcode module
from barcode.writer import ImageWriter

def mainmenu():
    while True: #loops over and over again
        print("1. Generate a barcode")
        print("2. Validate a barcode")
        print("3. Quit")  # prints out 3 options for the user to select
        selection=int(input("Enter choice: ")) #tells user to enter a choice
        if selection==1:
            generate() #calls the function
        elif selection==2:
            validate()
        elif selection==3:
            break
        else:
            print("Invalid choice. Enter 1-3")
def generate(arg=''):
    GTIN = arg
    if arg == '':
        GTIN=(input("Enter a 7 digit GTIN number: "))
    if(len(GTIN)==7):
        G1=int(GTIN[0])
        G2=int(GTIN[1])
        G3=int(GTIN[2])
        G4=int(GTIN[3])
        G5=int(GTIN[4])
        G6=int(GTIN[5])
        G7=int(GTIN[6])
        GTINT=int(G1*3+G2+G3*3+G4+G5*3+G6+G7*3)
        roundup=round(GTINT, -1)
        GTIN8 = int(roundup - GTINT) % 10
        data = str(GTIN)+str(GTIN8)
        if arg == '':
            print(arg)
            print("Your full GTIN-8 code is: "+data)
            print (int(data))
            getbarcode(data)
        return GTIN8
    else:
        print("Nope")

def validate():
    GTIN=(input("Enter an 8 digit GTIN number: "))
    GTIN8 = generate(GTIN[0:7])
    if str(GTIN8) == GTIN[7]:
        print("Your code is valid")
    else:
        print("Your code is invalid")
def getbarcode (data): # Creation barcode
   img = barcode.get ('ean8', data, writer = ImageWriter ()) # "ean8" may choose another
   img.save(f'{data}')
mainmenu()