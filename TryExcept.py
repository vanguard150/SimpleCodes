try:
    age=int(input("Age:"))
    income=20000
    avearage=income / age
    print(f"Average income is {avearage}")
except ValueError:
    print("Age has to be a number")
except ZeroDivisionError:
    print("Age can not be zero")
