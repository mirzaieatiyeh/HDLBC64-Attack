import numpy as np

###################################################################################################
####                         Integer to 32-bit binary vector convertor                         ####
###################################################################################################
def Int2Bin(r: int) -> np.uint8:
    try:
        if type(r) != int:
            raise TypeError("The input must be an integer.")
        elif (r > 65535 or r < 0):
            raise ValueError("Input must be an integer between 0 and 65535.")
        else:
            rcBin = np.zeros(16, dtype = np.uint8)
            temp = r
            for i in range (0, 16):
                rcBin[15 - i] = temp % 2
                temp = (temp - (temp % 2)) // 2
                if temp == 0:
                    break
            return rcBin.astype(np.uint8)

    except ValueError as e1:
        print(f"SizeError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                            32-bit vector to integer convertor                             ####
###################################################################################################
def Bin2Int(A: np.uint8) -> int:
    try:
        if A.dtype != np.uint8 or A.shape != (16, ):
            raise TypeError("The input must be a 32-bit binary vector.")
        elif np.max(A) > 1 or np.min(A) < 0:
            raise ValueError("The input must be a 32-bit binary vector (elements of the input vector must be either 0 or 1).")
        else:
            u = 0
            p = 1
            for i in range (0, 16):
                u += int(A[15 - i]) * p
                p *= 2
            return u

    except ValueError as e1:
        print(f"ValueError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                     Performing a bitwise XOR operation on two inputs                      ####
###################################################################################################
def Xor(a: int, b: int) -> np.uint8:
    try:
        if type(a) != int or type(b) != int:
            raise TypeError("Both inputs must be integer vectors between 0 and 1.")
        elif a < 0 or a > 1 or b < 0 or b > 1:
            raise ValueError("Both inputs must be integer vectors between 0 and 1")
        else:
            c = int((a + b) % 2)
            return c

    except ValueError as e1:
        print(f"ValueError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")


###################################################################################################
####                     Performing a bitwise NAND operation on two inputs                     ####
###################################################################################################
def Nand(a: int, b: int) -> int:
    try:
        if type(a) != int or type(b) != int:
            raise TypeError("Both inputs must be integer vectors between 0 and 1.")
        elif a < 0 or a > 1 or b < 0 or b > 1:
            raise ValueError("Both inputs must be integer vectors between 0 and 1")
        else:
            c = int(1 - a * b)
            return c

    except ValueError as e1:
        print(f"ValueError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")



