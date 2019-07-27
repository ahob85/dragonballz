# Constants (usually characters, or other values that will never change).
define n = Character("Nappa")
define v = Character("[player_name]")

# Variables (values that will change during gameplay)
$ player_name = ""
$ power_level = 1050
$ super_saiyan = False

label start:

    scene bg field

    "Welcome to {b}Dragon Ball Z: The Interactive Novel{/b}"

    $ player_name = renpy.input("What's your name?").strip()

    if not player_name:
        $ player_name = "Vegeta"

    "[player_name] and Nappa are facing off against Goku! Nappa is furious!"

    show nappa smiling

    n "[player_name]! What does the scouter say about his POWER LEVEL?!"

    hide nappa

    $ powerLevel = renpy.input("So, what does the scouter say? (Enter value between 0-9999)", allow="0123456789")

    if not powerLevel:
        $ powerLevel = 0

    show vegeta angry

    if powerLevel < 3000:
        jump laugh
    elif powerLevel >= 3000 and powerLevel <= 9000:
        jump fight
    else:
        jump omg

label laugh:

    v "Let's run away!"

    jump ending

label fight:

    v "Let's fight this guy now!"

    jump ending

label omg:

    v "IT'S OVER 9000!"

    jump ending

# This ends the game.

label ending:

    return
