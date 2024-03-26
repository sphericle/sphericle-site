from pyscript import document


def runCalculate(event):
    try:
        float(input_text)
        floatCheck = True
    except ValueError:
        floatCheck = False
    if floatCheck == False:
        output_div = document.querySelector("#output")
        output_div.innerText = "not a float"
    else:
        if input_text.value > 1:
            run = input_text.value / 100
        elif input_text.value < 0:
            if input_text.value > -1:
                run = input_text.value / 100
            else:
                run = input_text
        else:
            run = input_text.value
        
        seconds = run * 3600
    
        output_div = document.querySelector("#output")
        output_div.innerText = seconds
