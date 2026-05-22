import numpy as np
from Basic import Int2Bin, Nand, Xor, Bin2Int

###################################################################################################
####                        Check the existance of an integer in a list                        ####
###################################################################################################
def ExFlagChecker(M: list, n: int) -> bool:
    try:
        if type(M) != list or type(n) != int:
            raise TypeError("The first input must be a list and the scond one must be a non-negative integer.")
        elif n <0 or n > 65535:
            raise ValueError("The second input is not between 0 and 65535.")
        else:
            Len = len(M)
            exFlag = False
            for i in range(0, Len):
                if M[i] == n:
                    exFlag = True
                    break
                else:
                    continue
            return exFlag

    except TypeError as e1:
        print(f"Input-type Error: {e1}")

    except ValueError as e2:
        print(f"Input-value Error: {e2}")

###################################################################################################
####                                 Create the keyspace files                                 ####
###################################################################################################
def Calculator() -> None:
    Address = input("Please enetr the valid directory: \n")
    while ord(Address[0]) > 47 and ord(Address[0]) < 58:
        print("Input is not valid. Please enter the valid address.")
        Address = input("Please enetr the valid directory: \n")
    part1Address = Address + "\\RK4_0-3_8-11_32-35_40-43.txt"
    part2Address = Address + "\\RK4_4-7_12-15_36-39_44-47.txt"
    part3Address = Address + "\\RK4_16-19_24-27_48-51_56-59.txt"
    part4Address = Address + "\\RK4_20-23_28-31_52-55_60-63.txt"
    RK4 = np.zeros(64, dtype = np.uint8)
    M = []
    Vector = []
    ctr = 0
    ctr2 = 0
    Flag = False
    with open(part1Address, "w") as f:
        f.write(f"RK4[0,1,2,3,8,9,10,11,32,33,34,35,40,41,42,43]:\n")
        for K1 in range(0, 2):
            for K2 in range(0, 2):
                for K4 in range(0, 2):
                    for K7 in range(0, 2):
                        for K25 in range(0, 2):
                            for K26 in range(0, 2):
                                for K28 in range(0, 2):
                                    for K31 in range(0, 2):
                                        for K41 in range(0, 2):
                                            for K42 in range(0, 2):
                                                for K44 in range(0, 2):
                                                    for K47 in range(0, 2):
                                                        for K49 in range(0, 2):
                                                            for K50 in range(0, 2):
                                                                for K52 in range(0, 2):
                                                                    for K55 in range(0, 2):
                                                                        RK4[0] = Nand(Xor(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(K28, K26), Nand(K4, K2))), Xor(Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                        RK4[1] = Nand(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                        RK4[2] = Nand(Xor(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Xor(Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                        RK4[3] = Nand(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                        RK4[8] = Nand(Xor(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                        RK4[9] = Nand(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                        RK4[10] = Nand(Xor(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                        RK4[11] = Nand(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                        RK4[32] = Xor(Nand(Xor(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(K28, K26), Nand(K4, K2))), Xor(Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))), Nand(Nand(K52, K50), Nand(K44, K42)))), Xor(Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                        RK4[33] = Xor(Nand(Nand(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(Nand(K28, K26), Nand(K4, K2))), Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42)))), Nand(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(Nand(K52, K50), Nand(K44, K42))))
                                                                        RK4[34] = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Xor(Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)))), Xor(Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                        RK4[35] = Xor(Nand(Nand(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2))), Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)))), Nand(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42))))
                                                                        RK4[40] = Xor(Nand(Xor(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Xor(Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42)))), Xor(Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                        RK4[41] = Xor(Nand(Nand(Xor(Nand(Nand(K31, K25), Nand(K7, K1)), Nand(K7, K1)), Xor(Nand(Nand(K28, K26), Nand(K4, K2)), Nand(K4, K2))), Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42)))), Nand(Xor(Nand(Nand(K55, K49), Nand(K47, K41)), Nand(K47, K41)), Xor(Nand(Nand(K52, K50), Nand(K44, K42)), Nand(K44, K42))))
                                                                        RK4[42] = Xor(Nand(Xor(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Xor(Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42)))), Xor(Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                        RK4[43] = Xor(Nand(Nand(Xor(Nand(Xor(Nand(K31, K25), K25), Xor(Nand(K7, K1), K1)), Xor(Nand(K7, K1), K1)), Xor(Nand(Xor(Nand(K28, K26), K26), Xor(Nand(K4, K2), K2)), Xor(Nand(K4, K2), K2))), Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42)))), Nand(Xor(Nand(Xor(Nand(K55, K49), K49), Xor(Nand(K47, K41), K41)), Xor(Nand(K47, K41), K41)), Xor(Nand(Xor(Nand(K52, K50), K50), Xor(Nand(K44, K42), K42)), Xor(Nand(K44, K42), K42))))
                                                                        ctr += 1
                                                                        y = (25 * ctr) / 65536
                                                                        if abs(y - round(y, 2)) < 0.0005:
                                                                            if Flag == False:
                                                                                print(f"{round(y, 2)}% of the entropy checking has been completed.")
                                                                                Flag = True
                                                                        else:
                                                                            Flag = False
                                                                        A = np.concatenate((RK4[0:4], RK4[8:12], RK4[32:36],RK4[40:44]))
                                                                        numK = Bin2Int(A)
                                                                        exFlag = ExFlagChecker(M, numK)
                                                                        if exFlag== False:
                                                                            M.append(numK)
                                                                            B = Int2Bin(numK)
                                                                            Vector.append(B)
                                                                            f.write(f"{ctr2}: {Vector[ctr2]}\n")
                                                                            ctr2 += 1
                                                                        else:
                                                                            continue
    f.close()
    M = []
    Vector = []
    Flag = False
    ctr = 0
    ctr2 = 0
    with open(part2Address, "w") as f:
        f.write(f"RK4[4,5,6,7,12,13,14,15,36,37,38,39,44,45,46,47]:\n")
        for K0 in range(0, 2):
            for K3 in range(0, 2):
                for K5 in range(0, 2):
                    for K6 in range(0, 2):
                        for K24 in range(0, 2):
                            for K27 in range(0, 2):
                                for K29 in range(0, 2):
                                    for K30 in range(0, 2):
                                        for K40 in range(0, 2):
                                            for K43 in range(0, 2):
                                                for K45 in range(0, 2):
                                                    for K46 in range(0, 2):
                                                        for K48 in range(0, 2):
                                                            for K51 in range(0, 2):
                                                                for K53 in range(0, 2):
                                                                    for K54 in range(0, 2):
                                                                        RK4[4] = Nand(Xor(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(K29, K27), Nand(K5, K3))), Xor(Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                        RK4[5] = Nand(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                        RK4[6] = Nand(Xor(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Xor(Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                        RK4[7] = Nand(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                        RK4[12] = Nand(Xor(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                        RK4[13] = Nand(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                        RK4[14] = Nand(Xor(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                        RK4[15] = Nand(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                        RK4[36] = Xor(Nand(Xor(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(K29, K27), Nand(K5, K3))), Xor(Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))), Nand(Nand(K53, K51), Nand(K45, K43)))), Xor(Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                        RK4[37] = Xor(Nand(Nand(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(Nand(K29, K27), Nand(K5, K3))), Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43)))), Nand(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(Nand(K53, K51), Nand(K45, K43))))
                                                                        RK4[38] = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Xor(Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)))), Xor(Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                        RK4[39] = Xor(Nand(Nand(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3))), Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)))), Nand(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43))))
                                                                        RK4[44] = Xor(Nand(Xor(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Xor(Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43)))), Xor(Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                        RK4[45] = Xor(Nand(Nand(Xor(Nand(Nand(K30, K24), Nand(K6, K0)), Nand(K6, K0)), Xor(Nand(Nand(K29, K27), Nand(K5, K3)), Nand(K5, K3))), Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43)))), Nand(Xor(Nand(Nand(K54, K48), Nand(K46, K40)), Nand(K46, K40)), Xor(Nand(Nand(K53, K51), Nand(K45, K43)), Nand(K45, K43))))
                                                                        RK4[46] = Xor(Nand(Xor(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Xor(Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43)))), Xor(Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                        RK4[47] = Xor(Nand(Nand(Xor(Nand(Xor(Nand(K30, K24), K24), Xor(Nand(K6, K0), K0)), Xor(Nand(K6, K0), K0)), Xor(Nand(Xor(Nand(K29, K27), K27), Xor(Nand(K5, K3), K3)), Xor(Nand(K5, K3), K3))), Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43)))), Nand(Xor(Nand(Xor(Nand(K54, K48), K48), Xor(Nand(K46, K40), K40)), Xor(Nand(K46, K40), K40)), Xor(Nand(Xor(Nand(K53, K51), K51), Xor(Nand(K45, K43), K43)), Xor(Nand(K45, K43), K43))))
                                                                        ctr += 1
                                                                        y = (25 * ctr) / 65536
                                                                        if abs(y - round(y, 2)) < 0.0005:
                                                                            if Flag == False:
                                                                                print(f"{round(25 + y, 2)}% of the entropy checking has been completed.")
                                                                                Flag = True
                                                                        else:
                                                                            Flag = False
                                                                        A = np.concatenate((RK4[4:8], RK4[12:16], RK4[36:40],RK4[44:48]))
                                                                        numK = Bin2Int(A)
                                                                        exFlag = ExFlagChecker(M, numK)
                                                                        if exFlag== False:
                                                                            M.append(numK)
                                                                            B = Int2Bin(numK)
                                                                            Vector.append(B)
                                                                            f.write(f"{ctr2}: {Vector[ctr2]}\n")
                                                                            ctr2 += 1
                                                                        else:
                                                                            continue
    f.close()
    M = []
    Vector = []
    Flag = False
    ctr = 0
    ctr2 = 0
    with open(part3Address, "w") as f:
        f.write(f"RK4[16, 17, 18, 19, 24, 25, 26, 27, 48, 49, 50, 51, 56, 57, 58, 59]:\n")
        for K9 in range(0, 2):
            for K10 in range(0, 2):
                for K12 in range(0, 2):
                    for K15 in range(0, 2):
                        for K17 in range(0, 2):
                            for K18 in range(0, 2):
                                for K20 in range(0, 2):
                                    for K23 in range(0, 2):
                                        for K33 in range(0, 2):
                                            for K34 in range(0, 2):
                                                for K36 in range(0, 2):
                                                    for K39 in range(0, 2):
                                                        for K57 in range(0, 2):
                                                            for K58 in range(0, 2):
                                                                for K60 in range(0, 2):
                                                                    for K63 in range(0, 2):
                                                                        RK4[16] = Nand(Xor(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(K60, K58), Nand(K36, K34))), Xor(Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                        RK4[17] = Nand(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                        RK4[18] = Nand(Xor(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Xor(Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                        RK4[19] = Nand(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                        RK4[24] = Nand(Xor(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                        RK4[25] = Nand(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                        RK4[26] = Nand(Xor(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                        RK4[27] = Nand(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                        RK4[48] = Xor(Nand(Xor(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(K60, K58), Nand(K36, K34))), Xor(Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))), Nand(Nand(K20, K18), Nand(K12, K10)))), Xor(Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                        RK4[49] = Xor(Nand(Nand(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(Nand(K60, K58), Nand(K36, K34))), Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10)))), Nand(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(Nand(K20, K18), Nand(K12, K10))))
                                                                        RK4[50] = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Xor(Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)))), Xor(Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                        RK4[51] = Xor(Nand(Nand(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34))), Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)))), Nand(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10))))
                                                                        RK4[56] = Xor(Nand(Xor(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Xor(Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10)))), Xor(Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                        RK4[57] = Xor(Nand(Nand(Xor(Nand(Nand(K63, K57), Nand(K39, K33)), Nand(K39, K33)), Xor(Nand(Nand(K60, K58), Nand(K36, K34)), Nand(K36, K34))), Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10)))), Nand(Xor(Nand(Nand(K23, K17), Nand(K15, K9)), Nand(K15, K9)), Xor(Nand(Nand(K20, K18), Nand(K12, K10)), Nand(K12, K10))))
                                                                        RK4[58] = Xor(Nand(Xor(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Xor(Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10)))), Xor(Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                        RK4[59] = Xor(Nand(Nand(Xor(Nand(Xor(Nand(K63, K57), K57), Xor(Nand(K39, K33), K33)), Xor(Nand(K39, K33), K33)), Xor(Nand(Xor(Nand(K60, K58), K58), Xor(Nand(K36, K34), K34)), Xor(Nand(K36, K34), K34))), Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10)))), Nand(Xor(Nand(Xor(Nand(K23, K17), K17), Xor(Nand(K15, K9), K9)), Xor(Nand(K15, K9), K9)), Xor(Nand(Xor(Nand(K20, K18), K18), Xor(Nand(K12, K10), K10)), Xor(Nand(K12, K10), K10))))
                                                                        ctr += 1
                                                                        y = (25 * ctr) / 65536
                                                                        if abs(y - round(y, 2)) < 0.0005:
                                                                            if Flag == False:
                                                                                print(f"{round(50 + y, 2)}% of the entropy checking has been completed.")
                                                                                Flag = True
                                                                        else:
                                                                            Flag = False
                                                                        A = np.concatenate((RK4[16:20], RK4[24:28], RK4[48:52],RK4[56:60]))
                                                                        numK = Bin2Int(A)
                                                                        exFlag = ExFlagChecker(M, numK)
                                                                        if exFlag== False:
                                                                            M.append(numK)
                                                                            B = Int2Bin(numK)
                                                                            Vector.append(B)
                                                                            f.write(f"{ctr2}: {Vector[ctr2]}\n")
                                                                            ctr2 += 1
                                                                        else:
                                                                            continue
    f.close()
    M = []
    Vector = []
    Flag = False
    ctr = 0
    ctr2 = 0
    with open(part4Address, "w") as f:
        f.write(f"RK4[20, 21, 22, 23, 28, 29, 30, 31, 52, 53, 54, 55, 60, 61, 62, 63]:\n")
        for K8 in range(0, 2):
            for K11 in range(0, 2):
                for K13 in range(0, 2):
                    for K14 in range(0, 2):
                        for K16 in range(0, 2):
                            for K19 in range(0, 2):
                                for K21 in range(0, 2):
                                    for K22 in range(0, 2):
                                        for K32 in range(0, 2):
                                            for K35 in range(0, 2):
                                                for K37 in range(0, 2):
                                                    for K38 in range(0, 2):
                                                        for K56 in range(0, 2):
                                                            for K59 in range(0, 2):
                                                                for K61 in range(0, 2):
                                                                    for K62 in range(0, 2):
                                                                        RK4[20] = Nand(Xor(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(K61, K59), Nand(K37, K35))), Xor(Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                        RK4[21] = Nand(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                        RK4[22] = Nand(Xor(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Xor(Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                        RK4[23] = Nand(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                        RK4[28] = Nand(Xor(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), 1), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                        RK4[29] = Nand(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), 1), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                        RK4[30] = Nand(Xor(Xor(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), 1), Xor(Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))))
                                                                        RK4[31] = Nand(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))))
                                                                        RK4[52] = Xor(Nand(Xor(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(K61, K59), Nand(K37, K35))), Xor(Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))), Nand(Nand(K21, K19), Nand(K13, K11)))), Xor(Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                        RK4[53] = Xor(Nand(Nand(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(Nand(K61, K59), Nand(K37, K35))), Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11)))), Nand(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(Nand(K21, K19), Nand(K13, K11))))
                                                                        RK4[54] = Xor(Nand(Xor(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Xor(Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)))), Xor(Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                        RK4[55] = Xor(Nand(Nand(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35))), Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)))), Nand(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11))))
                                                                        RK4[60] = Xor(Nand(Xor(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), 1), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Xor(Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11)))), Xor(Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                        RK4[61] = Xor(Nand(Nand(Xor(Xor(Nand(Nand(K62, K56), Nand(K38, K32)), Nand(K38, K32)), 1), Xor(Nand(Nand(K61, K59), Nand(K37, K35)), Nand(K37, K35))), Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11)))), Nand(Xor(Nand(Nand(K22, K16), Nand(K14, K8)), Nand(K14, K8)), Xor(Nand(Nand(K21, K19), Nand(K13, K11)), Nand(K13, K11))))
                                                                        RK4[62] = Xor(Xor(Nand(Xor(Xor(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), 1), Xor(Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), Xor(Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11))), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), 1)
                                                                        RK4[63] = Xor(Xor(Nand(Nand(Xor(Nand(Xor(Nand(K62, K56), K56), Xor(Nand(K38, K32), K32)), Xor(Nand(K38, K32), K32)), Xor(Nand(Xor(Nand(K61, K59), K59), Xor(Nand(K37, K35), K35)), Xor(Nand(K37, K35), K35))), Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), Nand(Xor(Nand(Xor(Nand(K22, K16), K16), Xor(Nand(K14, K8), K8)), Xor(Nand(K14, K8), K8)), Xor(Nand(Xor(Nand(K21, K19), K19), Xor(Nand(K13, K11), K11)), Xor(Nand(K13, K11), K11)))), 1)
                                                                        ctr += 1
                                                                        y = (25 * ctr) / 65536
                                                                        if abs(y - round(y, 2)) < 0.0005:
                                                                            if Flag == False:
                                                                                print(f"{round(75 + y, 2)}% of the entropy checking has been completed.")
                                                                                Flag = True
                                                                        else:
                                                                            Flag = False
                                                                        A = np.concatenate((RK4[20:24], RK4[28:32], RK4[52:56],RK4[60:64]))
                                                                        numK = Bin2Int(A)
                                                                        exFlag = ExFlagChecker(M, numK)
                                                                        if exFlag== False:
                                                                            M.append(numK)
                                                                            B = Int2Bin(numK)
                                                                            Vector.append(B)
                                                                            f.write(f"{ctr2}: {Vector[ctr2]}\n")
                                                                            ctr2 += 1
                                                                        else:
                                                                            continue
    f.close()

