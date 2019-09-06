# The library of individual adventures on YUA_NI4
# WARNING! MAJOR SPOILERS AHEAD!

def ex_00(player):
    """
    THE CHASM
    """ 
    return True

def ex_10(player):
    return True

def ex_20(player):
    return True

def ex_30(player):
    return True

def ex_01(player):
    return True

def ex_11(player):
    return True

def ex_21(player):
    return True

def ex_31(player):
    return True

def ex_02(player):
    return True

def ex_12(player):
    return True

def ex_22(player):
    """
    THE LANDING SITE. Currently used as a test function
    """
    # TEMPORARY LOOP
    player.injuries.remove("Mild Headache")
    player.inventory.append("A sense of satisfaction")
    cont = input("The landing site. Type CONTINUE to move on. Type anything else to leave the game: ")
    while cont != "CONTINUE":
        return False

    return True

def ex_32(player):
    return True

def ex_03(player):
    return True

def ex_13(player):
    return True

def ex_23(player):
    return True

def ex_33(player):
    return True
