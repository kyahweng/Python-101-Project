import random


yourHand = None

randomHand = None


while True:
    
    yourHand = input("Rock, Paper or Scissor?")
    randomHand = random.choice(['Rock', 'Paper', 'Scissors'])
    print(f"Computer's hand is {randomHand}")

    if yourHand.lower() == randomHand.lower():
        print(f"You both chose {yourHand}. Play again")
        continue

    elif yourHand.lower() == 'rock' and randomHand.lower() == 'scissors':
        print(f"You win! {yourHand} wins over {randomHand}!")
        break
    elif yourHand.lower() == 'scissors' and randomHand.lower() == 'paper':
        print(f"You win! {yourHand} wins over {randomHand}!")
        break
    elif yourHand.lower() == 'paper' and randomHand.lower() == 'rock':
        print(f"You win! {yourHand} wins over {randomHand}!")
        break
   
    else:
        print("You lose! Choose again")
        continue
    





    
    
   
