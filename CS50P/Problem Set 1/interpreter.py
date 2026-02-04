def main():
    expression = input("Expression: ").strip().split()
    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])
    print(interpreter(x,y,z))

def interpreter(x,y,z):
    match y:
        case "+":
            return (x + z)
        case "-":
            return (x - z)
        case "*":
            return (x * z)
        case "/":
            return (x / z)

main()