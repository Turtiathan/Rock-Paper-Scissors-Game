import random

def rock_paper_scissors():
	"""
	This function implements the rock paper scissors game.
	"""
	choices = ("rock", "paper", "scissors")

	print("Hello and welcome to game of rock paper scissors.")
	while True:
		player_input = raw_input("Please choose rock, paper, or scissors. Enter 'r' for rock, 'p' for paper, and 's' for scissors.")

		if player_input == 'r' or player_input == 'R':
			player_choice = choices[0]
		elif player_input == 'p' or player_input == 'P':
			player_choice = choices[1]
		elif player_input == 's' or player_input == 'S':
			player_choice = choices[2]
		else:
			print("You entered an invalid value.")
			continue

		computer_choice = choices[random.randint(0,3)-1]

		if player_choice == computer_choice:
			print("Both the computer and you picked " + player_choice + ". It was a tie.")
		elif player_choice == "rock" and computer_choice == "paper":
			print("You picked " + player_choice + ". The computer picked " + computer_choice + ". The computer wins.")
		elif player_choice == "rock" and computer_choice == "scissors":
			print("You picked " + player_choice + ". The computer picked " + computer_choice + ". You win.")
		elif player_choice == "paper" and computer_choice == "scissors":
			print("You picked " + player_choice + ". The computer picked " + computer_choice + ". The computer wins.")
		elif player_choice == "paper" and computer_choice == "rock":
			print("You picked " + player_choice + ". The computer picked " + computer_choice + ". You win.")
		elif player_choice == "scissors" and computer_choice == "rock":
			print("You picked " + player_choice + ". The computer picked " + computer_choice + ". The computer wins.")
		elif player_choice == "scissors" and computer_choice == "paper":
			print("You picked " + player_choice + ". The computer picked " + computer_choice + ". You win.")

		playAgain = raw_input("Do you want to play again? Enter 'n' to end the game. Otherwise enter anything to continue playing.")

		if playAgain == "n" or playAgain == "N":
			break

rock_paper_scissors()


