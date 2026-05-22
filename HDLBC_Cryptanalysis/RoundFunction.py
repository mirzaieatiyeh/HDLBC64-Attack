import numpy as np
import Basic as Bsc

###################################################################################################
####                                        FA function                                        ####
###################################################################################################
def FAfunc(L: np.uint8, R: np.uint8, SK: np.uint8) -> np.uint8:
    try:
        if L.dtype != np.uint8 or R.dtype != np.uint8 or SK.dtype != np.uint8:
            raise TypeError("All inputs must be uint8 vectors.")
        elif (L.shape != R.shape) or (R.shape != SK.shape) or (SK.shape != (16, )):
            raise ValueError("All inputs must be 16-bit vectors.")
        else:
            try:
                if max(L) > 1 or min(L) < 0 or max(R) > 1 or min(R) < 0 or max(SK) > 1 or min(SK) < 0:
                    raise ValueError("Inputs must be a binary vectors (their elements must be either 0 or 1).")
                else:
                    rUpdt = Bsc.LeftRot8(R)
                    lUpdt = Bsc.LeftRot1(L)
                    lUpdt = Bsc.Nand(lUpdt, rUpdt)
                    F = Bsc.Xor(lUpdt, rUpdt)
                    F = Bsc.Xor(F, SK)
                    return F.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                                   HDLBC Round function                                    ####
###################################################################################################
def Roundfunc(P: np.uint8, RK: np.uint8) -> np.uint8:
    try:
        if P.dtype != np.uint8 or RK.dtype != np.uint8:
            raise TypeError("Two inputs must be uint8 vectors.")
        elif (P.shape != (64, )) or (RK.shape != (32, )):
            raise ValueError("The first inputs must be a 64-bit vector and the second one must be a 32-bit vector.")
        else:
            try:
                if max(P) > 1 or min(P) < 0 or max(RK) > 1 or min(RK) < 0:
                    raise ValueError("Two inputs must be binary vectors (their elements must be either 0 or 1).")
                else:
                    SK1 = RK[ :16].copy()
                    SK2 = RK[16: ].copy()
                    P0 = P[ :16].copy()
                    P1 = P[16:32].copy()
                    P2 = P[32:48].copy()
                    P3 = P[48: ].copy()
                    W = FAfunc(P0, P2, SK1)
                    X1 = Bsc.Xor(W, P1)
                    X3 = Bsc.Xor(W, P3)
                    Z = FAfunc(X1, X3, SK2)
                    X0 = Bsc.Xor(Z, P0)
                    X2 = Bsc.Xor(Z, P2)
                    Y = np.concatenate((X2, X3, X0, X1))
                    C = Bsc.Perm64(Y)
                    return C.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                               HDLBC Inverse round function                                ####
###################################################################################################
def InvRoundfunc(C: np.uint8, RK: np.uint8) -> np.uint8:
    try:
        if C.dtype != np.uint8 or RK.dtype != np.uint8:
            raise TypeError("Two inputs must be uint8 vectors.")
        elif (C.shape != (64, )) or (RK.shape != (32, )):
            raise ValueError("The first inputs must be a 64-bit vector and the second one must be a 32-bit vector.")
        else:
            try:
                if max(C) > 1 or min(C) < 0 or max(RK) > 1 or min(RK) < 0:
                    raise ValueError("Two inputs must be binary vectors (their elements must be either 0 or 1).")
                else:
                    SK1 = RK[ :16].copy()
                    SK2 = RK[16: ].copy()
                    Y = Bsc.InvPerm64(C)
                    X0 = Y[ :16].copy()
                    X1 = Y[16:32].copy()
                    X2 = Y[32:48].copy()
                    X3 = Y[48: ].copy()
                    Z = FAfunc(X3, X1, SK2)
                    P0 = Bsc.Xor(X0, Z)
                    P2 = Bsc.Xor(X2, Z)
                    W = FAfunc(P2, P0, SK1)
                    P1 = Bsc.Xor(X1, W)
                    P3 = Bsc.Xor(X3, W)
                    P = np.concatenate((P2, P3, P0, P1))
                    return P.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")
