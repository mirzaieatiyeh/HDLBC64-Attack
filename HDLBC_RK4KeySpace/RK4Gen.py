import SymbolicBasic as SymBsc
import SymbolicKeySchedule as SymKSch

###################################################################################################
####                    Generating and documenting the HDLBC RK4 equations                     ####
###################################################################################################
def RK4Gen() -> None:
    Address = input("Please enetr the valid directory: \n")
    while ord(Address[0]) > 47 and ord(Address[0]) < 58:
        print("Input is not valid. Please enter the valid address.")
        Address = input("Please enetr the valid directory: \n")
    rk4Address = Address + "\\RK4formula.txt"
    MK = SymBsc.SymMKGen()
    RK1 = SymKSch.KeyUpdate(MK, 0)
    RK2 = SymKSch.KeyUpdate(RK1, 1)
    RK3 = SymKSch.KeyUpdate(RK2, 2)
    RK4 = SymKSch.KeyUpdate(RK3, 3)
    with open(rk4Address, "w") as f:
        for i in range(0, 64):
            f.write(f"RK4[{i}] = {RK4[i]}\n")
    f.close()
    print("The 4th-round key file has been successully generated.")
