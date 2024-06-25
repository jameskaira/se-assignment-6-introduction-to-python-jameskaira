try:
  
    file = open("non_existent_file.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    
    print("The file does not exist.")
finally:
    
    print("This is the finally block.")