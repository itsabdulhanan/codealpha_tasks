# =============================
# Hangman Game
# =============================
import random

# Predefined words (as per task requirement)
word_list = ["python", "computer", "hangman", "programming", "university", "codealpha"]

# ASCII stages of Hangman
stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    =========
    """
]

def display_hangman(attempts_left):
    """Return the hangman stage based on the attempts left."""
    return stages[6 - attempts_left]

def play_hangman():
    """Play one round of Hangman. Return True if win, False if loss."""
    print("\n Welcome to Hangman!")

    # Select a random word from the list
    word = random.choice(word_list)

    # Setup game variables
    guessed_word = ["_"] * len(word)   # word display with underscores
    guessed_letters = []               # track guessed letters
    attempts_left = 6                  # max 6 wrong guesses

    # Game loop
    while attempts_left > 0 and "_" in guessed_word:
        # Display current game state
        print("\n" + display_hangman(attempts_left))
        print("Word: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Take user input
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print(" You already guessed that letter!")
            continue

        # Add guess to guessed letters
        guessed_letters.append(guess)

        # Check if guess is in the word
        if guess in word:
            print(" Good job! The letter is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(" Wrong guess!")
            attempts_left -= 1

    # End of Game
    print("\n" + display_hangman(attempts_left))
    if "_" not in guessed_word:
        print("Final word: " + " ".join(guessed_word))
        print(f" Congratulations! You guessed the word: {word}")
        return True   # WIN
    else:
        print("💀 Game Over! The word was: " + word)
        print(" Your progress: " + " ".join(guessed_word))
        return False  # LOSS

def hangman():
    """Main game loop with replay and scoring."""
    wins, losses = 0, 0

    while True:
        result = play_hangman()
        if result:
            wins += 1
        else:
            losses += 1

        # Show current score
        print(f"\n Current Score → Wins: {wins} | Losses: {losses}")

        # Ask if player wants to play again
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != "y":
            print("\n Thanks for playing Hangman!")
            print(f" Final Score → Wins: {wins} | Losses: {losses}")
            print("Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    hangman()
