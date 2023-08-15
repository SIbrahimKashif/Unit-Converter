import PySimpleGUI as sg


def km_to_mile(km):
    return round(float(km) * 0.6214, 2)


def mile_to_km(miles):
    return round(float(miles) / 0.6214, 2)


def kg_to_lb(kg):
    return round(float(kg) * 2.20462, 2)


def lb_to_kg(lbs):
    return round(float(lbs) / 2.20462, 2)


b_size = (15, 1)
font_name = "Segoe UI Light"

layout = [
    [
        sg.Spin(
            ["km", "kg", "miles", "lbs"],
            key="from",
            size=b_size,
            expand_x=True,
            text_color="#312D2B",
            background_color="#F2EEEE",
            font=(font_name, "15"),
        ),
        sg.Button(
            "<>",
            key="convert",
            size=(3, 1),
            button_color=("black", "#F2EEEE"),
            font=(font_name, "10"),
        ),
        sg.Spin(
            ["miles", "lbs", "km", "kg"],
            key="to",
            size=b_size,
            expand_x=True,
            text_color="#312D2B",
            background_color="#F2EEEE",
            font=(font_name, "15"),
        ),
    ],
    [sg.Input(key="input", expand_x=True)],
    [
        sg.Text(
            "Output",
            key="output",
            expand_x=True,
            justification="center",
            font=(font_name, "15"),
        )
    ],
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "convert":
        value = values["input"]
        if value.isnumeric():
            unit_from = values["from"]
            unit_to = values["to"]

            if unit_from == "km" and unit_to == "miles":
                output = km_to_mile(value)
            elif unit_from == "miles" and unit_to == "km":
                output = mile_to_km(value)
            elif unit_from == "kg" and unit_to == "lbs":
                output = kg_to_lb(value)
            elif unit_from == "lbs" and unit_to == "kg":
                output = lb_to_kg(value)
            else:
                output = "Error: Invalid conversion"

            window["output"].update(f"{output}")
        else:
            window["output"].update("Error: Please enter a number")

    elif event == "clear":
        window["output"].update('')
        window["input"].update('')

window.close()
