# enter name
# {name} you will die on [date].
# cause of death [random choice]

import random
def death_generator():
    name = input("What is your name? ")

    death_month = random.choice(["January","February","March","April","May", "June","July","August", "September","October","November","December"])
    death_date = random.randint(1,28)
    death_year = random.randint(2025,2130)

    death_date = f"{death_date} {death_month} {death_year}"

    deaths = ("getting run over by a tractor",
              "getting electrocuted by an electric eel",
              "passing away peacefully surrounded by your family :)",
              "licking a poisonous frog",
              "getting consumed by your pet boa constrictor",
              "torture. sorry man :(",
              "overtaking a lorry when you reeeeaalllyyy shouldn't have",
              "drowning after doing a cool flip into the ocean",
              "going cave diving. you idiot.",
              "straining too hard on the toilet. just like Elvis. lol.",
              "getting trampled by an elephant",
              "accidentally stabbing yourself while doing the washing up",
              "choking on a cherry pit",
              "falling out the window of your 5* hotel room in Dubai",
              "having a coconut fall on your head at the beach",
              "getting your hand stuck in a vending machine",
              "an eagle dropped a tortoise on your head")

    death_method = random.choice(deaths)
    print(f"{name}, you died by {death_method} on {death_date}.")

def choice():
    choose = input("Take a chance and find out how and when you die? (y/n): ").lower()
    if choose == "y":
        death_generator()
    elif choose == "n":
        print("Fine. Goodbye.")
    else:
        print("Mate it's a yes or no question, how did you mess that up?? Try again")
        choice()

choice()
