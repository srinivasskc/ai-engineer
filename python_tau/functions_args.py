print("====Positional Args====")


def user_info(name, age, city):
    """
    This function takes 3 args.
    name, age, city as positional arguments.
    """
    print(f"{name} of age-{age} yrs old, lives at {city}")


user_info("srinivas", 36, "Hyd")

# user_info("Srinivas", 30)

print("\n ====Keyword Args====")


def user_details(name, age=0, city="Bglr"):
    """
    This function takes 3 args.
    name, age, city as positional arguments.
    """
    print(f"{name} of age-{age} yrs old, lives at {city}")


user_details("srinivas", 36, "Hyd")

user_details("Srinivas", 30)

user_details("Kadiyala")

user_details(age=20, name="Vasu")

print("\n ====*args, **kwargs ====")


def application(fname, lname, email, company, *args, **kwargs):
    print(f"{fname} {lname}, His/Her email is: {email}, Works at {company}")

    # Explicitly Printing the arguments.
    print(f"Additional Positional Arguments: {args}")
    print(f"Additional Keyword Arguments: {kwargs}")
    print("Type of positional arguments: ", type(args))
    print("Type of keyword arguments: ", type(kwargs))


application(
    "Srinivas",
    "Kadiyala",
    "srinivasskc@gmail.com",
    "Moolya",
    75000,
    join_date="June 16,2026",
)
