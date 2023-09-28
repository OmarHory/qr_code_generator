import tkinter as tk
from tkinter import Entry, Label, Button
from utils import generate_qr, save_qr

def run():
    img = None

    def on_generate():
        nonlocal img
        img = generate_qr(url_entry, qr_label)

    def on_save():
        save_qr(img)

    root = tk.Tk()
    root.title("Fancy QR Code Generator")
    root.geometry("500x500")

    bg_color = "#282c34"
    entry_color = "#f5f5f5"
    btn_color = "#24a19c"
    text_color = "#f5f5f5"

    root.configure(bg=bg_color)

    label_font = ("Arial", 12)
    btn_font = ("Arial", 10, "bold")

    title_label = Label(root, text="QR Code Generator", bg=bg_color, fg=text_color, font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    Label(root, text="Enter URL:", bg=bg_color, fg=text_color, font=label_font).pack(pady=10)
    url_entry = Entry(root, width=50, bg=entry_color)
    url_entry.pack(pady=10)

    generate_btn = Button(root, text="Generate QR", command=on_generate, bg=btn_color, fg=text_color, font=btn_font)
    generate_btn.pack(pady=10)

    save_btn = Button(root, text="Save QR", command=on_save, bg=btn_color, fg=text_color, font=btn_font)
    save_btn.pack(pady=10)

    qr_label = Label(root, bg=bg_color)
    qr_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run()
