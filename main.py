def change_data_step(input_data):
    # Assuming input_data is a string with two elements separated by a space
    elements = input_data.split()
    if len(elements) != 2:
        return "Input should contain two elements."
    return f"{elements[0]} - {elements[1]}"

# Example usage
input_data = input("Enter two elements separated by a space: ")
output_data = change_data_step(input_data)
print(output_data)
