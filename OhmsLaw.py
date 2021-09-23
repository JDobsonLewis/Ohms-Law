#--------------------------------------------------------------------------------------------------------------------------------
#--Ohm's Law Calculator
#--By: Jonathan Dobson-lewis

#--Comments: Currently this works when feeding it a single variable x. I'm currently working to make it accept two x values.

#--------------------------------------------------------------------------------------------------------------------------------

print("OHM'S LAW CALCULATOR")
print("By: Jonathan Dobson-Lewis")
print(" ")
print("Enter the known variables V, I, R, and P. For the unknown variables, enter 'x' instead of a value.")
print(" ")
print(" ")
i = 0
while i < 100:
    i+=1
    x = "x"
    V = input("Voltage = ")
    I = input("Current = ")
    R = input("Resistance = ")
    P = input("Power = ")

    if V == x and I != x and R != x and P != x:
        I = float(I)
        R = float(R)
        P = float(P)
        V = str(P / I)
        print("Voltage = " + V + " Volts")
        print(" ")
    elif I == x and V != x and R != x and P != x:
        V = float(V)
        R = float(R)
        P = float(P)
        I = str(P / V)
        print("Current = " + I + " Amperes")
        print(" ")
    elif R == x and V != x and I != x and P != x:
        V = float(V)
        I = float(I)
        P = float(P)
        R = str(V / I)
        print("Resistance = " + R + " Ohms")
        print(" ")

    elif P == x and V != x and I != x and R != x:
        V = float(V)
        I = float(I)
        R = float(R)
        P = str(I * V)
        print("Power = " + P + " Watts")
        print(" ")



