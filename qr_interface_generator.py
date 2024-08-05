import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code to a temporary file
    img.save("temp_qr.png")
    
    # Load the image and display it in the label
    qr_img = Image.open("temp_qr.png")
    qr_img = qr_img.resize((200, 200), Image.ANTIALIAS)
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

def save_qr():
    # Open file dialog to select save location
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save QR Code")
    if file_path:
        # Generate QR code
        url = entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL")
            return
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code to the selected file
        img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved to {file_path}")

# Set up the main application window
app = tk.Tk()
app.title("QR Code Generator")

# URL entry field
entry_label = tk.Label(app, text="Enter URL:")
entry_label.pack(pady=5)
entry = tk.Entry(app, width=50)
entry.pack(pady=5)

# Generate button
generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Save button
save_button = tk.Button(app, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

# Label to display the QR code
qr_label = tk.Label(app)
qr_label.pack(pady=10)

# Run the application
app.mainloop()
