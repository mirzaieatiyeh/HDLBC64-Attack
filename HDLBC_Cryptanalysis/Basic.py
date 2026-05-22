import numpy as np

###################################################################################################
####                           32-bit representation of round number                           ####
###################################################################################################
def Int2Bin(r: int) -> np.uint8:
    try:
        if type(r) != int:
            raise TypeError("The input must be a vector of type uint8.")
        elif (r > 24 or r < 0):
            raise ValueError("Input must be an integer between 0 and 24.")
        else:
            rcBin = np.zeros(32, dtype=np.uint8)
            temp = r
            for i in range (0, 6):
                rcBin[31 - i] = temp % 2
                temp = (temp - (temp % 2)) // 2
                if temp == 0:
                    break
            return rcBin.astype(np.uint8)

    except ValueError as e1:
        print(f"SizeError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                     Performing a bitwise XOR operation on two inputs                      ####
###################################################################################################
def Xor(a: np.uint8, b: np.uint8) -> np.uint8:
    try:
        if a.dtype != np.uint8 or b.dtype != np.uint8:
            raise TypeError("Both inputs must be uint8 vectors.")
        elif (a.shape != b.shape):
            raise ValueError("Both inputs must be 1D arrays with the same length.")
        else:
            try:
                if max(a) > 1 or min(a) < 0 or max(b) > 1 or min(b) < 0:
                    raise ValueError("Inputs must be a binary vectors (their elements must be either 0 or 1).")
                else:
                    N =len(a)
                    c = np.zeros(N, dtype=np.uint8)
                    for i in range (0, N):
                        c[i] = a[i] ^ b[i]
                    return c.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")


###################################################################################################
####                     Performing a bitwise NAND operation on two inputs                     ####
###################################################################################################
def Nand(a: np.uint8, b: np.uint8) -> np.uint8:
    try:
        if a.dtype != np.uint8 or b.dtype != np.uint8:
            raise TypeError("Both inputs must be uint8 vectors.")
        elif (a.shape != b.shape):
            raise ValueError("Both inputs must be 1D arrays with the same length.")
        else:
            try:
                if max(a) > 1 or min(a) < 0 or max(b) > 1 or min(b) < 0:
                    raise ValueError("Inputs must be a binary vectors (their elements must be either 0 or 1).")
                else:
                    N =len(a)
                    c = np.zeros(N, dtype=np.uint8)
                    for i in range (0, N):
                        c[i] = 1 - (a[i] & b[i])
                    return c.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                                     HDLBC permutation                                     ####
###################################################################################################
def Perm64(a: np.uint8) -> np.uint8:
    try:
        if a.dtype != np.uint8:
            raise TypeError("The input must be a vector of type uint8.")
        elif a.shape != (64, ) or max(a) > 1 or min(a) < 0:
            raise ValueError("Input must be a 64-bit binary vector.")
        else:
            M = [39, 7, 47, 15, 55, 23, 63, 31, 
                 38, 6, 46, 14, 54, 22, 62, 30, 
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25,
                 32, 0, 40, 8, 48, 16, 56, 24]
            M = np.array(M, dtype = int)
            b = np.zeros(64, dtype=np.uint8)
            for i in range (0, 64):
                b[i] = a[M[i]]
            return b.astype(np.uint8)

    except ValueError as e1:
        print(f"SizeError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                                 Inverse HDLBC permutation                                 ####
###################################################################################################
def InvPerm64(a: np.uint8) -> np.uint8:
    try:
        if a.dtype != np.uint8:
            raise TypeError("The input must be a vector of type uint8.")
        elif a.shape != (64, ) or max(a) > 1 or min(a) < 0:
            raise ValueError("Input must be a 64-bit binary vector.")
        else:
            M = [39, 7, 47, 15, 55, 23, 63, 31, 
                 38, 6, 46, 14, 54, 22, 62, 30, 
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25,
                 32, 0, 40, 8, 48, 16, 56, 24]
            M = np.array(M, dtype = int)
            b = np.zeros(64, dtype=np.uint8)
            for i in range (0, 64):
                b[M[i]] = a[i]
            return b.astype(np.uint8)

    except ValueError as e1:
        print(f"SizeError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                                    16-bit cyclic shift                                    ####
###################################################################################################
def Rotation16(a: np.uint8) -> np.uint8:
    try:
        if a.dtype != np.uint8:
            raise TypeError("The input must be a vector of type uint8.")
        elif a.shape != (32, ) or max(a) > 1 or min(a) < 0:
            raise ValueError("Input must be a 32-bit binary vector.")
        else:
            b = a[16: ].copy()
            c = a[ :16].copy()
            d = np.concatenate((b, c))
            return d.astype(np.uint8)

    except ValueError as e1:
        print(f"SizeError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                             Key-schedule process of HDLBC-64                              ####
###################################################################################################
def LeftRot1(a: np.uint8) -> np.uint8:
    try:
        if a.dtype != np.uint8:
            raise TypeError("The input must be a vector of type uint8.")
        elif a.shape != (16, ) or max(a) > 2 or min(a) < 0:
            raise ValueError("Input must be a binary vector (its elements must be either 0 or 1).")
        else:
            b = a[1: ].copy()
            c = a[ :1].copy()
            d = np.concatenate((b, c))
            return d

    except TypeError as e1:
        print(f"Input Error: {e1}")

    except ValueError as e2:
        print(f"Input Error: {e2}")

###################################################################################################
####                             Key-schedule process of HDLBC-64                              ####
###################################################################################################
def LeftRot8(a: np.uint8) -> np.uint8:
     try:
        if a.dtype != np.uint8:
            raise TypeError("The input must be a vector of type uint8.")
        elif a.shape != (16, ) or max(a) > 2 or min(a) < 0:
            raise ValueError("Input must be a binary vector (its elements must be either 0 or 1).")
        else:
            b = a[8: ].copy()
            c = a[ :8].copy()
            d = np.concatenate((b, c))
            return d

     except TypeError as e1:
        print(f"Input Error: {e1}")

     except ValueError as e2:
        print(f"Input Error: {e2}")

###################################################################################################
####                                    HDLBC-64 block reader                                  ####
###################################################################################################
def ReadBlock(Address) -> np.uint8:
    try:
        if type(Address) != str:
            raise TypeError("Input must be a string.")
        else:
            with open(Address, "r") as f:
                Data = f.read()
                f.close()
            Len = len(Data)
            block = np.zeros(64, dtype = np.uint8)
            ctr = 0
            for i in range(0, Len - 1):
                if Data[i] in "01" and Data[i + 1] not in "0123456789":
                    block[ctr] = np.uint8(Data[i])
                    ctr += 1
                elif Data[i] in "23456789" or (Data[i] in "01" and Data[i + 1] in "0123456789"):
                    raise ValueError("Wrong block values.")
                else:
                    continue
            try:
                if ctr != 64:
                    raise ValueError("The length of the block is wrong.")
                else:
                    return block

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                                   HDLBC-64 block writer                                   ####
###################################################################################################
def WriteBlock(Address: str, block: np.uint8) -> None:
    try:
        if type(Address) != str or block.dtype != np.uint8:
            raise TypeError("The first input must be a string and the second one must be a 64-bit binary vector.")
        elif block.shape != (64, ) or min(block) < 0 or max(block) > 1:
            raise TypeError("The second input must be a 64-bit binary vector.")
        else:
            with open(Address, "w") as f:
                Data = f.write("[")
                for i in range(0, 63):
                    f.write(f"{block[i]}, ")
                f.write(f"{block[63]}]")
                f.close()

    except TypeError as e1:
        print(f"TypeError: {e1}")

    except TypeError as e2:
        print(f"TypeError: {e2}")
