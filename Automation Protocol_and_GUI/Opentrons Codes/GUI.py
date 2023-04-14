import PySimpleGUI as psg
import os

# Set up the GUI
layout = [
    [psg.Text("Enter number of bacterial samples (between 1 and 96 samples): "), psg.InputText(key="samples")],
    [psg.Button("Save")]
]

window = psg.Window('Input Form', layout)

# Read the protocol file
protocol_file = "Full protocol_v3.py"
with open(protocol_file, 'r') as f:
    protocol_lines = f.readlines()

# Display the GUI and wait for user input
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == 'Save':
        # Validate the user input
        try:
            num_samples = int(values['samples'])
            if num_samples < 1 or num_samples > 96:
                raise ValueError()
        except ValueError:
            psg.popup('Please enter a number between 1 and 96.')
            continue
        
        # Modify the protocol file with the user input
        new_lines = []
        for line in protocol_lines:
            if 'samples =' in line:
                line = f'samples = {values["samples"]}'
            new_lines.append(line)
        with open(protocol_file, 'w') as f:
            f.writelines(new_lines)
        psg.popup('Your input has been saved!')

window.close()
