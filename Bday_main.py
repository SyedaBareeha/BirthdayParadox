from birthday_paradox import BirthdayParadox

def main():
    bp1 = BirthdayParadox(group_size=50, simulations=200)
    bp1.show_probability()
    
    bp2 = BirthdayParadox(group_size=70, simulations=200)
    bp2.show_probability()

#  This must be at the top level, NOT inside main()
if __name__ == "__main__":
    main()
