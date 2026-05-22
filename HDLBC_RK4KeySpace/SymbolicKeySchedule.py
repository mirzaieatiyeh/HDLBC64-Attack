import SymbolicBasic as SymBsc

###################################################################################################
####                             Key-schedule process of HDLBC-64                              ####
###################################################################################################
def KeyUpdate(K: list, r: int) -> list:
    try:
        if type(K) != list or type(r) != int:
            raise TypeError("The first input must be a list and the second one must be an integer.")
        elif len(K) != 64:
            raise ValueError("The first input must be a list of length 64")
        else:
            try:
                if  r < 0 or r > 24:
                    raise ValueError("The second input must be an integer between 0 and 24.")
                else:
                    rcBin = SymBsc.SymRCGen(r)
                    Temp = K.copy()
                    Temp = SymBsc.SymPerm64(Temp)
                    lKey = Temp[ :32].copy()
                    rKey = Temp[32: ].copy()
                    lUpdt = SymBsc.SymRot16(lKey)
                    lUpdt = SymBsc.ArraySymNand(lUpdt, rKey)
                    rUpdt = SymBsc.ArraySymXor(lUpdt, rKey)
                    rUpdt = SymBsc.ArraySymXor(rUpdt, rcBin)
                    RK = lUpdt + rUpdt
                    return RK

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")


