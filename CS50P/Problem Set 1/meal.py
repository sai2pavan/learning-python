def main():
    hours,minutes = input("What time is it? ").split(":")
    value = convert(hours,minutes)
    if 7 <= value <= 8:
        print("breakfast time")
    elif 12 <= value <= 13:
        print("lunch time")
    elif 18 <= value <= 19:
        print("dinner time")

def convert(hours,minutes):
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    value = hours + minutes
    return value

main()