from pyscript import document


def runCalculate(event):
    input_text = document.querySelector("#calc")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = test
