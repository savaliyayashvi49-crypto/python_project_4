

data = []


def input_data():
    """Take numeric values from the user and store them in the dataset."""
    global data

    values = input("Enter data for a 1D array (separated by spaces): ")

    data = [int(x) for x in values.split()]

    print("\nData has been stored successfully!")


def display_summary():
    """Display dataset summary using Python built-in functions."""
    if not data:
        print("\nPlease enter data first.")
        return

    total = len(data)
    minimum = min(data)
    maximum = max(data)
    total_sum = sum(data)
    average = total_sum / total

    print("\nData Summary:")
    print("- Total elements:", total)
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total_sum)
    print("- Average value:", round(average, 2))


def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def filter_data():
    """Filter dataset values using a lambda function."""
    if not data:
        print("\nPlease enter data first.")
        return

    threshold = int(
        input("Enter a threshold value to filter out data below this value: ")
    )

    filtered = list(filter(lambda x: x >= threshold, data))

    print("\nFiltered Data (values >= {}):".format(threshold))

    if filtered:
        print(", ".join(map(str, filtered)))
    else:
        print("No values found.")


def sort_data():
    """Sort the dataset in ascending or descending order."""
    if not data:
        print("\nPlease enter data first.")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter your choice: ")

    if choice == "1":
        sorted_data = sorted(data)
        print("\nSorted Data in Ascending Order:")
        print(", ".join(map(str, sorted_data)))

    elif choice == "2":
        sorted_data = sorted(data, reverse=True)
        print("\nSorted Data in Descending Order:")
        print(", ".join(map(str, sorted_data)))

    else:
        print("\nInvalid sorting choice.")


def dataset_statistics(**kwargs):
    """Return multiple dataset statistics using keyword arguments."""
    minimum = kwargs.get("minimum")
    maximum = kwargs.get("maximum")
    total_sum = kwargs.get("total_sum")
    average = kwargs.get("average")

    return minimum, maximum, total_sum, average


def display_statistics():
    """Display multiple statistics returned from another function."""
    if not data:
        print("\nPlease enter data first.")
        return

    minimum = min(data)
    maximum = max(data)
    total_sum = sum(data)
    average = total_sum / len(data)

    stats = dataset_statistics(
        minimum=minimum,
        maximum=maximum,
        total_sum=total_sum,
        average=average
    )

    print("\nDataset Statistics:")
    print("- Minimum value:", stats[0])
    print("- Maximum value:", stats[1])
    print("- Sum of all values:", stats[2])
    print("- Average value:", round(stats[3], 2))


print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        display_summary()

    elif choice == "3":
        number = int(input("Enter a number to calculate its factorial: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(number)
            print("Factorial of", number, "is:", result)

    elif choice == "4":
        filter_data()

    elif choice == "5":
        sort_data()

    elif choice == "6":
        display_statistics()

    elif choice == "7":
        print(
            "\nThank you for using the Data Analyzer and Transformer Program. "
            "Goodbye!"
        )
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 7.")