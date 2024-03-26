from pyscript import document


def runCalculate(event):
    input_text = float(document.querySelector("#calc").getAttribute("value"))
    
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
