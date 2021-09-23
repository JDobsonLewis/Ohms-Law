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
    check=[V, I, R, P]
    if check.count(x)>=3:
        print(" ")
        print("Too many unknowns, please try again.")
        print(" ")
    else:
        if V == x:
            if I == x:  # Voltage and current unknown
                P = float(P)
                R = float(R)
                V = str(pow((P * R), 0.5))
                I = str(pow(P / R, 0.5))
                print("Voltage = " + V + " Volts")
                print("Current = " + I + " Amperes")
            elif R == x:  # Voltage and resistance unknown
                P = float(P)
                I = float(I)
                R = str(P / pow(I, 2))
                V = str(P / I)
                print("Voltage = " + V + " Volts")
                print("Resistance = " + R + " Ohms")
            elif P == x:  # Voltage and power unknown
                I = float(I)
                R = float(R)
                V = str(I * R)
                P = str(R * pow(I, 2))
                print("Voltage = " + V + " Volts")
                print("Power = " + P + " Watts")
            else:  # Only voltage not known
                I = float(I)
                R = float(R)
                P = float(P)
                V = str(P / I)
                print("Voltage = " + V + " Volts")
                print(" ")
        elif I == x:
            if V == x:  # Voltage and current unknown
                P = float(P)
                R = float(R)
                V = str(pow((P * R), 0.5))
                I = str(pow(P / R, 0.5))
                print("Voltage = " + V + " Volts")
                print("Current = " + I + " Amperes")
            elif R == x:  # Current and resistance unknown
                P = float(P)
                V = float(V)
                R = str(pow(V, 2) / P)
                I = str(P / V)
                print("Current = " + I + " Amperes")
                print("Resistance = " + R + " Ohms")
            elif P == x:  # Current and power unknown
                V = float(V)
                R = float(R)
                I = str(V / R)
                P = str(pow(V, 2) / R)
                print("Current = " + I + " Amperes")
                print("Power = " + P + " Watts")
            else:  # Only Current not known
                V = float(V)
                R = float(R)
                P = float(P)
                I = str(P / V)
                print("Current = " + I + " Amperes")
                print(" ")
        elif R == x:
            if V == x:  # Voltage and current unknown
                P = float(P)
                I = float(I)
                R = str(P / pow(I, 2))
                V = str(P / I)
                print("Voltage = " + V + " Volts")
                print("Resistance = " + R + " Ohms")
            elif I == x:  # Current and resistance unknown
                P = float(P)
                V = float(V)
                R = str(pow(V, 2) / P)
                I = str(P / V)
                print("Current = " + I + " Amperes")
                print("Resistance = " + R + " Ohms")
            elif P == x:  # Resistance and power unknown
                V = float(V)
                I = float(I)
                R = str(V / I)
                P = str(V * I)
                print("Resistance = " + R + " Ohms")
                print("Power = " + P + " Watts")
            else:  # Only Resistance not known
                V = float(V)
                I = float(I)
                P = float(P)
                R = str(V / I)
                print("Resistance = " + R + " Ohms")
                print(" ")
        elif P == x:
            if V == x:  # Voltage and power unknown
                I = float(I)
                R = float(R)
                V = str(I * R)
                P = str(pow(I, 2) * R)
                print("Voltage = " + V + " Volts")
                print("Power = " + P + " Watts")
            elif I == x:  # Power and current unknown
                V = float(V)
                R = float(R)
                I = str(V / R)
                P = str(pow(V, 2) / R)
                print("Current = " + I + " Amperes")
                print("Power = " + P + " Watts")
            elif R == x:  # Power and resistance unknown
                V = float(V)
                I = float(I)
                R = str(V / I)
                P = str(V * I)
                print("Resistance = " + R + " Ohms")
                print("Power = " + P + " Watts")
            else:  # Only power is unknown
                V = float(V)
                I = float(I)
                R = float(R)
                P = str(I * V)
                print("Power = " + P + " Watts")
                print(" ")
