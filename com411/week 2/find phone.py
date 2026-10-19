
place = input("Where should I look?")

if place == "in the bedroom":
    bedroom_place = input("Where in the bedroom should I look?")
    if bedroom_place == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

elif place == "in the bathroom":
    bathroom_place = input("Where in the bathroom should I look?")
    if bathroom_place == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found some stuff but no phone.")

elif place == "in the living room":
    lab_place = input("Where in the living room should I look?")
    if lab_place == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

else:
 print("I am not sure where that place is located.")