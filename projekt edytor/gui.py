import sys
from tkinter import *
from tkinter import filedialog
import subprocess
import os
def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a Text File", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_widget.delete(1.0, tk.END)  # Clear previous content
            text_widget.insert(tk.END, content)

def openFile(): #funkcja dodany przez gemini
    obecny_folder = os.path.dirname(os.path.abspath(__file__))
    sciezka = os.path.join(obecny_folder, "aplikacja.py")
    
    try:
            # Zamiast 'xdg-open', wywołujemy Pythona, podając mu ścieżkę do Twojej aplikacji
        subprocess.Popen([sys.executable, sciezka])
        print("Program został pomyślnie uruchomiony w tle.")
    except Exception as e:
        print(f"Błąd podczas uruchamiania programu: {e}")

window = Tk()
window.geometry("400x300")
window.title("My GUI Application")
window.configure(bg="#000000")
bt1 = Button(window, text="create new project", font=("Arial", 24), fg="#FFFFFF", bg="#000000", command=openFile)
bt1.pack(pady=10)
bt2 = Button(window, text="open existing project", font=("Arial", 24), fg="#FFFFFF", bg="#000000", command=open_file)
bt2.pack(pady=10)
bt3 = Button(window, text="settings", font=("Arial", 24), fg="#FFFFFF", bg="#000000")
bt3.pack(pady=10)
bt4 = Button(window, text="exit", font=("Arial", 24), fg="#FFFFFF", bg="#000000", command=window.destroy)
bt4.pack(pady=10)
window.mainloop()