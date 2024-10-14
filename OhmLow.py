def Menu():
    print("""
             1) U:
             2) I: 
             3) R:
             4) Stop
           """)
    valg = int(input("Indtast 1,2,3 eller 4:  "))
    if valg==1:
        stateU()
    elif valg==2:
        stateI()
    elif valg==3:
        stateR()
    elif valg==4:
        stop()
def stateU():
    print("Indtast værdierne for I og R: ")
    strom = float(input("I=: "))
    modstand = float(input("R=: "))
    spaending=strom*modstand
    print(f"Spaending er U={spaending} [volt]")
    beregningfile(spaending, strom, modstand)
    Menu()
def stateI():
    print("Indtast værdierne for U og R: ")
    spaending = float(input("U=: "))
    modstand = float(input("R=: "))
    strom=spaending/modstand
    print(f"Strom er I={strom} [Ampere]")
    beregningfile(spaending, strom, modstand)
    Menu()
def stateR():
    print("Indtast værdierne for U og I: ")
    spaending = float(input("U=: "))
    strom = float(input("I=: "))
    modstand=spaending/strom
    print(f"modstand er R={modstand} [Ohm]")
    beregningfile(spaending, strom, modstand)
    Menu()
def stop():
    exit
def beregningfile(spaending, strom, modstand):
    file = open("ohm.txt", "a")
    file.write("\n")
    file.write(f"Modstanden i kredsloebet = {str(modstand)} [Ohm]")
    file.write("\n")
    file.write(f"Spaendingen i kredsloebet = {str(spaending)} [V]")
    file.write("\n")
    file.write(f"Stroemmen i kredsloebet = {str(strom)} [A]")
    file.close()
Menu()    

