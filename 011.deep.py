#CS50-Week2 
#Ask for input
#Based on : The Hitchhiker’s Guide to the Galaxy, Douglas Adams
question = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

#Read the input (is it 42?) 
if question.lower() == "42" or question.lower() == "forty-two" or question.lower() == "forty two": 
   print("YES!!") 
else: 
   print(" NO ;| ")
# in lines above: peint the feedback 