# The library of individual adventures on YUA_NI4
# WARNING! MAJOR SPOILERS AHEAD!
# The overview of the planet, given to the player on arrival

from _utilities import clear
from _utilities import printHelp
from _utilities import filterInput
from _dale import dale
from YUA_NI4_Texts import *

class adventures():

    @staticmethod
    def planetIntro():
        print(planetIntro1)
        input("<Enter to Continue>")
        print(planetIntro2)
        input("<Enter to Continue>")
        print(planetIntro3)
        input("<Enter to Continue>")
        print(planetIntro4)
        input("<Enter to Continue>")
        printHelp()
        input("<Enter to Continue>")

    @staticmethod
    def exc_00(player):
        print("Explored canopy 0-0")
        return True

    @staticmethod
    def vc_00(player):
        print(c00Desc)
        return True

    @staticmethod
    def exc_20(player):
        print("Explored canopy 2-0")
        return True

    @staticmethod
    def vc_20(player):
        print(c20Desc)
        return True

    @staticmethod
    def exc_01(player):
        print("Explored canopy 0-1")
        return True

    @staticmethod
    def vc_01(player):
        print(c01Desc)
        return True

    @staticmethod
    def exc_11(player):
        print(c11Expl)
        cont = True
        base = True
        branch = False
        #climbing = False
        #carveSearch = False
        while cont:
            action = input("Exploring area 1-1. Decisions, decisions... ").upper()
            if filterInput(action, "LEAVE", "RETURN", "NOTHING", "STAY", confirmationMessage="NONE"):
                if (base):
                    return True
                else:
                    print("Unable to leave at this moment")
            elif filterInput(action, "JUMP", "LEAP", "BRANCH", "LEFT", confirmationMessage="Jump to the nearby branch?"):
                if (base):
                    print(c11BranchDesc)
                    base = False
                    branch = True
                elif (branch):
                    print("After a moment of hesitation, you jump back to your original branch.")
                    base = True
                    branch = False
            elif filterInput(action, "BEETLE", "BUG", "FOLLOW", "CHASE", confirmationMessage="NONE"):
                if (base):
                    print("The beetle marches across the branch to your left. The branch is thin, but close enough to jump to.")
                elif (branch):
                    print("Chase that beetle!")
            else:
                print("Please try again, or type LEAVE to stop exploring this area (if possible).\n")
            
        return True

    @staticmethod
    def vc_11(player):
        print(c11Desc)
        return True

    @staticmethod
    def exc_12(player):
        print(c12Desc)
        return True

    @staticmethod
    def vc_12(player):
        print("\nType EXPLORE to learn about the landing site \n")
        return True

    @staticmethod
    def exc_22(player):
        print(c22Expl)

        cont = True
        while cont:
            action = input("Exploring area 2-2. Decisions, decisions... ").upper()
            # Drop into the mire
            if filterInput(action, "JUMP", "DROP", "DIVE", "FALL", "LEAP", confirmationMessage="Drop into the mire?"):
                print(c22Drop)
                player.z = 0
                input("<Enter to Continue>")
                print(c22Drop2)
                input("<Enter to Continue>")
                print(m22Desc)
                player.visited.append((player.x, player.y, player.z))
                return True
            # Leave
            elif filterInput(action, "LEAVE", "RETURN", "NOTHING", "STAY", confirmationMessage="NONE"):
                return True
            else:
                print("Please try again, or type LEAVE to stop exploring this area.\n")

    @staticmethod
    def vc_22(player):
        print(c22Desc)
        return True

    #------------ MIRE ------------#

    @staticmethod
    def exm_00(player):
        print("Explored Mire 0-0")
        return True

    @staticmethod
    def vm_00(player):
        print(m00Desc)
        return True

    @staticmethod
    def exm_10(player):
        print("Explored Mire 1-0")
        return True

    @staticmethod
    def vm_10(player):
        print(m10Desc)
        return True

    @staticmethod
    def exm_20(player):
        print("Explored Mire 2-0")
        return True

    @staticmethod
    def vm_20(player):
        print(m20Desc)
        return True

    @staticmethod
    def exm_01(player):
        print("Explored Mire 0-1")
        return True

    @staticmethod
    def vm_01(player):
        print(m01Desc)
        return True

    @staticmethod
    def exm_11(player):
        print("Explored Mire 1-1")
        return True

    @staticmethod
    def vm_11(player):
        print(m11Desc)
        return True

    @staticmethod
    def exm_21(player):
        print("Explored Mire 2-1")
        return True

    @staticmethod
    def vm_21(player):
        print(m21Desc)
        return True

    @staticmethod
    def exm_02(player):
        print("Explored Mire 0-2")
        return True

    @staticmethod
    def vm_02(player):
        print(m02Desc)
        return True

    @staticmethod
    def exm_12(player):
        print("Explored Mire 1-2")
        return True

    @staticmethod
    def vm_12(player):
        print(m12Desc)
        return True

    @staticmethod
    def exm_22(player):
        print("Explored Mire 2-2")
        return True

    @staticmethod
    def vm_22(player):
        print(m22Desc)
        return True