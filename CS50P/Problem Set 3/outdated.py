months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month,day,year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            print(f"{year:04}-{month:02}-{day:02}")
        else:
            month,day,year = date.replace(",","").split()
            month = month.title()
            month = months.index(month) + 1
            day = int(day)
            year = int(year)
        if not (1 <= month <= 12 and 1 <= day <= 31):
                continue
        print(f"{year:04}-{month:02}-{day:02}")
        break
    except (ValueError, IndexError):
        pass