print ("Program started")
code = abs(int(input("Enter a ASCII code: ")))

if 32 <= code <= 126:
    print  (f"The character represented by the ASCII code {code} is {chr(code)}")
else:
    print("error")

print ("Program ended")
