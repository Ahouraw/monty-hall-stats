import random, time

# set the number of iterations
ITERATIONS = 1_000_000

# seeding
random.seed(time.time())

def main():
    #set up the possible outcomes of the game
    outcomes = {"switched_won": 0, "not_switched_won": 0, "switched_lost": 0, "not_switched_lost": 0}

    # run the simulation 10,000 times
    for _ in range(ITERATIONS):
        # randomly choose to switch or not
        switch = random.choice([True, False])

        # run the Monty Hall simulation
        won = monty_hall(switch)

        if won and switch == True:
            outcomes["switched_won"] += 1
        elif won and switch == False:
            outcomes["not_switched_won"] += 1
        elif not won and switch == True:
            outcomes["switched_lost"] += 1
        elif not won and switch == False:
            outcomes["not_switched_lost"] += 1
        else:
            raise ValueError("Unexpected outcome in the Monty Hall simulation.")
        
    for outcome in outcomes:
        print(f"{outcome}: {outcomes[outcome]} times || {(outcomes[outcome] / ITERATIONS) * 100}%")


def monty_hall(switch: bool) -> bool:
    # initialize colors
    red = "🔴"
    green = "🟢"
    blue = "🔵"

    # make a list to be able to use random.choice
    colors = [red, green, blue]

    # randomly choose a color for the prize
    prize = random.choice(colors)
    
    # randomly simulate a user's choice
    choice = random.choice(colors)

    # populate a list of empty colors
    busts = [color for color in colors if color != prize]

    # choose a color to reveal a bust
    while True:
        reveal = random.choice(busts)
        if reveal != choice:
            break

    # remove the revealed color from the options
    busts.remove(reveal)
    colors.remove(reveal)

    if switch == True:
        for color in colors:
            if color != choice:
                choice = color
                break

    # check if the user's choice is the prize
    return choice == prize


if __name__ == "__main__":
    main()