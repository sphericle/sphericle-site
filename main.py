from pyscript import document


def runCalculate(event):
    run = float()
    try:
        input_text = float(document.querySelector("#calc"))
    except:
        output_div.innerText = "Please enter a valid run."
    if input_text.value > 1:
        run = input_text.value / 100
    elif input_text.value < 0:
        if input_text.value > -1:
        run = input_text.value / 100
    else:
        run = input_text.value
        
    seconds = run * 3600
    
    output_div = document.querySelector("#output")
    output_div.innerText = "test"
