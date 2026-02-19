# A dictionary of example settings for testing
test_settings = {
    'theme': 'dark',
    'noticiations': 'enabled',
    'volume': 'high'
}


# ADD SETTING -----
def add_setting(settings, pair):
    key, value = pair            # unpack the tuple into key and value

    key = key.lower()            # convert key to lowercase
    value = value.lower()        # convert value to lowercase

    if key in settings:          # check if the key already exists
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value        # add the new key-value pair
    return f"Setting '{key}' added with value '{value}' successfully!"


# UPDATE SETTING -----
def update_setting(settings, pair):
    key, value = pair            # unpack the tuple
    key = key.lower()            # lowercase key
    value = value.lower()        # lowercase value

    if key in settings:          # if the key exists, update it
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:                        # if it doesn't exist, return error
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# DELETE SETTING -----
def delete_setting(settings, key):
    key = key.lower()            # convert key to lowercase

    if key in settings:          # if the key exists, delete it
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:                        # otherwise return error
        return "Setting not found!"


# VIEW SETTINGS -----
def view_settings(settings):
    if not settings:             # if dictionary is empty
        return "No settings available.\n"   # must end with newline for tests

    result = "Current User Settings:"       # header line

    # loop through each key-value pair
    for key, value in settings.items():
        result += f"\n{key.capitalize()}: {value}"   # capitalize key, keep value as-is

    return result + "\n"          # requires a newline at the end
