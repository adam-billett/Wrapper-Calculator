
import customtkinter as ctk


def calculate_wrapping_paper_dimensions(length, width, height):
    wrapping_paper_length = 2 * (length + width) + min(length, width)
    wrapping_paper_width = 2 * (width + height) + min(width, height)
    return wrapping_paper_length, wrapping_paper_width


def calculate_and_display():
    # Retrieve values from entry widgets
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_entry.get())

    # Calculate wrapping paper dimensions
    wrapping_paper_length, wrapping_paper_width = calculate_wrapping_paper_dimensions(length, width, height)

    # Update result label
    result_label.configure(text=f"For this gift, cut a piece of wrapping paper with dimensions:\n"
                             f"Length: {wrapping_paper_length} inches\n"
                             f"Width: {wrapping_paper_width} inches")


# Create the main application window
root = ctk.CTk()
root.title("Gift Wrapping Calculator")

# Create and place labels and entry widgets for dimensions
length_label = ctk.CTkLabel(root, text="Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = ctk.CTkEntry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

width_label = ctk.CTkLabel(root, text="Width:")
width_label.grid(row=1, column=0, padx=10, pady=10)
width_entry = ctk.CTkEntry(root)
width_entry.grid(row=1, column=1, padx=10, pady=10)

height_label = ctk.CTkLabel(root, text="Height:")
height_label.grid(row=2, column=0, padx=10, pady=10)
height_entry = ctk.CTkEntry(root)
height_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place a button to calculate dimensions
calculate_button = ctk.CTkButton(root, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place a label to display the result
result_label = ctk.CTkLabel(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
