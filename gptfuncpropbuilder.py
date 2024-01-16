# Function's property builder
class GPTFuncPropBuilder:

  def __init__(self,prop_prefix = '', prop_suffix = ''):

    # Common property's prefix and suffix of prompt
    # default value for function find_laptops
    # Set new value using prop_prefix = some text.
    self.__prop_prefix = prop_prefix
    self.__prop_suffix = prop_suffix  
        
    self.__d_find_laptop_properties = {}
    # Fields marked as *
    self.__required = []

    # Checks if build_props function was called before
    # calling add_prop
    __has_build = False

  # Build properties
  def build_props(self, lst):
    if not isinstance(lst, list):
      return None

    self.__has_build = True

    for item in lst:
      #
      # Following code does the following e.g.
      # Example
      # Converts GPU intensity into gpu_intensity
      #

      lower_item, item = self.prepare_key(item)

      # add key value in dictionary
      self.__d_find_laptop_properties[lower_item] = self.__build_prop(item)

  # Add any other property which does not have common prop prefix and suffix
  def add_prop(self, key, val):
    # If build function has already been called
    # check if the current prop is required (*)
    if self.__has_build:

        # prepare key and add required item to the required list
        # val ignored as we don't want to make changes to the description
        key,ignore_val = self.prepare_key(key)

    self.__d_find_laptop_properties[key] = self.__insert_in_dic(val)

  # Prepare key from val
  def prepare_key(self, val):

      # if has star - Meaning the parameter is required
      has_star = '*' == val[0]

      if has_star:
        # ignore star
        val = val[1:]

       # converting the value to lower case
      key = val.lower()
      # replace space with underscore in key values
      key = key.replace(' ', '_')

      if has_star:
        # Add item to required list
        self.__required.append(key)

      return key, val

  # Return properties
  def get_props(self):
    return self.__d_find_laptop_properties

  def get_required(self):
    return self.__required

  # Getters and Setters
  @property
  def prop_prefix(self):
    return self.__prop_prefix

  @prop_prefix.setter
  def prop_prefix(self, val):
    self.__prop_prefix = val

  # Getters and Setters
  @property
  def prop_suffix(self):
    return self.__prop_suffix

  @prop_suffix.setter
  def prop_suffix(self, val):
    self.__prop_suffix = val


  # This function sets properties description.
  def __insert_in_dic(self,description):

    desc = description

    dic = {
      "type": "string",
      "description": desc
    }
    return dic

  # Returns property
  def __build_prop(self, text):
    
    description = f'{self.prop_prefix} {text} {self.prop_suffix}'

    return self.__insert_in_dic(description.strip())


# Example

# # All are marked * meaning these field are all required.
# lst_of_prop = ["*GPU intensity","*display quality","*portability","*multitasking","*processing speed"]

# # Create GPT function property object
# o_prop = GPTFuncPropBuilder()

# # Build properties from the list
# o_prop.build_props(lst_of_prop)

# # Add required budget property with description
# o_prop.add_prop('*budget',"The amount of money a user can invest for purchasing laptop. Budget must be greater than INR 25000")

# # Get the built properties
# props = o_prop.get_props()

# # Output
# print(props)