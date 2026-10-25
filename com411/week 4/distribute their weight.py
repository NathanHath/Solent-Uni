def sum_weights(weight_character, weight_invertory):
    return weight_character + weight_invertory

def calc_avg_weight (weight_character, weight_invertory):
    return sum_weights(weight_character, weight_invertory) / 2

def run ():
    weight_character = int(input("Enter your weight character: "))
    weight_invertory = int(input("Enter your weight invertory: "))
    choice = input("do you want to caluate the average weight? or the sum of the weights?")
    if choice == "average":
        return calc_avg_weight(weight_character, weight_invertory)
    elif choice == "sum":
        return sum_weights(weight_character, weight_invertory)
    else:
        return "Error"

print (run())