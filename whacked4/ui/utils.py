def validate_numeric(window):
    value = window.GetValue()
    
    if len(value) == 0:
        return 0

    # Handle negative values.        
    if value.startswith('-') == True:
        # If the value contains more than just a minus sign, attempt to get the integer value.
        if len(value) > 1:
            if value[1:].isnumeric() == False:
                value = 0
            else:
                value = int(value)
        
        # Otherwise directly return 0 as a temporary value until the user finishes entering a valid value.
        else:
            return 0
    
    else:
        # Non-numeric values are set to 0.
        if value.isnumeric() == False:
            value = 0
        
        # Others are parsed.
        else:
            value = int(value)
    
    # Update the text control if the validated value is now different.
    if str(value) != window.GetValue():
        window.ChangeValue(str(value))
        
    return value


def focus_text(event, parent):
    window = parent.FindWindowById(event.GetId())
    window.SetSelection(-1, -1)