import tkinter as tk

def enter_no(button, other_button):
  # Change labels on hover (entering the button)
  button.config(text="Yes")
  other_button.config(text="No")

def leave_no(button, other_button):
  # Change labels back on leaving the button
  button.config(text="No")
  other_button.config(text="Yes")

window = tk.Tk()
window.title("Do You Love Me?")

# Create the message label
message = tk.Label(window, text="Do you love me?", font=("Arial", 16))
message.pack(padx=20, pady=20)

# Create the "Yes" button
yes_button = tk.Button(window, text="Yes", font=("Arial", 12))
yes_button.pack(padx=10, pady=10)

# Create the "No" button with hover effect
no_button = tk.Button(window, text="No", font=("Arial", 12))

# Bind functions for hover events
no_button.bind("<Enter>", lambda event: enter_no(no_button, yes_button))
no_button.bind("<Leave>", lambda event: leave_no(no_button, yes_button))

no_button.pack(padx=10, pady=10)

window.mainloop()
