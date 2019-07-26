# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nappa")
define v = Character("Vegeta")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nappa smiling

    # These display lines of dialogue.

    n "Vegeta! What does the scouter say about his POWER LEVEL?!"

    hide nappa smiling
    show vegeta angry

    v "IT'S OVER 9000!"

    # This ends the game.

    return
