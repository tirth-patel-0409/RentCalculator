# todo - Input needed
# todo - total rent
# todo - persons living in flat
# todo - food, electricity bill etc.

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nInput interrupted by user. Exiting.")
            exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def rent_calculator():
    print("=== Rent Calculator ===")
    rent = get_positive_int("Enter Your Flat Rent = ")
    food = get_positive_int("Enter The Amount Of Food Ordered = ")
    electricity_bill = get_positive_int("Enter The Amount Of Electricity Bill = ")
    persons = get_positive_int("Enter The Number of Persons = ")

    try:
        while persons <= 0:
            print("Error: Please enter a valid number of persons.")
            persons = get_positive_int("Enter The Number of Persons = ")
        total_cost = rent + food + electricity_bill
        per_person_rent = total_cost // persons
        print("\n------------------------------")
        print("Total Rent (including all):", total_cost)
        print("Rent for each person is:", per_person_rent)
        print("------------------------------")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")


if __name__ == "__main__":
    rent_calculator()
