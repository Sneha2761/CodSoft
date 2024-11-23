import tkinter as tk
from tkinter import messagebox

# Initialize the contacts dictionary
contacts = {}

# Function to add a new contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone Number are required.")
        return

    contacts[name] = {"phone": phone, "email": email, "address": address}
    update_contact_list()
    clear_entries()
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

# Function to update the contact list display
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name, info in contacts.items():
        listbox_contacts.insert(tk.END, f"{name} ({info['phone']})")

# Function to search for a contact
def search_contact():
    query = entry_search.get().strip().lower()
    if not query:
        messagebox.showerror("Error", "Enter a name or phone number to search.")
        return

    results = [
        name for name, info in contacts.items()
        if query in name.lower() or query in info["phone"]
    ]

    if results:
        listbox_contacts.delete(0, tk.END)
        for name in results:
            listbox_contacts.insert(tk.END, f"{name} ({contacts[name]['phone']})")
    else:
        messagebox.showinfo("Not Found", "No matching contacts found.")

# Function to load contact details into entry fields for updating
def load_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to update.")
        return

    contact_name = listbox_contacts.get(selected[0]).split(" (")[0]
    contact = contacts[contact_name]

    entry_name.delete(0, tk.END)
    entry_name.insert(0, contact_name)
    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, contact["phone"])
    entry_email.delete(0, tk.END)
    entry_email.insert(0, contact["email"])
    entry_address.delete(0, tk.END)
    entry_address.insert(0, contact["address"])

# Function to update an existing contact
def update_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone Number are required.")
        return

    if name in contacts:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
    else:
        messagebox.showerror("Error", f"Contact '{name}' does not exist.")

# Function to delete a contact
def delete_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return

    contact_name = listbox_contacts.get(selected[0]).split(" (")[0]
    del contacts[contact_name]
    update_contact_list()
    messagebox.showinfo("Success", f"Contact '{contact_name}' deleted successfully!")

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Contact Management System")
app.geometry("500x500")

# Input fields
frame_inputs = tk.Frame(app)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_inputs, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_inputs, width=30)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_inputs, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Address:").grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(frame_inputs, width=30)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# Buttons
frame_buttons = tk.Frame(app)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Add Contact", command=add_contact)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_update = tk.Button(frame_buttons, text="Update Contact", command=update_contact)
btn_update.grid(row=0, column=1, padx=5, pady=5)

btn_delete = tk.Button(frame_buttons, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=0, column=2, padx=5, pady=5)

btn_clear = tk.Button(frame_buttons, text="Clear Fields", command=clear_entries)
btn_clear.grid(row=0, column=3, padx=5, pady=5)

# Search bar
frame_search = tk.Frame(app)
frame_search.pack(pady=10)

entry_search = tk.Entry(frame_search, width=30)
entry_search.grid(row=0, column=0, padx=5, pady=5)

btn_search = tk.Button(frame_search, text="Search", command=search_contact)
btn_search.grid(row=0, column=1, padx=5, pady=5)

# Contact list display
listbox_contacts = tk.Listbox(app, width=50, height=15)
listbox_contacts.pack(pady=10)

btn_load = tk.Button(app, text="Load Selected Contact", command=load_contact)
btn_load.pack(pady=5)

# Run the application
app.mainloop()
