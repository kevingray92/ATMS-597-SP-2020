# -*- coding: utf-8 -*-
"""ATMS-597-Project-1-Submit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eU89GMopPMC2KpbqIgLmCBBQKDYA9icW

ATMS-597-SP-2020 Project 1
Task: Create an object-oriented python module that converts temperatures interchangeably between degrees Celsius, Fahrenheit, and Kelvin.

Group Members:Jeffrey Thayer, Carolina Bieri, Rose Miller

Installing needed libraries and importing packages
"""

!apt-get -qq install libproj-dev proj-data proj-bin libgeos-dev
import numpy as np

# ATMS-597-Project
# 
class temp_array():
    """
    A class to store temperature values and convert them interchangeably between 
    Celsius, Fahrenheit, and Kelvin.   
    """

    # Defining the function for temperature values and units
    def __init__(self, temp_values, temp_units):  # This is a special function to initiate a method 
        self.temp_values = temp_values
        self.temp_units = temp_units
    

    # Defining the function for temperature conversion between Kelvin, Celsius, and Fahrenheit
    def tempconvert(self, conversion_unit):
        """ 
        This function converts temperature values from the current units to desired units.
        Supported units are degrees C, degrees F, and K. 

        Input: 
        conversion_unit - desired unit for output temperature values (string; 'C', 'K', or 'F')

        Output:
        A new instance of the temp_array class which includes the new temperature values
        in the desired units

        """
        # Not a list unless...it is
        islist = False


        # Checking whether the temperature input type is a list or numpy array
        if type(self.temp_values) is list:
            self.temp_values = np.asarray(self.temp_values)
            islist = True
        elif isinstance(self.temp_values, np.ndarray) == True:
            self.temp_values = self.temp_values


        # Setting up logic comparisons to convert temperatures stated in Celsuis to Kelvin or Fahrenheit
        if self.temp_units == "C" and conversion_unit == "C":
            print ("Values are already in degrees C")
            new = temp_array(self.temp_values, self.temp_units)
        elif self.temp_units == "C" and conversion_unit == "K":
            new = temp_array(self.temp_values + 273.15,"K")
        elif self.temp_units == "C" and conversion_unit == "F":
            new = temp_array(self.temp_values * 9.0 / 5.0 + 32.0,"F")
        elif self.temp_units == "C":
            raise ValueError("Error: incompatible temperature unit. Conversion units must be Fahrenheit or Kelvin.")

    
        # Setting up logic comparisons to convert temperatures stated in Kelvin to Celsuis or Fahrenheit
        if self.temp_units == "K" and conversion_unit == "K":
            print ("Values are already in degrees K")
            new = temp_array(self.temp_values, self.temp_units)
        elif self.temp_units == "K" and conversion_unit == "C":
            new = temp_array(self.temp_values - 273.15,"C")
        elif self.temp_units == "K" and conversion_unit == "F":
            new = temp_array((self.temp_values - 273.15) * 9.0 / 5.0 + 32.0,"F")
        elif self.temp_units == "K":
            raise ValueError("Error: incompatible temperature unit. Conversion units must be Celsius or Fahrenheit.")
    

        # Setting up logic comparisons to convert temperatures stated in Fahrenheit to Celsuis or Kelvin 
        if self.temp_units == "F" and conversion_unit == "F":
            print ("Values are already in degrees F")
            new = temp_array(self.temp_values, self.temp_units)
        elif self.temp_units == "F" and conversion_unit == "K":
            new = temp_array((self.temp_values - 32.0) * (5.0 / 9.0) + 273.15,"K")
        elif self.temp_units == "F" and conversion_unit == "C":
            new = temp_array((self.temp_values - 32.0) * (5.0 / 9.0),"C")
        elif self.temp_units == "F":
            raise ValueError("Error: incompatible temperature unit. Conversion units must be Celsius or Kelvin.")


        # Return output as list if a list was provided
        if islist:
            new.temp_values = list(new.temp_values)
            return new
        # Otherwise return as-is
        else:
            return new


    # Organized printing of output for easy visualization
    def print_nice_output(self, orig_values, orig_units, multiple_input = False):  
        """ 
        This function prints the given original temperature values and the converted values.

        Input: 
        orig_values - original temperature values (list, array, or single number - float or int)
        orig_units  - original units (string; 'C', 'K', or 'F')
        multiple_input - set to true if temperature values are passed as a list or array, false if single
        number

        Output:
        Original and converted temperature values will be printed to the console.

        """
       # Do this if temperature values are type list or array
        if multiple_input:
            # Print original values
            print('Original temps were:') 
            for i in range(len(orig_values)):
                print('{0:3.2f}'.format(orig_values[i]), orig_units) 
            
            #Print converted values
            print('New temps are:')
            for i in range(len(self.temp_values)):
                print('{0:3.2f}'.format(self.temp_values[i]), self.temp_units)
        
        # Do this if single temperature value
        else: 
            # Print original and converted values
            print('Original temp was {0:3.2f}'.format(orig_values) + orig_units
            + ', new temp is {0:3.2f}'.format(self.temp_values) + self.temp_units + '.')
        # Add white space for readability
        print('\n')

# Below are examples demonstrating the functionality of the temp_array class

# Run this code if this is the main script
if __name__ == "__main__":

  # Example of functionality with a single temperature value

    # Create class instance
    temp = temp_array(50, 'C')
    # Convert to new units
    temp_in_K = temp.tempconvert('K')
    # Print output 
    temp_in_K.print_nice_output(temp.temp_values, temp.temp_units)


  # Example of functionality with an array of temperatures 

    # Create class instance
    temp_arr = temp_array(np.asarray([50., 60., 70., 80.]), 'F')
    # Convert to new units
    temp_arr_in_C = temp_arr.tempconvert('C')
    # Print output
    temp_arr_in_C.print_nice_output(temp_arr.temp_values, temp_arr.temp_units, multiple_input = True)


  # Example of functionality with a list of temperatures

    # Create class instance
    temp_list = temp_array([300., 270., 250., 299.], 'K')
    # Convert to new units
    temp_list_in_C = temp_list.tempconvert('C')
    # Print output
    temp_list_in_C.print_nice_output(temp_list.temp_values, temp_list.temp_units, multiple_input = True)

