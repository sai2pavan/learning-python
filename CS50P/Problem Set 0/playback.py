#take input of a sentence from the user
def main():
    sent = input("Enter a sentence ").strip()
    print(replace(sent))
#replace spaces in the sentence with ...
def replace(sentence):
    return sentence.replace(" ","...")
#print output
main()