# Script written by Jamil Matheny

import customtkinter
import random
from tkinter import filedialog, END

# Custom theme settings
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class CashFive(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Title
        self.title("Cash 5 Lottery | Random Number Generator")
        self.geometry('450x200')
        self.resizable(False, False)
        self.grid()

        # Create multiple frame
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frames
        frame_left = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        frame_left.grid(row=0, column=0, sticky="nswe")

        frame_right = customtkinter.CTkFrame(master=self)
        frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # Label
        label_left = customtkinter.CTkLabel(master=frame_left, text="Cash 5 Lottery", font=customtkinter.CTkFont(weight="bold", size=18), justify=customtkinter.LEFT)
        label_left.place(relx=0.5, rely=0.15, anchor="center")

        # Buttons
        button_left = customtkinter.CTkButton(master=frame_left, text="Generate Numbers", command=self.display_numbers)
        button_left.place(relx=0.5, rely=0.35, anchor="center")

        # Buttons
        button_right = customtkinter.CTkButton(master=frame_right, text="Save As", command=self.save_file_as)
        button_right.place(relx=0.5, rely=0.8, anchor="center")

        # Text inside the textbox
        self.entry_right = customtkinter.CTkEntry(master=frame_right, width=210, height=40, font=customtkinter.CTkFont(size=18))
        self.entry_right.pack(pady=30, padx=10)

        # Appearances
        self.appearance_mode_label = customtkinter.CTkLabel(master=frame_left, text="Appearance Mode:")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label.place(relx=0.5, rely=0.6, anchor="center")
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(master=frame_left, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionmenu.place(relx=0.5, rely=0.75, anchor="center")

    # Generating random numbers
    def generate_numbers(self):
        numbers = []
        while len(numbers) < 5:
            new_number = random.randint(1, 41)
            if new_number not in numbers:
                numbers.append(new_number)
        numbers.sort()
        return numbers

    # Display the random numbers in the textbox
    def display_numbers(self):
        numbers = self.generate_numbers()
        numbers_string = ",   ".join(str(n) for n in numbers)
        self.entry_right.delete(0, END)
        self.entry_right.insert(END, numbers_string)

    # The change user appearance mode function
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Function on saving the file document and checking whether the user will save the data or not.
    def save_file_as(self):
        filename = filedialog.asksaveasfilename(initialdir="r(C:\Documents", title="Save File As", defaultextension=".txt", filetypes=(('Text Documents,' '.txt*'), ("All Files", '*.*')))
        if filename:
            textcontent = str(self.entry_right.get())
            with open(filename, 'w+') as file:
                file.write(textcontent)
            print("File saved as ", filename)
        else:
            print("File save has been cancelled")

# This is run the script directly. Not when the script is imported from one module to another script.
if __name__ == "__main__":
    root = CashFive()
    root.mainloop()
