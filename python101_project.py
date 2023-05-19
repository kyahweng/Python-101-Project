import random


yourHand = None

randomHand = None


while True:
    
    yourHand = input("Rock, Paper or Scissor?")
    randomHand = random.choice(['Rock', 'Paper', 'Scissors'])
   

    if yourHand.lower() == randomHand.lower():
        print(f"Play again! You both chose {yourHand}.  ('Q' to Quit)")

        continue

    elif yourHand.lower() != 'rock'and yourHand.lower() != 'scissors'and yourHand.lower() != 'paper'and yourHand.lower() != "q":
        print("Please enter the correct option")
        continue

    elif yourHand.lower() == 'rock' and randomHand.lower() == 'scissors':
        print(f"Computer's hand is {randomHand}")
        print(f"You win! {yourHand} wins over {randomHand}!")
        break
    elif yourHand.lower() == 'scissors' and randomHand.lower() == 'paper':
        print(f"Computer's hand is {randomHand}")
        print(f"You win! {yourHand} wins over {randomHand}!")
        break
    elif yourHand.lower() == 'paper' and randomHand.lower() == 'rock':
        print(f"Computer's hand is {randomHand}")
        print(f"You win! {yourHand} wins over {randomHand}!")
        break

    

    elif yourHand.lower() == "q":
        print('Thank you for playing')
        break
   
    else:
        print('You lose! Choose again ("Q" to Quit)')
        continue
    



#print(f"You win! {yourHand} wins over {randomHand}!")

    
    
   
