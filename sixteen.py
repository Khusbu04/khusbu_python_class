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
    #check batteries over hundred
def get_charged_batteries():
    batteries = [50, 30, 4, 45, 12, 18, 30] ##battery basket
    minimum_battery_powewr = 20 ### battery use minimum 20% charge
    usable_battery_power = 0
    usable_battery_count = 0
    for battery in batteries: ## check every battery
     if battery > minimum_battery_power: #check if battery is over charge 20% to use
      usable_battery_power += battery # if yes use power added
      usable_battery_count = usable_battery_count + 1 # if yes use count added
      if usable_battery_power >= 100:
        return usable_battery_power, usable_battery_count

def decrypt_alien_message(alien_message):
    human_message = alien_message[::-1] ## reverse string
    return human_message
def food_divide_equally(foods, crew_member):
    equally_foods = len(food) // crews_member
    remaining_foods = len(foods) % crews_member
    return equally_foods, remaining_food 
def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission.......")
    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronauts and food available = {foods}")
    print("WELCOME TO THE MARS!!!")
    print("Your battery is dead please change the battery")
    battery_power, battery_count = get_charged_batteries()
    print("Hurray!!! You battery is charged.")
    print("Oops... Alien has arrived saying:")
    print("rednerrus")
    decrypted_text = decrypt_alien_message("rednerrus")
    print(f"Alien is saying: {decrypted_text}")
    print("Alien has captured all astronauts")
    print("if astronaut wants to escape they have divide each food and give remaining foods")
    equally_divided, remaining_food = food_divide_equally(foods, crews_number)
    print(f"You have {equally_divided} foods divided equally and remaining = {remaining_food}")
    print("Okay... Now you can go to Earth")
    print("Mission completed")
alien_attack_game()