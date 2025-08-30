import random

class BirthdayParadox:
    def __init__(self, group_count, repeat_count=200):
        """
        group_count: Number of people in the group
        repeat_count: Number of times the simulation is repeated
        """
        self.group_count = group_count
        self.repeat_count = repeat_count

    def generate_birthdays(self):
        """
        Create a list of randomly assigned birthdays for all individuals in the group.
        Each birthday is represented by an integer between 1 and 365.
        """
        birthdays = []  # List to store generated birthdays
        for _ in range(self.group_count): 
            day = random.randint(1, 365)
            birthdays.append(day)
        return birthdays

    def has_duplicate_birthday(self, birthdays):
        """
        Check if the list of birthdays contains any duplicates.

        Returns:
            True if at least two people share the same birthday, False otherwise.
        """
        return len(birthdays) != len(set(birthdays))

    def run_simulation(self):
        """
        Run the birthday paradox simulation multiple times.

        Returns:
            Estimated probability that at least two people in the group share a birthday.
        """
        duplicate_cases = 0

        for _ in range(self.repeat_count):
            birthdays = self.generate_birthdays()
            if self.has_duplicate_birthday(birthdays):
                duplicate_cases += 1

        probability = duplicate_cases / self.repeat_count
        return probability

    def show_probability(self):
        """
        Run the simulation and print the estimated probability.
        """
        probability = self.run_simulation()
        print(f"For a group of {self.group_count} people → Probability ≈ {probability:.2f}")
