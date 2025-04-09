#Write a program which prompts the user for an adjective, then a noun, 
# then a verb, and then prints a fun sentence with those words!
#Mad Libs is a word game where players are prompted for one word at a time,
# and the words are eventually filled into the blanks of a word template to make an entertaining story! 
# We've provided you with the beginning of a sentence (the SENTENCE_START constant) 
# which will end in a user-inputted adjective, noun, and then verb.



STORY_START: str = "Yesterday, I saw a "

def main():
    color: str = input("Enter a color: ")
    animal: str = input("Enter an animal: ")
    action: str = input("Enter an action: ")

    print(STORY_START + color + " " + animal + " " + action + " in the park!")

if __name__ == '__main__':
    main()
