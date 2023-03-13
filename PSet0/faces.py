# main 
def main():
    # prompt user to express his/her feelong with emoticons
    user_feeling = input("Please! Express your feeling: ")
    emotico_emoji(user_feeling)

# make function to replace ":)" and ":(" with emoji
def emotico_emoji(message):

    # replacing ":)" to "🙂"
    message = message.replace(":)", "🙂")
    # replacing ":(" to "🙁"
    message = message.replace(":(", "🙁")
    # print user message 
    print(message)
    
main()
