from pyscript import document


input_element = document.querySelector("#calc")
if input_element:
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
        output_div = document.querySelector("#output")
        output_div.innerText = seconds
    else:
        print("Input field value is empty")
else:
    print("Input element with ID 'calc' not found")
