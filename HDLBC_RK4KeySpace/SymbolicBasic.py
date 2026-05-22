###################################################################################################
####                               Symbolic master-key generator                               ####
###################################################################################################
def SymMKGen() -> list:
    MK = []
    for i in range (0, 64):
        MK.append(f"K{i}")
    return MK

###################################################################################################
####                             Symbolic bit-based NAND operator                              ####
###################################################################################################
def SymNand(a: str, b: str) -> str:
    try:
        if type(a) != str or type(b) != str:
            raise TypeError("Both inputs must be strings.")
        else:
            if a == "0" or b == "0":
                c = "1"
            elif a == b:
                c = f"Xor({a}, 1)"
            else:
                c = f"Nand({a}, {b})"
            return c

    except TypeError as e:
        print(f"Invalid inputs: {e}")


###################################################################################################
####                              Symbolic bit-based XOR operator                              ####
###################################################################################################
def SymXor(a: str, b: str) -> str:
    try:
        if type(a) != str or type(b) != str:
            raise TypeError("Both inputs must be strings.")
        else:
            if a == "0":
                c = b
            elif b == "0":
                c = a
            elif a == b:
                c = "0"
            else:
                c = f"Xor({a}, {b})"
            return c

    except TypeError as e:
        print(f"Invalid inputs: {e}")

###################################################################################################
####                            Symbolic vector-based NAND operator                            ####
###################################################################################################
def ArraySymNand(A: list, B: list) -> list:
    try:
        if type(A) != list or type(B) != list:
            raise TypeError("Both inputs must be lists.")
        elif len(A) != len(B):
            raise ValueError("Both inputs must be 1D lists with the same length.")
        else:
            m = len(A)
            C = []
            for i in range(0, m):
                c = SymNand(A[i], B[i])
                C.append(c)
            return C

    except TypeError as e1:
        print(f"Invalid inputs: {e1}")

    except TypeError as e2:
        print(f"Invalid inputs: {e2}")

###################################################################################################
####                            Symbolic vector-based NAND operator                            ####
###################################################################################################
def ArraySymXor(A: list, B: list) -> list:
    try:
        if type(A) != list or type(B) != list:
            raise TypeError("Both inputs must be lists.")
        elif len(A) != len(B):
            raise ValueError("Both inputs must be 1D lists with the same length.")
        else:
            m = len(A)
            C = []
            for i in range(0, m):
                c = SymXor(A[i], B[i])
                C.append(c)
            return C

    except TypeError as e1:
        print(f"Invalid inputs: {e1}")

    except TypeError as e2:
        print(f"Invalid inputs: {e2}")

###################################################################################################
####                                   Symbolic 16-bit shift                                   ####
###################################################################################################
def SymRot16(A: list) -> list:
    try:
        if type(A) != list:
            raise TypeError("Input must be a list.")
        elif len(A) != 32:
            raise ValueError("Input must be a 1D lists with 32 elements.")
        else:
            B = []
            for i in range(0, 16):
                B.append(A[16 + i])
            for i in range(0, 16):
                B.append(A[i])
            return B

    except TypeError as e1:
        print(f"Invalid inputs: {e1}")

    except TypeError as e2:
        print(f"Invalid inputs: {e2}")

###################################################################################################
####                                Symbolic HDLBC permutation                                 ####
###################################################################################################
def SymPerm64(A: list) -> list:
    try:
        if type(A) != list:
            raise TypeError("The input must be a list.")
        elif len(A) != 64:
            raise ValueError("Input must be a list of 64 elements.")
        else:
            M = [39, 7, 47, 15, 55, 23, 63, 31, 
                 38, 6, 46, 14, 54, 22, 62, 30, 
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25,
                 32, 0, 40, 8, 48, 16, 56, 24]
            B = []
            for i in range (0, 64):
                B.append(A[M[i]])
            return B

    except ValueError as e1:
        print(f"SizeError: {e1}")
    
    except TypeError as e2:
        print(f"TypeError: {e2}")

###################################################################################################
####                             Symbolic round constant generator                             ####
###################################################################################################
def SymRCGen(r: int) -> list:
    try:
        if type(r) != int or r < 0 or r > 24:
            raise TypeError("The input must be an integer between 0 and 24.")
        else:
            rc = []
            for i in range (0, 27):
                rc.append("0")
            temp = r
            for i in range (0, 5):
                b = int(temp // 2 ** (4 - i))
                rc.append(f"{b}")
                temp -= b * (2 ** (4 - i))
                temp = int(temp)
            return rc

    except TypeError as e:
        print(f"TypeError: {e}")
