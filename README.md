# Cash 5 Lottery Random Number Generator
A random number generator for the Cash Five lottery game. This script uses the 'customtkinter' GUI library, which is subsidiary of the standard tkinter library built-in Python. The script consists of a 'Generate Numbers' button that generates 5 random numbers between 1 and 41 and sorts them to be displayed in an entry text box. 


 # Generating random numbers
 ```Python
    def generate_numbers(self):
        numbers = []
        while len(numbers) < 5:
            new_number = random.randint(1, 41)
            if new_number not in numbers:
                numbers.append(new_number)
        numbers.sort()
        return numbers
```

In addition, the application includes a save button labeled 'Save As' to store the 5 generated random numbers in a text file with using the filedialog library built-in Python. 

```Python
    def save_file_as(self):
        filename = filedialog.asksaveasfilename(initialdir=r"C:\Documents", title="Save File As", defaultextension=".txt", filetypes=(('Text Documents,' '.txt*'), ("All Files", '*.*')))
        if filename:
            textcontent = str(self.entry_right.get())
            with open(filename, 'w+') as file:
                file.write(textcontent)
            print("File saved", filename)
        else:
            print("File save has been cancelled")
```

## Here's a video demo of the application
https://user-images.githubusercontent.com/36749450/213258932-96a9463c-6f99-407a-bd77-b795b7eb1f51.mp4


