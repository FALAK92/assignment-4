def madlibs():
    print("Welcome to the Madlibs game!")
    
    # User inputs for the story
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adj2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb (past tense): ")
    
    
    story = f"Once upon a time, there was a {adj1} {noun1}. It {verb1} over the {adj2} {noun2} and {verb2} into the sunset."
    
    print("\nHere's your Madlib story:")
    print(story)

madlibs()

