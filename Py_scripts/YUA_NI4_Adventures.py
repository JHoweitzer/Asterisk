# The library of individual adventures on YUA_NI4
# WARNING! MAJOR SPOILERS AHEAD!
# The overview of the planet, given to the player on arrival

from _utilities import clear
from _utilities import printHelp

planetIntro1 = """
Your pod rattles and groans as it pierces the icey-blue atmosphere.
Golden heat flickers around the thick glass windows. You grip your harness.
Through the glowing glass a green horizon stretches before you, long and dark 
like a beer bottle; though you can't ever remember having beer yourself.
"""
planetIntro2 = """
Your stomach lurches as engines kick in to slow your descent. Clumsily, you 
break through the canopy, greeted by snappings and rumblings of foliage outside.
The natural light that once filled your ship dims, leaving just the gentle glow
of your ship's display unit. 

Your ship slows to a hover over a thick round branch of a colossal tree, 
and awkwardly drop to the surface with a loud thunk. The dull hum of your ship
slowly silences.
"""
planetIntro3 = r"""
You unclasp your harness and tap the wide rectangular screen on your wrist.
It begins to glow orange, your only companion in this universe stirs awake slowly.
... Loading ...
... Loading ...
... Loading ...
 ___    __    _     ____ 
| | \  / /\  | |   | |_  
|_|_/ /_/--\ |_|__ |_|__ 

And a chipper voice greets you - "HOWDY BUD!"
"""
planetIntro4 = """
"LOOKIN GOOD! Where are we? OH! This planet is NEAT! You'll be able to breathe the
atmosphere no problem. Well. Unless you're worried about bacteria in the air. Your
immune system kinda sucks; you know that? Should've played outside more as a kid. 
Keep your helmet on to be safe. OH ALSO! The surface of this planet is a nightmare.
Dark. Wet. Try to stay out of it ok? I mean I'm not the boss of you HAHA. Unless?
NAH I'm just kiddin. But really listen to me. Don't forget your Blaster!"

You've missed DALE. You grab your Blaster, adjust your helmet, and crank the door handle.
The outside atmosphere rushes in, and you push the door wide and step onto the firm grey
surface of the tree trunk.
"""

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

def ex_00(player):
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
