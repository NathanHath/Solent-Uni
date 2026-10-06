cover_type = input("what is the cover type (hard/soft): \n")
if cover_type=="soft":
    perfect_bound = input("is the book perfect bound (yes/no)\n")
    if perfect_bound=="yes":
        print ("Soft cover, perfect bound books are very popular!")
    else:
        print ("Soft covers with coils or stitches are great for short books")
elif cover_type=="hard":
    print ("Books with hard covers can be more expensive!")
else:
    print ("error")