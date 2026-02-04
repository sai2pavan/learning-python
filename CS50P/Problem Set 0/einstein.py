#take input of m value from the user
def main():
    m = int(input("Enter value of M "))
    print("E =",formula(m))
#compute e = mc^2 
def formula(mass):
    return (mass * 300000000 * 300000000)
#print output
main()