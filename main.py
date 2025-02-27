
def modify_data(input_data):
    return input_data + ' - B'

if __name__ == "__main__":
    input_data = input("Enter data: ")
    result = modify_data(input_data)
    print(result)
