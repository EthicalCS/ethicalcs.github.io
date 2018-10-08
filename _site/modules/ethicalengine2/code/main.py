import sys
from scenario import (
    set_seed,
    Scenario
)
from engine import (
    ruleset1,
    ruleset2,
    ruleset3,
    my_decision
)


def runSimulation(seed):
    print("===========================================")
    print("THE ETHICAL ENGINE")
    print("===========================================")
    print()

    set_seed(seed)
    keepRunning = True
    while keepRunning:
        scene = Scenario()
        print(scene)
        print()
        result = ruleset1(scene)
        # result = ruleset2(scene)
        # result = ruleset3(scene)
        # result = my_decision(scene)
        print()
        input('Hit any key to see decision: ')
        print('I choose to save the', result)
        print()

        # For breaking the loop
        response = input("Hit 'q' to quit or 'enter' to continue: ")
        if response == 'q':
            keepRunning = False

    print('Done')


if __name__ == '__main__':
    seed = 42
    if len(sys.argv) >= 2:
        seed = int(sys.argv[1])
    runSimulation(seed)
