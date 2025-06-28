# temp_conversion_tool.py
# A script to demonstrate variable scope by converting temperatures between Celsius and Fahrenheit

# Global conversion factors - accessible throughout the script
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius using global conversion factor
    
    Args:
        fahrenheit: Temperature in Fahrenheit (float or int)
    
    Returns:
        float: Temperature converted to Celsius
    """
    # Using the global conversion factor to convert F to C
    # Formula: (F - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit using global conversion factor
    
    Args:
        celsius: Temperature in Celsius (float or int)
    
    Returns:
        float: Temperature converted to Fahrenheit
    """
    # Using the global conversion factor to convert C to F
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_temperature_input():
    """
    Get temperature input from user with validation
    
    Returns:
        float: Valid temperature value
    
    Raises:
        ValueError: If user enters non-numeric value
    """
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    """
    Get unit input from user with validation
    
    Returns:
        str: Valid unit ('C' or 'F')
    
    Raises:
        ValueError: If user enters invalid unit
    """
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit_input not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    return unit_input

def main():
    """
    Main function to run the temperature conversion tool
    """
    try:
        # Get temperature input from user
        temperature = get_temperature_input()
        
        # Get unit input from user
        unit = get_unit_input()
        
        # Perform conversion based on the input unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the script when executed directly
if __name__ == "__main__":
    main()
