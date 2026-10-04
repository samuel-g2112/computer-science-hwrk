import random

game = True

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

socialvalue = 100
economicvalue = 100
naturalvalue = 100
year = 0

def setup():
    print("WELCOME TO CIVILIZATION SIMULATOR")
    print("Your points can't be below 0")
    print("\n")
    print("Enter your civilizations name:")
    civname = input("->")
    print("Year 0")
    print(f"Social: {socialvalue}")
    print(f"Economic: {economicvalue}")
    print(f"Natural: {naturalvalue}")
    return civname

def get_event():
    Resources = ["social","economic","natural"]
    rstatus = random.choice(Resources)
    Impact = ["positive","negative"]
    istatus = random.choice(Impact)

    social_disasters = [
        "A deadly disease spread through the population.",
        "A violent rebellion broke out.",
        "Crime increased dramatically across the cities.",
        "A major religious conflict divided the population.",
        "A large part of the population migrated away.",
        "A civil war broke out between rival factions.",
        "A political scandal caused widespread unrest.",
        "Food shortages caused riots in several cities.",
        "A powerful group began protesting against the government.",
        "Relations between different social groups became increasingly hostile.",
        "A major city was abandoned after years of declining population.",
        "The government lost the trust of much of the population."
    ]
    social_benefits = [
        "A new education system was introduced.",
        "A major festival brought the population together.",
        "A new hospital system improved public health.",
        "A popular leader united the population.",
        "A period of peace greatly increased public happiness.",
        "A new cultural movement brought people together.",
        "The government introduced important social reforms.",
        "A large number of skilled immigrants arrived.",
        "Literacy increased dramatically.",
        "A new university was founded.",
        "Crime fell after major improvements to the justice system.",
        "A strong sense of national identity developed."
    ]

    economic_disasters = [
        "The kingdom entered a severe recession.",
        "The currency lost much of its value.",
        "A major trading partner stopped doing business with the kingdom.",
        "A bank collapsed.",
        "A major trade route was blocked.",
        "Taxes became extremely difficult to collect.",
        "A large number of businesses went bankrupt.",
        "Inflation caused prices to rise rapidly.",
        "The government ran out of money.",
        "A major economic scandal damaged investor confidence.",
        "Pirates disrupted important trade routes.",
        "A shortage of workers slowed economic growth."
    ]
    economic_benefits = [
        "A major trade route opened.",
        "A large gold deposit was discovered.",
        "Foreign merchants began investing in the kingdom.",
        "A powerful new trading company was founded.",
        "The kingdom entered a period of rapid economic growth.",
        "A new industry became extremely profitable.",
        "A successful trade agreement was signed.",
        "A new banking system improved the economy.",
        "The kingdom became an important center of international trade.",
        "A technological invention greatly increased productivity.",
        "Taxes were reduced, encouraging businesses to grow.",
        "A new market was discovered overseas."
    ]

    natural_disasters = [
        "A devastating drought destroyed much of the farmland.",
        "A massive earthquake struck the kingdom.",
        "A powerful flood destroyed settlements near the river.",
        "A volcanic eruption covered the surrounding land in ash.",
        "A terrible storm destroyed forests and farmland.",
        "A wildfire spread across a huge area.",
        "A swarm of locusts destroyed the crops.",
        "An unusually harsh winter killed large amounts of livestock.",
        "A major landslide destroyed a mountain settlement.",
        "A tsunami devastated the coastal region.",
        "A disease killed a large portion of the kingdom's livestock.",
        "A river changed course, flooding several settlements."
    ]
    natural_benefits = [
    "An unusually large harvest provided abundant food.",
    "A new source of fresh water was discovered.",
    "A large forest rich in valuable resources was discovered.",
    "A deposit of iron was discovered in the mountains.",
    "A large amount of fertile farmland became available.",
    "A rich deposit of gold was discovered.",
    "The climate became unusually favorable for farming.",
    "A new source of coal was discovered.",
    "A previously unknown species of valuable plant was discovered.",
    "A river provided a new route for transportation.",
    "A large natural harbor was discovered.",
    "The kingdom discovered a region rich in valuable minerals."
]

    if rstatus == "social":
        if istatus == "positive":
            points = (random.randint(1,16))
            event = random.choice(social_benefits)
        elif istatus == "negative":
            points = (random.randint(1,16)) * -1
            event = random.choice(social_disasters)
    elif rstatus == "economic":
        if istatus == "positive":
            points = (random.randint(1,16))
            event = random.choice(economic_benefits)
        elif istatus == "negative":
            points = (random.randint(1,16)) * -1
            event = random.choice(economic_disasters)
    elif rstatus == "natural":
        if istatus == "positive":
            points = (random.randint(1,16))
            event = random.choice(natural_benefits)
        elif istatus == "negative":
            points = (random.randint(1,16)) * -1
            event = random.choice(natural_disasters)
    return event, points, rstatus

name = setup()
while game == True:
    nothing = input("Press ENTER to advance a year.")
    clear()
    event, points, rstatus = get_event()


    if rstatus == "social":
        socialvalue = socialvalue + points
    elif rstatus == "economic":
        economicvalue = economicvalue + points
    elif rstatus == "natural":
            naturalvalue = naturalvalue + points

    print("Year:", year)

    print("\n")
    print(event)
    print("\n")
    print(f"{points} {rstatus} points")
    print("\n")
    print(f"Social: {socialvalue}")
    print(f"Economic: {economicvalue}")
    print(f"Natural: {naturalvalue}")

    if socialvalue <= 0:
        clear()
        print("Year:", year)
        print("\n")
        print(f"Social: {socialvalue}")
        print(f"Economic: {economicvalue}")
        print(f"Natural: {naturalvalue}")
        print("\n")
        print(f"Your citizens manifested, and {name} fell off.")
        print("You lost!")
        game = False
    if economicvalue <= 0:
        clear()
        print("Year:", year)
        print("\n")
        print(f"Social: {socialvalue}")
        print(f"Economic: {economicvalue}")
        print(f"Natural: {naturalvalue}")
        print("\n")
        print(f"{name} has no more money to trade, so allied betrayed you.")
        print("You lost!")
        game = False
    if naturalvalue <= 0:
        clear()
        print("Year:", year)
        print("\n")
        print(f"Social: {socialvalue}")
        print(f"Economic: {economicvalue}")
        print(f"Natural: {naturalvalue}")
        print("\n")
        print(f"There is no more food and water, so everyone in {name} left.")
        print("You lost!")
        game = False

    year += 1
