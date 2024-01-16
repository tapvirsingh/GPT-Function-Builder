
# All are marked * meaning these field are all required.
lst_of_prop = ["*GPU intensity","*display quality","*portability","*multitasking","*processing speed"]

# Create GPT function property object
o_prop = GPTFuncPropBuilder()

# Build properties from the list
o_prop.build_props(lst_of_prop)

# Add required budget property with description
o_prop.add_prop('*budget',"The amount of money a user can invest for purchasing laptop. Budget must be greater than INR 25000")

# Get the built properties
props = o_prop.get_props()

# Output
print(props)