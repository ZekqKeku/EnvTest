import os
import sys
import customtkinter as ctk
from dotenv import load_dotenv

if hasattr(sys, '_MEIPASS'):
    env_path = os.path.join(sys._MEIPASS, '.env')
else:
    env_path = '.env'

load_dotenv(dotenv_path=env_path)

api_key = os.getenv("API_KEY", "Brak klucza w pliku .env")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x200")
app.title("Aplikacja Env Test")

label = ctk.CTkLabel(app, text=f"Wiadomość:\n{api_key}", font=("Arial", 16))
label.pack(expand=True, pady=20)

close_button = ctk.CTkButton(app, text="Zamknij", command=app.destroy)
close_button.pack(side="bottom", pady=20)

if __name__ == "__main__":
    app.mainloop()
