characters = ['N', '!', 't', '8', '@', 'B', 'G', '-', '3', 'P', ':', 'x', 'U', ')', '2', 'c', 'K', 'o', 's', 'i', '#', '0', 'X', 'n', '7', '4', '1', ']', 'R', 'e', 'm', 'T', 'u', '^', 'D', 'j', '6', 'F', 'b', 'y', 'V', 'g', '%', 'h', 'w', 'r', 'k', '5', 'W', ' ', 'C', 'Q', '?', 'S', '{', 'f', '.', '*', 'q', ',', 'a', 'v', 'I', 'A', 'p', '(', 'J', 'z', 'H', 'Z', 'L', 'M', '[', 'O', 'd', '9', 'l', '}', 'E', ';', 'Y', '+', "'", '_', '$', '&', '!', '|', 'b', 'N', '"', '0', '/', '4', '>', '<']

encode_decode = True
while encode_decode == True:
     another = input("Want to do more encode and decode things? then Enter 'Y' if not Enter 'N' :--").upper()
     if another == 'N':
         encode_decode = False
         exit()
     elif another == 'Y':
        while True:
            direction = input("Type 'D' for decode Type 'E' to encode --: \n ").upper()
            if direction == 'E':
                text = input("Inpute your Message for 'ENCODET': --  ")
                break
            elif direction == 'D':
                text = input("Inpute your Message for 'DECODET':--   ")
                break
            else:
                print("ERROR -- Wrong inpute.... Please try again.")

        shift = int(input("Input your sift amount : --  "))

        def ceaser(start_text, shift_amount,direction):
            end_text = ''
            length = len(characters)
            for letter in start_text:
                position = characters.index(letter)
                if direction == 'E':
                    new_position = (position + shift_amount) % length
                elif direction == 'D':
                    new_position = (position - shift_amount) % length
                else:
                    print("ERROR -- Wrong inpute....")
                new_letter = characters[new_position]
                end_text += new_letter
            if direction == 'E':
                print(f"Your Encode Messase Is {end_text}")
            elif direction == 'D':
                print(f"Your Decode Messase Is {end_text}")
        ceaser(start_text=text, shift_amount= shift, direction=direction)
     else:
         encode_decode = False
         print("ERROR --")