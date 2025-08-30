from birthday_paradox import BirthdayParadox

def main():
     bp1 = BirthdayParadox(group_count=50, repeat_count=200)
     bp1.show_probability()

     bp2 = BirthdayParadox(group_count=70, repeat_count=200)
     bp2.show_probability()


if __name__ == "__main__":
 main()