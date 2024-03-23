#input
print ("Say Hello to Us!" , " Better choose it carefully!" , " Now enter your text! " , end='\n' , sep='\n')
user_greeting = input( "--> ") 
user_greeting = user_greeting.strip().lower()

if user_greeting.startswith("hello"):
    print("$0")
elif user_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
