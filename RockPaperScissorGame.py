import random

def get_choices():
  player_choice=input("Enter your choice as (rock, paper, scissors): ")
  options=["rock", "paper", "scissors"]
  computer_choice=random.choice(options)
  choices={"player":player_choice, "computer":computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player==computer:
    return "It's a tie!"
  elif player=="rock":
    if computer=="scissors":
      return "Rock smashes Scissors! You win!"
    else:
      return "Paper covers rock! You loose."
  elif player=="paper":
    if computer=="rock":
      return "Paper covers rock! You Win!"
    else:
      return "Scissors cut paper! You loose."
  elif player=="scissors":
    if computer=="paper":
      return "Scissors cut paper!You win!"
    else:
      return "Rock smashes scissors you loose."

choices=get_choices()
result=check_win(choices["player"], choices["computer"])
print(result)
