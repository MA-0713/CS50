#faces Smiley to emoji

#define the function
def convert(input_str):
    input_str = input_str.replace(':)', '🙂')
    input_str = input_str.replace(':(', '🙁')
    return input_str
#get the input
input_text = input("Type Here!") 
#define the output
output_text = convert(input_text)
#get the output
print(output_text)

#%%

#Condition 
#if the user calles the main function the function above will work (hopefully!)
#define the function first (it runs the code to the line contains the new unidetified function and wont go further...)

def main(): 
        user_input = input("Type a string here!")
        output = convert(user_input)
        print("here's your converted text : " , output )
        
if __name__ == "__main__" :
    main() 
