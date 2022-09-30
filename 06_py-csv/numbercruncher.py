"""
Hui Wang, William Vongphanith
Softdev
K06 -- StI/O: Divine your Destiny!
2022-09-29
Time Spent: 0.3 hour
"""

"""
DISCO:
    - The csv module is very useful for reading csv files (when you don't want to parse them yourself)
    - You can use the csv.DictReader() function to read a csv file into a dictionary (instead of a list of lists)
    
QCC:
    - Can you use the csv module to write to a csv file from a dictionary?
    
OPS SUMMARY:
    - We used the csv module to read the csv file
    - We used the random module to generate a random number
    - We used the random number to select a job from the csv file
    - We printed the job
"""

import csv
import random

def main():
    with open('occupations.csv', newline='') as csvfile:
        # read that dict
        reader = csv.DictReader(csvfile)
        # jobs list
        jobs = []
        # for each job
        for row in reader:
            if row['Job Class'] != 'Total':
                # add the job to the list percentage x 10 times (weighting to the first decimal place)
                for i in range(int(float(row['Percentage']) * 10)):
                    # add the job to the list
                    jobs.append(row['Job Class'])
        # print a random job (they're weighted so no need to do arcane probability stuff)
        print(random.choice(jobs))

# run main
if __name__ == "__main__":
    main()