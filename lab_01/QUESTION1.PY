string_var = input("Enter a string: ")
int_var = int(input("Enter an integer: "))
float_var = float(input("Enter a float: "))
bool_input = input("Enter 'True' or 'False' for a boolean: ")
bool_var = bool_input.lower() == 'true'

print("\nValues and their types:")
print(f"String: {string_var} (Type: {type(string_var)})")
print(f"Integer: {int_var} (Type: {type(int_var)})")
print(f"Float: {float_var} (Type: {type(float_var)})")
print(f"Boolean: {bool_var} (Type: {type(bool_var)})")
