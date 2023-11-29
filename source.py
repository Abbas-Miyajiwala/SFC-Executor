import subprocess
import customtkinter as ctk
import threading
import os

baseFont = 'Roboto Slab'
# Create Root window
root = ctk.CTk()
root.geometry('750x500')
root.title('SFC Executor v1.0 ~AM')

# Command functions:
def runSfc():
    outputBox.delete(1.0,ctk.END)
    execLabel.configure(text='Executing the sfc command....')
    
    # Start the progress bar
    progressbar.pack()
    progressbar.start()

    if os.name == 'nt':
        # For windows
        creationFlag = subprocess.CREATE_NO_WINDOW
    else:
        # For other operating Systems
        creationFlag = 0
    result = subprocess.run(['sfc', '/scannow'], stdout=subprocess.PIPE,creationflags=creationFlag)
    
    # Stop and delete the progressbar
    progressbar.stop()
    progressbar.pack_forget()
    
    # Display whether the command executed successfully or not
    if result.returncode == 0:
        outLabel.configure(text='sfc.exe command executed successfully!',text_color='green')
    else:
        outLabel.configure(text='Error in executing the sfc command!!',text_color='red')
    
    # Display the console output in the text widget (textbox)
    output = result.stdout.decode('utf-8').strip()
    outputBox.pack(pady=10)
    for line in output:
        outputBox.insert(ctk.END,line)
    # print(result.stdout)
    
def runSfcThreaded():
    # Run the function in a separate thread
    threading.Thread(target=runSfc).start()
    
# Create some content
# Header Label
header = ctk.CTkLabel(root, text='Python app to run the sfc command!!',font=(baseFont,24))
header.pack(pady=20)
# Run Button
run_button = ctk.CTkButton(root, text='Run',font=(baseFont,18),command=runSfcThreaded)
run_button.pack(pady=20)
# Label to display some execution related text
execLabel = ctk.CTkLabel(root,text='',font=(baseFont,14))
execLabel.pack(pady=20)
# Label to display whether execution was successful or not
outLabel = ctk.CTkLabel(root,text='',font=(baseFont,14))
outLabel.pack(pady=10)
# Progressbar to keep the user engaged (starts and stops according to the command execution)
progressbar = ctk.CTkProgressBar(root,orientation='horizontal',mode='indeterminate')
# Textbox o display console output
outputBox = ctk.CTkTextbox(root, width=400, wrap='word')

# Run the app
root.mainloop()