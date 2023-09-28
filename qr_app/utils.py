import qrcode
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os

def generate_qr(url_entry, qr_label):
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "URL cannot be empty!")
        return

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    return img

def save_qr(img):
    if img is None:
        messagebox.showerror("Error", "Generate the QR code first!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

    if not file_path:
        return

    img.save(file_path)
    messagebox.showinfo("Success", f"QR code saved to {file_path}")
