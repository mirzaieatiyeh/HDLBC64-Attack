import numpy as np
import KeySchedule as KeySch
import HDLBC
from Basic import Nand, Xor, ReadBlock, WriteBlock

###################################################################################################
####                          Reading the keys listed in a text file                           ####
###################################################################################################
def ReadKey(Address) -> list:
    try:
        if type(Address) != str:
            raise TypeError("The input must be the address of the target file.")
        else:
            keyList = []
            with open(Address, "r") as f:
                Data = f.read()
                f.close()
            Len = len(Data)
            ctr = 0
            while(ctr < Len):
                if Data[ctr] in "0123456789" and Data[ctr + 1] == ":":
                    ctr += 4
                    X = np.array([
                        0, 0, 0, 0,
                        0, 0, 0, 0,
                        0, 0, 0, 0,
                        0, 0, 0, 0
                        ], dtype = np.uint8)
                    for i in range(0, 16):
                        X[i] = int(Data[ctr + 2 * i])
                    keyList.append(X.copy())
                    ctr = ctr + 32
                else:
                    ctr += 1
            return keyList

    except TypeError as e:
        print("Error: Invalid input.", e)

###################################################################################################
####                                 Merging Masterkey vectors                                 ####
###################################################################################################
def MKMergeKey(A: np.uint8, B: np.uint8, C: np.uint8, D: np.uint8) -> np.uint8:
    try:
        if A.dtype != np.uint8 or A.dtype != np.uint8 or A.dtype != np.uint8 or A.dtype != np.uint8:
            raise TypeError("Inputs must be 16-bit binary vectors.")
        elif A.shape != B.shape or C.shape != D.shape or D.shape != A.shape or A.shape != (16, ):
            raise ValueError("Inputs must be 16-bit binary vectors.")
        else:
            try:
                if min(A) < 0 or max(A) > 1 or min(B) < 0 or max(B) > 1 or min(C) < 0 or max(C) > 1 or min(D) < 0 or max(D) > 1:
                    raise ValueError("Inputs must be 16-bit binary vectors, elements must be between 0 and 1.")
                else:
                    MK = np.zeros(64, dtype = np.uint8)
                    MK[0] = B[0]
                    MK[1:3] = A[0:2]
                    MK[3] = B[1]
                    MK[4] = A[2]
                    MK[5:7] = B[2:4]
                    MK[7] = A[3]
                    MK[8] = D[0]
                    MK[9:11] = C[0:2]
                    MK[11] = D[1]
                    MK[12] = C[2]
                    MK[13:15] = D[2:4]
                    MK[15] = C[3]
                    MK[16] = D[4]
                    MK[17:19] = C[4:6]
                    MK[19] = D[5]
                    MK[20] = C[6]
                    MK[21:23] = D[6:8]
                    MK[23] = C[7]
                    MK[24] = B[4]
                    MK[25:27] = A[4:6]
                    MK[27] = B[5]
                    MK[28] = A[6]
                    MK[29:31] = B[6:8]
                    MK[31] = A[7]
                    MK[32] = D[8]
                    MK[33:35] = C[8:10]
                    MK[35] = D[9]
                    MK[36] = C[10]
                    MK[37:39] = D[10:12]
                    MK[39] = C[11]
                    MK[40] = B[8]
                    MK[41:43] = A[8:10]
                    MK[43] = B[9]
                    MK[44] = A[10]
                    MK[45:47] = B[10:12]
                    MK[47] = A[11]
                    MK[48] = B[12]
                    MK[49:51] = A[12:14]
                    MK[51] = B[13]
                    MK[52] = A[14]
                    MK[53:55] = B[14: ]
                    MK[55] = A[15]
                    MK[56] = D[12]
                    MK[57:59] = C[12:14]
                    MK[59] = D[13]
                    MK[60] = C[14]
                    MK[61:63] = D[14: ]
                    MK[63] = C[15]
                    return MK.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")

    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                             Merging fourth-round key vectors                              ####
###################################################################################################
def RK4MergeKey(A: np.uint8, B: np.uint8, C: np.uint8, D: np.uint8) -> np.uint8:
    try:
        if A.dtype != np.uint8 or A.dtype != np.uint8 or A.dtype != np.uint8 or A.dtype != np.uint8:
            raise TypeError("Inputs must be 16-bit binary vectors.")
        elif A.shape != B.shape or C.shape != D.shape or D.shape != A.shape or A.shape != (16, ):
            raise ValueError("Inputs must be 16-bit binary vectors.")
        else:
            try:
                if min(A) < 0 or max(A) > 1 or min(B) < 0 or max(B) > 1 or min(C) < 0 or max(C) > 1 or min(D) < 0 or max(D) > 1:
                    raise ValueError("Inputs must be 16-bit binary vectors, elements must be between 0 and 1.")
                else:
                    RK4 = np.zeros(64, dtype = np.uint8)
                    RK4[ :4] = A[ :4]
                    RK4[4:8] = B[ :4]
                    RK4[8:12] = A[4:8]
                    RK4[12:16] = B[4:8]
                    RK4[16:20] = C[ :4]
                    RK4[20:24] = D[ :4]
                    RK4[24:28] = C[4:8]
                    RK4[28:32] = D[4:8]
                    RK4[32:36] = A[8:12]
                    RK4[36:40] = B[8:12]
                    RK4[40:44] = A[12: ]
                    RK4[44:48] = B[12: ]
                    RK4[48:52] = C[8:12]
                    RK4[52:56] = D[8:12]
                    RK4[56:60] = C[12: ]
                    RK4[60: ] = D[12: ]
                    return RK4.astype(np.uint8)

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")

    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                          Detaching the fourth-round key vectors                           ####
###################################################################################################
def DetachKey(RK4: np.uint8) -> list:
    try:
        if RK4.dtype != np.uint8:
            raise TypeError("Input must be a 64-bit binary vector.")
        elif RK4.shape != (64, ) or min(A) < 0 or max(A) > 1:
            raise ValueError("Input must be a 64-bit binary vector.")
        else:
            try:
                if min(RK4) < 0 or max(RK4) > 1:
                    raise ValueError("Input must be a 64-bit binary vector, elements must be between 0 and 1.")
                else:
                    rkPartList = []
                    rkA = np.zeros(16, dtype = np.uint8)
                    rkB = np.zeros(16, dtype = np.uint8)
                    rkC = np.zeros(16, dtype = np.uint8)
                    rkD = np.zeros(16, dtype = np.uint8)
                    rkA[ :4] = RK4[ :4] 
                    rkB[ :4] = RK4[4:8]
                    rkA[4:8] = RK4[8:12]
                    rkB[4:8] = RK4[12:16]
                    rkC[ :4] = RK4[16:20]
                    rkD[ :4] = RK4[20:24]
                    rkC[4:8] = RK4[24:28]
                    rkD[4:8] = RK4[28:32]
                    rkA[8:12] = RK4[32:36]
                    rkB[8:12] = RK4[36:40]
                    rkA[12: ] = RK4[40:44]
                    rkB[12: ] = RK4[44:48]
                    rkC[8:12] = RK4[48:52]
                    rkD[8:12] = RK4[52:56]
                    rkC[12: ] = RK4[56:60]
                    rkD[12: ] = RK4[60: ]
                    rkPartList.append(rkA)
                    rkPartList.append(rkB)
                    rkPartList.append(rkC)
                    rkPartList.append(rkD)
                    return rkPartList

            except ValueError as e1:
                print(f"ValueError: {e1}")

    except ValueError as e2:
        print(f"SizeError: {e2}")

    except TypeError as e3:
        print(f"TypeError: {e3}")

###################################################################################################
####                            Partial decryption and RK4 sieving                             ####
###################################################################################################
def PartialDec(Address: str) -> np.uint8:
    try:
        if type(Address) != str:
            raise TypeError("Input must be a valid string.")
        else:
            progressFlag = True
            k1 = ReadKey(Address + "\\RK4_0-3_8-11_32-35_40-43.txt")
            k2 = ReadKey(Address + "\\RK4_4-7_12-15_36-39_44-47.txt")
            k3 = ReadKey(Address + "\\RK4_16-19_24-27_48-51_56-59.txt")
            k4 = ReadKey(Address + "\\RK4_20-23_28-31_52-55_60-63.txt")
            ptxList =[]
            rng = np.random.default_rng()
            for i in range(0, 3):
                X = np.zeros(64, dtype = np.uint8)
                for i in range(0, 64):
                    y = rng.integers(0, 65536)
                    X[i] = np.uint8(y % 2)
                ptxList.append(X.copy())
                X[17] = 1 - X[17]
                ptxList.append(X.copy())
            masterKeyAddress = Address + "\\MasterKey.txt"
            plaintextAddress = Address + "\\Plaintext.txt"
            ciphertextAddress = Address + "\\Ciphertext.txt"
            ctxList = HDLBC.EncOracle(ptxList, masterKeyAddress)
            WriteBlock(plaintextAddress, ptxList[0])
            WriteBlock(ciphertextAddress, ctxList[0])
            ctr = 0;
            nominatedKeys = []
            for i in range(0, 649):
                for j in range (0, 649):
                    for l in range (0, 649):
                        for m in range (0, 669):
                            ctr =+ 1
                            y = 100 * ctr / (669 * 649 ** 3)
                            RK4 = RK4MergeKey(k1[i], k2[j], k3[l], k4[m])
                            RK5_25 = []
                            rk = RK4.copy()
                            for r in range(4, 25):
                                rk = KeySch.KeyUpdate(rk, r)
                                RK5_25.append(rk)
                            nominatedFlag = True
                            for n in range(0, 3):
                                C1 = ctxList[2 * n]
                                C2 = ctxList[2 * n + 1]
                                X1 = HDLBC.PartDecrypt(C1, RK5_25, 21)
                                X2 = HDLBC.PartDecrypt(C2, RK5_25, 21)
                                Delta = Xor(X1, X2)
                                if Delta[4] != 0 or Delta[20] != 0 or Delta[22] != 0 or Delta[24] != 0 or Delta[25] != 0 or Delta[30] != 0 or Delta[31] != 0 or Delta[54] != 0 or Delta[62] != 0:
                                    nominatedFlag = False
                                    break
                                else:
                                    continue
                            if nominatedFlag == True:
                                nominatedKeys.append(RK4)
                            if abs(y - round(y, 3)) < 0.0005 and progressFlag == True:
                                print(f"HDLBC cryptanalysis: {round(y, 3)}% of the partial decryption has been completed.")
                                progressFlag = False
                            elif abs(y - round(y, 3)) >= 0.0005:
                                progressFlag = True
                            else:
                                continue
            return nominatedKeys.astype(np.uint8)

    except TypeError as e:
        print(f"Input type error: {e}")

###################################################################################################
####                   Match the master key with the given fourth-round key                    ####
###################################################################################################
def MK_Matching(rk4Sec: np.uint8, secNum: int) -> list:
    try:
        if rk4Sec.dtype != np.uint8 or type(secNum) != int:
            raise TypeError("The first input must be a 16-bit binary vector and the second one must be an integer between 1 and 4.")
        elif np.shape(rk4Sec) != (16, ) or max(rk4Sec) > 1 or min(rk4Sec) < 0 or secNum < 1 or secNum > 4:
            raise ValueError("First input must be a 16-bit binary and the second input must be an integer between 1 and 4.")
        else:
            One = np.ones(1, dtype = np.uint8)
            mkList = []
            X = np.zeros(16, dtype = np.uint8)
            mkSec = np.zeros(16, dtype = np.uint8)
            if secNum == 1:
                for k1 in range(0, 2):
                    K1 = np.array([k1], dtype = np.uint8)
                    for k2 in range(0, 2):
                        K2 = np.array([k2], dtype = np.uint8)
                        for k4 in range(0, 2):
                            K4 = np.array([k4], dtype = np.uint8)
                            for k7 in range(0, 2):
                                K7 = np.array([k7], dtype = np.uint8)
                                for k25 in range(0, 2):
                                    K25 = np.array([k25], dtype = np.uint8)
                                    for k26 in range(0, 2):
                                        K26 = np.array([k26], dtype = np.uint8)
                                        for k28 in range(0, 2):
                                            K28 = np.array([k28], dtype = np.uint8)
                                            for k31 in range(0, 2):
                                                K31 = np.array([k31], dtype = np.uint8)
                                                for k41 in range(0, 2):
                                                    K41 = np.array([k41], dtype = np.uint8)
                                                    for k42 in range(0, 2):
                                                        K42 = np.array([k42], dtype = np.uint8)
                                                        for k44 in range(0, 2):
                                                            K44 = np.array([k44], dtype = np.uint8)
                                                            for k47 in range(0, 2):
                                                                K47 = np.array([k47], dtype = np.uint8)
                                                                for k49 in range(0, 2):
                                                                    K49 = np.array([k49], dtype = np.uint8)
                                                                    for k50 in range(0, 2):
                                                                        K50 = np.array([k50], dtype = np.uint8)
                                                                        for k52 in range(0, 2):
                                                                            K52 = np.array([k52], dtype = np.uint8)
                                                                            for k55 in range(0, 2):
                                                                                K55 = np.array([k55], dtype = np.uint8)
                                                                                Z0 = Nand(Xor(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(K28, K26), Nand(K4, K2))), Xor(Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                                Z1 = Nand(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                                Z2 = Nand(Xor(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Xor(Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                                Z3 = Nand(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                                Z4 = Nand(Xor(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                                Z5 = Nand(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                                Z6 = Nand(Xor(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                                Z7 = Nand(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                                Z8 = Xor(Nand(Xor(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(K28, K26), Nand(K4, K2))), Xor(Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))), Nand(Nand(K52, K50), Nand(K44, K42)))), Xor(Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                                Z9 = Xor(Nand(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42)))), Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                                Z10 = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Xor(Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)))), Xor(Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                                Z11 = Xor(Nand(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)))), Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                                Z12 = Xor(Nand(Xor(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42)))), Xor(Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                                Z13 = Xor(Nand(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42)))), Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                                Z14 = Xor(Nand(Xor(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42)))), Xor(Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                                Z15 = Xor(Nand(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42)))), Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                                X = np.concatenate((Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15))
                                                                                Delta = Xor(X, rk4Sec)
                                                                                if max(Delta) == 0:
                                                                                    mkSec[0] = k1
                                                                                    mkSec[1] = k2
                                                                                    mkSec[2] = k4
                                                                                    mkSec[3] = k7
                                                                                    mkSec[4] = k25
                                                                                    mkSec[5] = k26
                                                                                    mkSec[6] = k28
                                                                                    mkSec[7] = k31
                                                                                    mkSec[8] = k41
                                                                                    mkSec[9] = k42
                                                                                    mkSec[10] = k44
                                                                                    mkSec[11] = k47
                                                                                    mkSec[12] = k49
                                                                                    mkSec[13] = k50
                                                                                    mkSec[14] = k52
                                                                                    mkSec[15] = k55
                                                                                    mkList.append(mkSec.copy())
                                                                                else:
                                                                                    continue
            elif secNum == 2:
                for k0 in range(0, 2):
                    K0 = np.array([k0], dtype = np.uint8)
                    for k3 in range(0, 2):
                        K3 = np.array([k3], dtype = np.uint8)
                        for k5 in range(0, 2):
                            K5 = np.array([k5], dtype = np.uint8)
                            for k6 in range(0, 2):
                                K6 = np.array([k6], dtype = np.uint8)
                                for k24 in range(0, 2):
                                    K24 = np.array([k24], dtype = np.uint8)
                                    for k27 in range(0, 2):
                                        K27 = np.array([k27], dtype = np.uint8)
                                        for k29 in range(0, 2):
                                            K29 = np.array([k29], dtype = np.uint8)
                                            for k30 in range(0, 2):
                                                K30 = np.array([k30], dtype = np.uint8)
                                                for k40 in range(0, 2):
                                                    K40 = np.array([k40], dtype = np.uint8)
                                                    for k43 in range(0, 2):
                                                        K43 = np.array([k43], dtype = np.uint8)
                                                        for k45 in range(0, 2):
                                                            K45 = np.array([k45], dtype = np.uint8)
                                                            for k46 in range(0, 2):
                                                                K46 = np.array([k46], dtype = np.uint8)
                                                                for k48 in range(0, 2):
                                                                    K48 = np.array([k48], dtype = np.uint8)
                                                                    for k51 in range(0, 2):
                                                                        K51 = np.array([k51], dtype = np.uint8)
                                                                        for k53 in range(0, 2):
                                                                            K53 = np.array([k53], dtype = np.uint8)
                                                                            for k54 in range(0, 2):
                                                                                K54 = np.array([k54], dtype = np.uint8)
                                                                                Z0 = Nand(Xor(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(K29, K27), Nand(K5, K3))), Xor(Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                                Z1 = Nand(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                                Z2 = Nand(Xor(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Xor(Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                                Z3 = Nand(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                                Z4 = Nand(Xor(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                                Z5 = Nand(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                                Z6 = Nand(Xor(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                                Z7 = Nand(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                                Z8 = Xor(Nand(Xor(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(K29, K27), Nand(K5, K3))), Xor(Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))), Nand(Nand(K53, K51), Nand(K45, K43)))), Xor(Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                                Z9 = Xor(Nand(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43)))), Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                                Z10 = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Xor(Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)))), Xor(Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                                Z11 = Xor(Nand(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)))), Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                                Z12 = Xor(Nand(Xor(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43)))), Xor(Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                                Z13 = Xor(Nand(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43)))), Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                                Z14 = Xor(Nand(Xor(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43)))), Xor(Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                                Z15 = Xor(Nand(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43)))), Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                                X = np.concatenate((Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15))
                                                                                Delta = Xor(X, rk4Sec)
                                                                                if max(Delta) == 0:
                                                                                    mkSec[0] = k0
                                                                                    mkSec[1] = k3
                                                                                    mkSec[2] = k5
                                                                                    mkSec[3] = k6
                                                                                    mkSec[4] = k24
                                                                                    mkSec[5] = k27
                                                                                    mkSec[6] = k29
                                                                                    mkSec[7] = k30
                                                                                    mkSec[8] = k40
                                                                                    mkSec[9] = k43
                                                                                    mkSec[10] = k45
                                                                                    mkSec[11] = k46
                                                                                    mkSec[12] = k48
                                                                                    mkSec[13] = k51
                                                                                    mkSec[14] = k53
                                                                                    mkSec[15] = k54
                                                                                    mkList.append(mkSec.copy())
                                                                                else:
                                                                                    continue
            elif secNum == 3:
                for k9 in range(0, 2):
                    K9 = np.array([k9], dtype = np.uint8)
                    for k10 in range(0, 2):
                        K10 = np.array([k10], dtype = np.uint8)
                        for k12 in range(0, 2):
                            K12 = np.array([k12], dtype = np.uint8)
                            for k15 in range(0, 2):
                                K15 = np.array([k15], dtype = np.uint8)
                                for k17 in range(0, 2):
                                    K17 = np.array([k17], dtype = np.uint8)
                                    for k18 in range(0, 2):
                                        K18 = np.array([k18], dtype = np.uint8)
                                        for k20 in range(0, 2):
                                            K20 = np.array([k20], dtype = np.uint8)
                                            for k23 in range(0, 2):
                                                K23 = np.array([k23], dtype = np.uint8)
                                                for k33 in range(0, 2):
                                                    K33 = np.array([k33], dtype = np.uint8)
                                                    for k34 in range(0, 2):
                                                        K34 = np.array([k34], dtype = np.uint8)
                                                        for k36 in range(0, 2):
                                                            K36 = np.array([k36], dtype = np.uint8)
                                                            for k39 in range(0, 2):
                                                                K39 = np.array([k39], dtype = np.uint8)
                                                                for k57 in range(0, 2):
                                                                    K57 = np.array([k57], dtype = np.uint8)
                                                                    for k58 in range(0, 2):
                                                                        K58 = np.array([k58], dtype = np.uint8)
                                                                        for k60 in range(0, 2):
                                                                            K60 = np.array([k60], dtype = np.uint8)
                                                                            for k63 in range(0, 2):
                                                                                K63 = np.array([k63], dtype = np.uint8)
                                                                                Z0 = Nand(Xor(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(K60, K58), Nand(K36, K34))), Xor(Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                                Z1 = Nand(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                                Z2 = Nand(Xor(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Xor(Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                                Z3 = Nand(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                                Z4 = Nand(Xor(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                                Z5 = Nand(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                                Z6 = Nand(Xor(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                                Z7 = Nand(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                                Z8 = Xor(Nand(Xor(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(K60, K58), Nand(K36, K34))), Xor(Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))), Nand(Nand(K20, K18), Nand(K12, K10)))), Xor(Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                                Z9 = Xor(Nand(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10)))), Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                                Z10 = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Xor(Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)))), Xor(Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                                Z11 = Xor(Nand(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)))), Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                                Z12 = Xor(Nand(Xor(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10)))), Xor(Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                                Z13 = Xor(Nand(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10)))), Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                                Z14 = Xor(Nand(Xor(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10)))), Xor(Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                                Z15 = Xor(Nand(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10)))), Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                                X = np.concatenate((Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15))
                                                                                Delta = Xor(X, rk4Sec)
                                                                                if max(Delta) == 0:
                                                                                    mkSec[0] = k9
                                                                                    mkSec[1] = k10
                                                                                    mkSec[2] = k12
                                                                                    mkSec[3] = k15
                                                                                    mkSec[4] = k17
                                                                                    mkSec[5] = k18
                                                                                    mkSec[6] = k20
                                                                                    mkSec[7] = k23
                                                                                    mkSec[8] = k33
                                                                                    mkSec[9] = k34
                                                                                    mkSec[10] = k36
                                                                                    mkSec[11] = k39
                                                                                    mkSec[12] = k57
                                                                                    mkSec[13] = k58
                                                                                    mkSec[14] = k60
                                                                                    mkSec[15] = k63
                                                                                    mkList.append(mkSec.copy())
                                                                                else:
                                                                                    continue
            else:
                ctr = 0
                for k8 in range(0, 2):
                    K8 = np.array([k8], dtype = np.uint8)
                    for k11 in range(0, 2):
                        K11 = np.array([k11], dtype = np.uint8)
                        for k13 in range(0, 2):
                            K13 = np.array([k13], dtype = np.uint8)
                            for k14 in range(0, 2):
                                K14 = np.array([k14], dtype = np.uint8)
                                for k16 in range(0, 2):
                                    K16 = np.array([k16], dtype = np.uint8)
                                    for k19 in range(0, 2):
                                        K19 = np.array([k19], dtype = np.uint8)
                                        for k21 in range(0, 2):
                                            K21 = np.array([k21], dtype = np.uint8)
                                            for k22 in range(0, 2):
                                                K22 = np.array([k22], dtype = np.uint8)
                                                for k32 in range(0, 2):
                                                    K32 = np.array([k32], dtype = np.uint8)
                                                    for k35 in range(0, 2):
                                                        K35 = np.array([k35], dtype = np.uint8)
                                                        for k37 in range(0, 2):
                                                            K37 = np.array([k37], dtype = np.uint8)
                                                            for k38 in range(0, 2):
                                                                K38 = np.array([k38], dtype = np.uint8)
                                                                for k56 in range(0, 2):
                                                                    K56 = np.array([k56], dtype = np.uint8)
                                                                    for k59 in range(0, 2):
                                                                        K59 = np.array([k59], dtype = np.uint8)
                                                                        for k61 in range(0, 2):
                                                                            K61 = np.array([k61], dtype = np.uint8)
                                                                            for k62 in range(0, 2):
                                                                                K62 = np.array([k62], dtype = np.uint8)
                                                                                Z0 = Nand(Xor(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(K61, K59), Nand(K37, K35))), Xor(Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                                Z1 = Nand(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                                Z2 = Nand(Xor(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Xor(Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                                Z3 = Nand(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                                Z4 = Nand(Xor(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), One), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                                Z5 = Nand(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), One), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                                Z6 = Nand(Xor(Xor(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), One), Xor(Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))))
                                                                                Z7 = Nand(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))))
                                                                                Z8 = Xor(Nand(Xor(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(K61, K59), Nand(K37, K35))), Xor(Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))), Nand(Nand(K21, K19), Nand(K13, K11)))), Xor(Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                                Z9 = Xor(Nand(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11)))), Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                                Z10 = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Xor(Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)))), Xor(Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                                Z11 = Xor(Nand(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)))), Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                                Z12 = Xor(Nand(Xor(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), One), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11)))), Xor(Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                                Z13 = Xor(Nand(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), One), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11)))), Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                                Z14 = Xor(Xor(Nand(Xor(Xor(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), One), Xor(Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), Xor(Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), One)
                                                                                Z15 = Xor(Xor(Nand(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), One)
                                                                                X = np.concatenate((Z0, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15))
                                                                                Delta = Xor(X, rk4Sec)
                                                                                if max(Delta) == 0:
                                                                                    mkSec[0] = k8
                                                                                    mkSec[1] = k11
                                                                                    mkSec[2] = k13
                                                                                    mkSec[3] = k14
                                                                                    mkSec[4] = k16
                                                                                    mkSec[5] = k19
                                                                                    mkSec[6] = k21
                                                                                    mkSec[7] = k22
                                                                                    mkSec[8] = k32
                                                                                    mkSec[9] = k35
                                                                                    mkSec[10] = k37
                                                                                    mkSec[11] = k38
                                                                                    mkSec[12] = k56
                                                                                    mkSec[13] = k59
                                                                                    mkSec[14] = k61
                                                                                    mkSec[15] = k62
                                                                                    mkList.append(mkSec.copy())
                                                                                else:
                                                                                    continue
            return mkList

    except ValueError as e1:
        print(f"Invalid input type. {e1}")

    except TypeError as e2:
        print(f"Invalid input size or value. {e2}")



###################################################################################################
####                                        Brute-force                                        ####
###################################################################################################
def BruteForce(Address: str, nominatedRK4: list) -> np.uint8:
    try:
        if nominatedRK4.type != list or type(Address) != str:
            raise TypeError("The first input must be a string and the second one must be a list of 64-bit keys.")
        elif nominatedRK4 == []:
            raise ValueError("Input list is empty.")
        else:
            progressFlag = True
            Len = len(nominatedRK4)
            plaintextAddress = Address + "\\Plaintext.txt"
            ciphertextAddress = Address + "\\Ciphertext.txt"
            P = ReadBlock(plaintextAddress)
            C = ReadBlock(ciphertextAddress)
            for i in range(0, Len):
                rk4Parts = DetachKey(nominatedRK4[i])
                MK1 = MK_Matching(rk4Parts[0], 1)
                Len1 = len(MK1)
                MK2 = MK_Matching(rk4Parts[1], 2)
                Len2 = len(MK2)
                MK3 = MK_Matching(rk4Parts[2], 3)
                Len3 = len(MK3)
                MK4 = MK_Matching(rk4Parts[3], 4)
                Len4 = len(MK4)
                keyRecFlag = False
                for j in range(0, Len1):
                    for l in range(0, Len2):
                        ctr =+ 1
                        y = 100 * ctr / (Len * Len1 * Len2)
                        if abs(y - round(y, 3)) < 0.0005 and progressFlag == True:
                            print(f"HDLBC cryptanalysis: {round(y, 3)}% of the brute-force has been completed.")
                            progressFlag = False
                        elif abs(y - round(y, 3)) >= 0.0005:
                            progressFlag = True
                        for m in range(0, Len3):
                            for n in range(0, Len4):
                                MK = MKMergeKey(MK1[j], MK1[j], MK1[j], MK1[j])
                                cHat = HDLBC.Encrypt(P, MK)
                                Delta = Xor(cHat, C)
                                if max(Delta) == 0:
                                    mkHat = MK.copy()
                                    keyRecFlag = True
                                    break
                        break
                    break
                break
            if keyRecFlag == False:
                mkHat = []
                print("Cryptanalysis is Failed!")

            return mkHat.astype(np.uint8)

    except ValueError as e1:
        print(f"Input Error: {e1}")

    except TypeError as e2:
        print(f"Input Error: {e2}")
