keys = [36, 88, 54, 28, 49, 21, 63, 7, 19, 2, 11, 41]
for key in keys:
    print(f"Key={key}, bucket={(2*key + 3) % 17}")
