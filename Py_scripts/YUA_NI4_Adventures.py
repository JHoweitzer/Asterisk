# The library of individual adventures on YUA_NI4
# WARNING! MAJOR SPOILERS AHEAD!
# The overview of the planet, given to the player on arrival

from _utilities import clear
from _utilities import printHelp
from YUA_NI4_Texts import *

def planetIntro():
    print(planetIntro1)
    input("<Enter to Continue>")
    clear()
    print(planetIntro2)
    input("<Enter to Continue>")
    clear()
    print(planetIntro3)
    input("<Enter to Continue>")
    clear()
    print(planetIntro4)
    input("<Enter to Continue>")
    clear()
    printHelp()
    input("<Enter to Continue>")
    clear()

def exc_00(player):
    print(c00Desc)
    return True

def exc_20(player):
    print(c20Desc)
    return True

def exc_01(player):
    print(c01Desc)
    return True

def exc_11(player):
    print(c11Desc)
    return True

def exc_12(player):
    print(c12Desc)
    return True
    """
    player.inventory.append("A sense of satisfaction")
    cont = input("The landing site. Type DESCEND to go to the mire. ")
    if cont == "DESCEND":
        player.z = 0
        return True
    else:
        print("Did not DESCEND")
        return True
    """

def exc_22(player):
    print(c22Desc)
    return True

def exm_00(player):
    print(m00Desc)
    return True

def exm_10(player):
    print(m10Desc)
    return True

def exm_20(player):
    print(m20Desc)
    return True

def exm_01(player):
    print(m01Desc)
    return True

def exm_11(player):
    print(m11Desc)
    return True

def exm_21(player):
    print(m21Desc)
    return True

def exm_02(player):
    print(m02Desc)
    return True

def exm_12(player):
    print(m12Desc)
    return True

def exm_22(player):
    print(m22Desc)
    return True