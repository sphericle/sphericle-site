from pyscript import document


# Assuming you have imported document from pyscript

input_element = document["calc"]
output_div = document["output"]

if input_element and output_div:
    input_text = input_element.value.strip()  # Remove leading/trailing whitespace
    if input_text:  # Check if input_text is not empty
        input_number = float(input_text)
        # Perform range check
        if 0 < input_number < 1:
            run = input_number
        elif input_number <= 0:
            run = input_number / 100 if input_number > -1 else input_number
        else:
            run = input_number / 100
        seconds = run * 3600
        output_div.text = str(seconds)
    else:
        print("Input field value is empty")
else:
    print("Input element or output element not found")