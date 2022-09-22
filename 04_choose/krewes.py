"""
TEAM JAW: William Vongphanith, Abid Talukder, Jonathan Song
SoftDev
K01 -- Choose
2022-09-22

DISCO
___________

QCC
___________

OPS SUMMARY
___________
"""

import random

krewes = {
    2: ["William", "Abid", "Jonathan"],
    7: ["Test user 1", "Test user 2", "Test user 3"],
    8: ["Test user 4", "Test user 5", "Test user 6"],
}

def chooseRandomDevo():
    teamKeyIndex = random.randint(0, len(krewes) - 1)
    teamKey = list(krewes.keys())[teamKeyIndex]
    teamMemberIndex = random.randint(0, len(krewes[teamKey]) - 1)
    teamMember = krewes[teamKey][teamMemberIndex]
    print("Team " + str(teamKey) + ": " + teamMember)

def main():
    chooseRandomDevo()

if __name__ == "__main__":
    main()
