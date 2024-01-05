# Treasure Island Adventure

Welcome to **Treasure Island**, a text-based adventure game where your mission is to find the hidden treasure. Explore the island, make choices, and see if you have what it takes to claim the prize.

## Instructions

1. **Starting Point**
   - You start at a crossroad. Choose your direction wisely.

    ```python
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" \n')
    ```

2. **Left or Right**
   - If you choose the left path, you'll encounter a lake. Decide whether to wait for a boat or swim across.

    ```python
    if choice1.lower() == 'left':
        choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n')
    ```

3. **Lake Crossing**
   - Depending on your choice, the story unfolds differently. If you wait, you'll enter a castle with multiple colored doors.

    ```python
    if choice2.lower() == 'wait':
        choice3 = input('You\'ve come inside a castle. There are multiple doors inside the castle. Type "Red" to go inside the Red color door. Type "Yellow" to go inside the Yellow color door. Type "Blue" to go inside the Blue color door. \n')
    ```

4. **Door Choices**
   - Your fate depends on the color of the door you choose. Make your decision wisely.

    ```python
    if choice3.lower() == 'red':
        print("You are burned by fire. Game over!")
    elif choice3.lower() == 'yellow':
        print("Congratulations! You successfully hunted the treasure. You win!")
    elif choice3.lower() == 'blue':
        print("You are eaten by beasts. Game over!")
    else:
        print("Game over! You chose the wrong door.")
    ```

5. **Alternate Endings**
   - Depending on your choices, you may face different outcomes. Will you find the treasure, or will your adventure end in defeat?

    ```python
    else:
        print("You are attacked by trout. Game over!")
    ```

    ```python
    else:
        print("You fell into a hole. Game over!")
    ```

Feel free to play the game and discover the various paths and endings. Good luck, adventurer!

## Requirements

- Python 3.x

## Contributors

- Ghufran Ahmed

Feel free to contribute to the project by [opening an issue](https://github.com/Parfowhat/Plus-W_UOK-Data-Science-/issues) or submitting a pull request.
