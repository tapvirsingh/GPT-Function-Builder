from gptfuncpropbuilder import GPTFuncPropBuilder

# Builds the function calling for GPT
class GPTFuncBuilder:


  # lst = List of properties / parameters
  def __init__(self,name=None, description=None, lst = None, dic = None, prefix = '', suffix = ''):
        
    self.__prefix = prefix
    self.__suffix = suffix
        
    # Calls this function to set the class attributes
    self.__assign(name, description, assign_lst = lst,  assign_dic = dic)

  def __assign(self,name, description, assign_lst = None, assign_dic = None):
    
    # If one of these is set
    is_set = assign_lst != None or assign_dic != None
    
    # Exit the function if none of the parameters are set
    if name== None and description == None and not is_set:
        return None
    
    # Sets the name and description of the function
    self.__name = name
    self.__description = description

    # Calls the function property builder
    o_prop = GPTFuncPropBuilder(prop_prefix = self.__prefix, prop_suffix = self.__suffix)
    self.__o_prop = o_prop

    # Priorty
    if assign_dic != None:
    # Build the properties using the list
      o_prop.build_props(dict_of_props = assign_dic)
    else:
      o_prop.build_props(lst_of_props = assign_lst)

    # Get the properties
    self.__properties = o_prop.get_props()
    # Get the required ones
    self.__required = o_prop.get_required()

  def __build_parameters(self):
      props = {
          "type":"object",
          "properties": self.__properties
        }
      if len(self.__required) > 0:
        props["required"] = self.__required

      return props
    
  # Public Methods
    
  # Add any property with not common prompt
  def add_prop(self, name,description):
    o_prop = self.__o_prop
    o_prop.add_prop(name,description)

  # Main function that builds and returns the enitre function
  def build(self,name=None, description=None, lst = None):
    self.__assign(name, description, lst)
    dic = {
            "type" : "function",
            "function":
            { "name":self.__name,
              "description":self.__description,
              "parameters":self.__build_parameters()
            }
          }

    return dic
  

# # Example

# Use either of the props
# All are marked * meaning these field are all required.
lst_of_prop = ["*GPU intensity","*display quality","*portability","*multitasking","*processing speed"]

# Or use
# dictionary of prop
dict_of_prop = {
    "*GPU intensity": "Prompt describing about GPU intensity",
    "*display quality":"Prompt describing about display quality",
    "*portability":"Prompt describing about probability",
    "*multitasking":"Prompt describing about display multitasking",
    "*processing speed":"Prompt describing about display processing speed"
  }

# Create build function object with the name, description and list of properties
o_build_func =  GPTFuncBuilder("find_laptop", 
                               "Based on user's requirements this function searches the laptop in the database",
                               lst = lst_of_prop,
                               prefix = "Classify",
                               suffix = "into High, Medium or Low")

# o_build_func =  GPTFuncBuilder("find_laptop", "Based on user's requirements this function searches the laptop in the database",dictionary = dict_of_prop)

# Add required budget property with custom description
o_build_func.add_prop("*budget","The amount of money a user can invest for purchasing laptop. Budget must be greater than INR 25000")

# Build the function
find_lptp = o_build_func.build()

# Output of the built function
print(find_lptp)