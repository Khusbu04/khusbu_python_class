def setup_mission():
    print("Setting up for the mission....")
    available_foods = [
        "apple",
        "banana",
        "watermelon",
        "chocolate",
        "water",
        "grapes",
        "pineapple",
        "cherry",
        "berries",
        "cupcakes",
        "pestries",
        "pizza",
        "burger",
    ]
    available_crews = int(input("Enter available crews"))
    print("Setup Completed.....")
    return available_crews, available_foods
def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.......")
    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronauts and food available = {foods}")
    print("WELCOME TO THE MARS!!!")
    print("Your battery is dead please change the battery")
    print("Mission completed")
alien_attack_game()