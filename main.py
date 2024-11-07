import customtkinter as ctk
import random

def bill_generator():
    # Generate a random bill amount between $10.5 and $570
    bill = random.uniform(10.5, 570)
    return round(bill, 2)

def calc(tip_percentage):
    global bill_amount
    # Calculate tip and total based on the selected tip percentage
    tip = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip
    info_label.configure(text=f"This is your bill: ${bill_amount}\nTip: ${round(tip, 2)}\nTotal: ${round(total, 2)}")
    return total  # Return total for use in pay function

def pay():
    global last_tip_percentage
    if last_tip_percentage is not None:
        total = calc(last_tip_percentage)  # Calculate total with the last selected tip
        # Display payment message based on the selected tip percentage
        if last_tip_percentage == 0:
            info_label.configure(text=f"Paid ${round(total, 2)} with a {last_tip_percentage}% tip. Damn you're broke.")
        elif last_tip_percentage == 30:
            info_label.configure(text=f"Paid ${round(total, 2)} with a {last_tip_percentage}% tip. Goddamn Mr Beast.")
    else:
        info_label.configure(text="Please select a tip before paying.")

def steal_payment():
    # Display message when the steal button is pressed
    info_label.configure(text="911! What's your emergency?")

window = ctk.CTk()
window.geometry('500x300')
window.title("Tip Calculator")

bill_amount = bill_generator()  # Generate initial bill amount
info_label = ctk.CTkLabel(window, text=f"This is your bill: ${bill_amount}")
info_label.pack()

frame = ctk.CTkFrame(window)
frame.pack()

last_tip_percentage = None  # Variable to store the last selected tip percentage

# Create buttons for different tip percentages
tip1 = ctk.CTkButton(frame, text="0%", width=100, height=100, command=lambda: set_tip(0))
tip1.grid(row=0, column=0, padx=2, pady=2)

tip2 = ctk.CTkButton(frame, text="5%", width=100, height=100, command=lambda: set_tip(5))
tip2.grid(row=0, column=1, padx=2, pady=2)

tip3 = ctk.CTkButton(frame, text="10%", width=100, height=100, command=lambda: set_tip(10))
tip3.grid(row=0, column=2, padx=2, pady=2)

tip4 = ctk.CTkButton(frame, text="15%", width=100, height=100, command=lambda: set_tip(15))
tip4.grid(row=1, column=0, padx=2, pady=2)

tip5 = ctk.CTkButton(frame, text="20%", width=100, height=100, command=lambda: set_tip(20))
tip5.grid(row=1, column=1, padx=2, pady=2)

tip6 = ctk.CTkButton(frame, text="30%", width=100, height=100, command=lambda: set_tip(30))
tip6.grid(row=1, column=2, padx=2, pady=2)

def set_tip(tip_percentage):
    global last_tip_percentage
    last_tip_percentage = tip_percentage
    calc(tip_percentage)  # Update the display with the selected tip

frame_decision = ctk.CTkFrame(window)
frame_decision.pack()

# Create buttons for payment and stealing
pay_button = ctk.CTkButton(frame_decision, text="Pay", height=30, width=162, command=pay)
pay_button.grid(row=0, column=0, padx=2, pady=2)

steal = ctk.CTkButton(frame_decision, text="Steal", command=steal_payment)
steal.grid(row=0, column=1, padx=2, pady=2)

window.mainloop()  # Start the application
