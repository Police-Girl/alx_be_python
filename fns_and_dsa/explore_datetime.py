# explore_datetime.py
# A script to demonstrate Python's datetime module functionality

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Function to display the current date and time in YYYY-MM-DD HH:MM:SS format
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Function to calculate a future date by adding specified days to current date
    
    Args:
        current_date: datetime object representing the current date
        days_to_add: integer number of days to add
    
    Returns:
        datetime object representing the future date
    """
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    
    return future_date

def main():
    """
    Main function to run the datetime exploration script
    """
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        # Prompt user for number of days
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        # Calculate and display future date
        future_date = calculate_future_date(current_date, days_to_add)
        
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the script when executed directly
if __name__ == "__main__":
    main()
