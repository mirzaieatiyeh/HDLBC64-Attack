"""
CryptDriver.py – Master key recovery driver for HDLBC-64.

This script implements the key recovery attack described in the paper:
"Near-Practical Low-Data Key Recovery Attack on Full-Round HDLBC-64".
"""

import numpy as np
import AttackFunctions as AttFunc

def main():
    Address = input("Please enetr the valid directory: \n")
    while ord(Address[0]) > 47 and ord(Address[0]) < 58:
        print("Input is not valid. Please enter the valid address.")
        Address = input("Please enetr the valid directory: \n")
    rk4Nominatelist = AttFunc.PartialDec(Address)
    MK = AttFunc.BruteForce(Address, rk4Nominatelist)
    print(f"The recovered master key is: \n{MK}")

if __name__ == "__main__":
    main()
