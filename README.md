# GPT Function Builder
Quick and easy function calling JSON format builder. Makes it more readable and reduces the chances of error.

## Creating the object
```o_build_func = GPTFuncBuilder(name=None, description=None, lst = None)```

### Parameters
**name :** Name of the function

**description :** Description of the function

**lst :** List of parameters


**Required Parameters :** prepend '*' before the name of the parameter in the list to mark it required.

```lst_of_prop = ["*GPU intensity","*display quality","*portability","*multitasking","*processing speed"]```

## Adding Property / Parameter
```o_build_func = add_prop(name,description)```

### Parameters

**name :** Name of the parameter

**description :** Description of the parameter


```python
# Usage Example

# All are marked * meaning these field are all required.
lst_of_prop = ["*GPU intensity","*display quality","*portability","*multitasking","*processing speed"]

# Create build function object with the name, description and list of properties
o_build_func = GPTFuncBuilder("find_laptop", "Based on user's requirements this function searches the laptop in the database",lst_of_prop)

# Add required budget property with custom description
o_build_func.add_prop("*budget","The amount of money a user can invest for purchasing laptop. Budget must be greater than INR 25000")

# Build the function
find_lptp = o_build_func.build()

# Output of the built function
print(find_lptp)
```

## Output

```python
{
  'type': 'function',
  'function': {
    'name': 'find_laptop',
    'description': "Based on user's requirements this function searches the laptop in the database",
    'parameters': {
      'type': 'object',
      'properties': {
          'gpu_intensity': {
              'type': 'string',
              'description': 'GPU intensity'
          },
          'display_quality': {
              'type': 'string',
              'description':'display quality'
          },
          'portability':{
              'type': 'string',
              'description': 'portability'
          },
          'multitasking': {
              'type': 'string',
              'description': 'multitasking'
          },
          'processing_speed': {
              'type': 'string',
              'description': 'processing speed'
          },
          'budget': {
              'type': 'string',
              'description': 'The amount of money a user can invest for purchasing laptop. Budget must be greater than INR 25000'
          }
      },
      'required': ['gpu_intensity', 'display_quality', 'portability', 'multitasking', 'processing_speed', 'budget']
    }
  }
}

```
