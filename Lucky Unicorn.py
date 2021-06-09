from random import choice
prize_money = 0
print('''

 ("<<<<<<<<<<Lucky Unicorn Game>>>>>>>>>>>>>> \n")
''')

valid = False
while not valid:
    try:
        dollars = int(input("How much would you like to put in today \n"  ))
        if 0 < dollars <= 10:
            valid = True
        else:
            print("please enter a whole number between 1-10\n")

    except ValueError:
        print("please enter a whole number between 1-10\n")
        print("finish program")

    
   
tokens = []
horse_num=500
zebra_num=499
donkey_num=1000
unicorn_num=50

for i in range(horse_num):
    tokens.append("horse")

for i in range(zebra_num):
    tokens.append("zebra")

for i in range(donkey_num):
    tokens.append("donkey")

for i in range(unicorn_num):
    tokens.append("unicorn")

while dollars > 0:
    dollars -= 1
    token =choice(tokens)
    rewards = {'horse': 0.5,
                'zebra': 0.5,
                'donkey': 0,
                'unicorn': 5}


    reward = rewards[token]

    if token == 'horse' or 'zebra':
        print (f"congradulations you got a {token} \n you win ${reward} as a prize")

    if token == 'donkey':
        print(f"uh oh you lost")

    if token == 'unicorn':
        print(f" <<<JACKPOT>>> you got a {token} \n you win ${reward} as a prize")

    prize_money += reward
    print(f"Your current winnings: ${prize_money}, money left {dollars}")
    replay= int(input("Press enter to play again \n Type exit to cash out \n"))
    if replay == 'exit' or dollars <0:
        print("you've run out of turns. Please come back later")
        break

print (f"Here are your winnings of ${prize_money + dollars}. \n See yhou next time.")
