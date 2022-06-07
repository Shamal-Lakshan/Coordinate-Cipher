from collections import deque

alphabet = deque(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",","])

coordinates = deque(["(0,0)","(0,1)","(0,2)","(0,3)","(0,4)","(0,5)","(0,6)","(0,7)","(0,8)","(0,9)","11","22","32","41","31","21","23","24","34","33","43","42","51","52","53","12","13","14","44","54","35","25","15","45","55","47","69","56","10"])

choice = input("Encode(E) or Decode(D): " )

def decode():

    container = []

    user_input = input("Input a string to decode: ")

    key = input("Enter the key: ")
    key = int(key)
    coordinates.rotate(key)

    for i in range(len(user_input)):
        for j in range(len(coordinates)):
            if (user_input[i]==" "):
                container.append(26)
                break
        
            if i==len(user_input)-1:

                break
            else: 
                sentence=user_input[i]+user_input[i+1]
                if coordinates[j]==sentence:
                    container.append(j)
    print("Result :")

    for k in range(len(container)): 
        print(alphabet[container[k]],end="")
    print("\n")


def encode():
    container=[]
    user_input=input("Input a string to encode: ")

    key = input("Enter the key: ")
    key = int(key)
    coordinates.rotate(key)

    sentence_up=user_input.upper()

    for i in range(len(sentence_up)):
        for j in range(len(alphabet)):
            if (sentence_up[i]==" "):
                container.append(26)
                break
        
            if alphabet[j]==sentence_up[i]:
                container.append(j)

    print("Result :")

    for k in range(len(container)):
        print(coordinates[container[k]],end=" ") 
    print("\n")


if choice == "D":
    decode()
elif choice == "E":
    encode()
else:
    print("Please choose a valid operation!(E/D)")


