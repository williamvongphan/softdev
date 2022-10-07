import csv
import random


def choose_occupation():
    """
    Chooses an occupation from the csv file and returns it as a string

    Returns:
        str: occupation chosen
    """
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
        return random.choice(jobs)


# run main
if __name__ == "__main__":
    choose_occupation()
