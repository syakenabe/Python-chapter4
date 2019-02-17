def change(string):
    try:
        return float(string)
    except ValueError:
        print("This word can't change to float.")
        
result = change("word")
print(result)
