available_food = [
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
available_crews = 3
each_crew_food = len(available_food) // available_crews
remaining_food_count = len(available_food) % available_crews
print(f"Each crew get {each_crew_food} food and Remaining food count = {remaining_food_count}")