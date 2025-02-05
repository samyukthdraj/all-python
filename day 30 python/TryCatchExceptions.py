try: #conditons
    with open("./day 30 python/file.txt","r") as file:
        file.write("Hey")
    
    dictionary = {"key":"value"}
    print(dictionary["non-existent-key"])

except FileNotFoundError as filenotfound: #if try fails then except is run, if the condition in try fails except will run.
    print(f"File '{filenotfound}' was missing. So a file_added.txt is created.")
    with open("./day 30 python/file_added.txt","a") as file:
        file.write("Hello")

except KeyError as keyerror:
    print(f"Key '{keyerror}' was not found.") 
    print(f"The value searched for in this error was {dictionary["key"]}")   

else: #if try is successful then else is run
    print(file.read())



finally: #if try is successful or failed, finally will run
    print("This statement will run regardless of if try is successful or not.")

raise ValueError ("I created this exception") #we can put out our own exceptions.


##json files.

# Website = input.get()
# email = email.get()

# new_file = {
#     Website:
#     f"Email: {email}"
# }

# try:
#     with open ("jsonfile.json", "r") as json1:
#         data = json.load(json1) #read from a pre-existing json file.
# except FileNotFoundError:
#     with open("jsonfile.json", "w") as json1:
#         json.dump (new_data, json1, indent=4) #create new json file w details from new_data
# else:
#     data.update(new_data) #updating old data w new data.

#     with open("jsonfile.json", "w") as json1:
#         json.dump (new_data, json1, indent=4) #saving updated json file.
# finally:
#     website.label.delete(0,END)
