#Author: Cole D. Black-Stallard cdb5655@psu.edu
#Collaborators: NONE

TempIN = input("Enter temperature: ")
Unit = input("Enter unit in F/f or C/c: ")

if Unit == "F" or Unit == "f":
  TempFIN = float(TempIN)
  TempCOUT = (TempFIN - 32) * 5 / 9
  print(f"{TempFIN}\N{degree sign} in Fahrenheit is equivalent to {TempCOUT}\N{degree sign} Celsius.")

elif Unit == "C" or Unit == "c":
  TempCIN = float(TempIN)
  TempFOUT = (TempCIN * 9) / 5 + 32
  print(f"{TempCIN}\N{degree sign} in Celsius is equivalent to {TempFOUT}\N{degree sign} Fahrenheit.")
  
else:
  print(f"Invalid unit({Unit}).")