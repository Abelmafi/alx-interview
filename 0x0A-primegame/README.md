# Prime Number Game

This is a Python program that simulates a game between two players, Maria and Ben. The game involves choosing prime numbers from a set of consecutive integers and removing the chosen number and its multiples from the set. The player who cannot make a move loses the game. The program determines the winner of each game based on the given rounds.

## Usage

The program is implemented in the `isWinner(x, nums)` function, where `x` is the number of rounds and `nums` is an array of `n` values for each round. The function returns the name of the player that won the most rounds. If the winner cannot be determined, `None` is returned.

To use the program, follow these steps:

1. Install Python (version 3 or above) on your machine.
2. Copy the code from `prime_number_game.py` into a new Python file or an interactive Python environment.
3. Call the `isWinner` function with the desired number of rounds and `n` values.
4. The function will return the name of the player with the most wins or `None` if the winner cannot be determined.

```python
x = 3
nums = [4, 5, 1]
winner = isWinner(x, nums)
print(winner)  # Output: Maria

Constraints

    The number of rounds (x) and the n values should not exceed 10,000.
    The program does not require any external packages or libraries.

Contributing

Contributions to the Prime Number Game project are welcome! If you find any issues or would like to suggest improvements, please feel free to open an issue or submit a pull request.
License

The Prime Number Game project is licensed under the MIT License.

javascript


Please note that this `README.md` file assumes the presence of a `prime_number_game.py` file containing the implementation of the `isWinner` function. Adjust the file names accordingly based on your project structure.

