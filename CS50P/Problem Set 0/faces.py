#take input sentence from the user
def main():
    sent = input("Enter sentence ")
    print(emojis(sent))
#convert emoticons into emojis
def emojis(sentence):
    return sentence.replace(":)","🙂").replace(":(","🙁")
#print output
main()