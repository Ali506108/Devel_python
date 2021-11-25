def calories(grams_of_fat , grams_of_carbohydrates):
    calories_from_fat = grams_of_fat * 9
    calories_from_carbohydrates = grams_of_carbohydrates * 4
    print(calories_from_fat)
    print(calories_from_carbohydrates)

calories(int(input('введите грам жиров: ')) , int(input('введите грам углеродав: ')) )