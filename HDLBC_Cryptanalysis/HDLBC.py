import numpy as np
import RoundFunction as RoundFnc
import KeySchedule as KSch
from Basic import ReadBlock, WriteBlock

###################################################################################################
####                                 HDLBC encryption process                                  ####
###################################################################################################
def Encrypt(P: np.uint8, MK: np.uint8) -> np.uint8:
    try:
        if P.dtype != np.uint8 or MK.dtype != np.uint8:
            raise TypeError("Both inputs must be uint8 vectors.")
        elif (P.shape != (64, )) or (MK.shape != (64, )):
            raise ValueError("Two inputs must be 64-bit vectors.")
        else:
            try:
                if max(P) > 1 or min(P) < 0 or max(MK) > 1 or min(MK) < 0:
                    raise ValueError("Both inputs must be binary vectors (their elements must be either 0 or 1).")
                else:
                    C = P.copy()
                    RK = MK.copy()
                    for r in range(0, 25):
                        RK = KSch.KeyUpdate(RK, r)
                        RKEff = RK[32: ].copy()
                        C = RoundFnc.Roundfunc(C, RKEff)
                    return C.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                             HDLBC partial decryption process                              ####
###################################################################################################
def PartDecrypt(C: np.uint8, RK: list, Nr: int) -> np.uint8:
    try:
        if C.dtype != np.uint8 or type(RK) != list or type(Nr) != int:
            raise TypeError("The first inputs must be an uint8 vector, the middle input must be a list, and the last input must be a postive integer value.")
        elif C.shape != (64, ) or len(RK) != Nr:
            raise ValueError(f"The first input must be a 64-bit vectors, and the second input must contain {Nr} elements.")
        else:
            try:
                if max(C) > 1 or min(C) < 0 or Nr < 1 or Nr > 25:
                    raise ValueError("The first inputs must be a binary vector (their elements must be either 0 or 1) and the last input must be a positive integer less than 26.")
                else:
                    X = C.copy()
                    for i in range(0, Nr):
                        currentRK = RK[Nr - i - 1].copy()
                        RKEff = currentRK[32: ].copy()
                    for r in range(0, Nr):
                        X = RoundFnc.InvRoundfunc(X, RKEff)
                    return X.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")
    
    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                                  HDLBC Encryption Oracle                                  ####
###################################################################################################
def EncOracle(ptxList: list, Address: str) -> list:
    try:
        if type(ptxList) != list or type(Address) != str:
            raise TypeError("The first input must be a list and the second one must be a string.")
        else:
            ctxList = []
            Len = len(ptxList)
            MK = ReadBlock(Address)
            for i in range(0, Len):
                C = Encrypt(ptxList[i], MK)
                ctxList.append(C)
            return ctxList
                
    except TypeError as e3:
        print(f"TypeError: {e3}")
