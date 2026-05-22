import numpy as np
import Basic as Bsc

###################################################################################################
####                             Key-schedule process of HDLBC-64                              ####
###################################################################################################
def KeyUpdate(K: np.uint8, r: int) -> np.uint8:
    try:
        if K.dtype != np.uint8 or type(r) != int:
            raise TypeError("The first input must be an uint8 vector and the second one must be an integer.")
        elif (K.shape != (64, )):
            raise ValueError("The first input must be a 1D array of length 64.")
        else:
            try:
                if max(K) > 1 or min(K) < 0:
                    raise ValueError("Input must be a binary vector (its elements must be either 0 or 1).")
                else:
                    try:
                        if r < 0 or r > 24:
                            raise ValueError("The second input must be an integer between 0 and 24.")
                        else:
                            rcBin = Bsc.Int2Bin(r)
                            Temp = K.copy()
                            Temp = Bsc.Perm64(Temp)
                            lKey = Temp[ :32].copy()
                            rKey = Temp[32: ].copy()
                            lUpdt = Bsc.Rotation16(lKey)
                            lUpdt = Bsc.Nand(lUpdt, rKey)
                            rUpdt = Bsc.Xor(lUpdt, rKey)
                            rUpdt = Bsc.Xor(rUpdt, rcBin)
                            RK = np.concatenate((lUpdt, rUpdt))
                            return RK

                    except ValueError as e0:
                        print(f"ValueError: {e0}")

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")


