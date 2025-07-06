import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator_str = sys.argv[1] # Keep as string for now, safe_divide will convert
    denominator_str = sys.argv[2] # Keep as string for now, safe_divide will convert

    # Call the safe_divide function
    result = safe_divide(numerator_str, denominator_str)

    # --- THIS IS THE CRUCIAL PART TO CHANGE ---
    # Check if the result is a number (int or float), meaning success
    if isinstance(result, (int, float)):
        # If it's a number, format it into the expected sentence
        print(f"The result of the division is {result}")
    else:
        # If it's not a number, it must be an error message string from safe_divide
        print(result)
    # --- END OF CRUCIAL PART ---

if __name__ == "__main__":
    main()

