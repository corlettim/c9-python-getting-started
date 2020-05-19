#The enable_pin method is not coded yet
# I have created a dummy method so the code
# will run without an error
# Don't panic if you don't understand this part of the code
# we cover methods in a separate module
def enable_pin(user, pin):
    print('pin enabled')

# Set current_user and pin to test values
current_user = 'TEST123'
pin = '123456'

# Enable PIN check as listed in
# security requirements
enable_pin(current_user, pin)
# remember that the name of the value you are passing through does not matter
# it will fill in the parameter in the method name since a parameter is a place
# holder for whatever value is being passed through
