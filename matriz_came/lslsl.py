import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

class CAMEAnalysis(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")  # Usa un tema moderno

        self.title("Análisis CAME")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.configure("TNotebook", background="#f0f0f0")
        self.style.configure("TFrame", background="#ffffff")
        self.style.configure("TButton", padding=10, font=('Arial', 10))
        self.style.configure("TLabel", background="#ffffff", font=('Arial', 11))

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both', padx=20, pady=20)

        self.create_dafo_tab()
        self.create_came_tab()

    def create_dafo_tab(self):
        dafo_frame = ttk.Frame(self.notebook)
        self.notebook.add(dafo_frame, text='Análisis DAFO')

        labels = ['Debilidades', 'Amenazas', 'Fortalezas', 'Oportunidades']
        colors = ['#FFCCCB', '#FFFFCC', '#CCFFCC', '#CCFFFF']
        self.dafo_texts = {}

        for i, (label, color) in enumerate(zip(labels, colors)):
            frame = ttk.Frame(dafo_frame, style="TFrame")
            frame.grid(row=i//2, column=i%2, padx=10, pady=10, sticky='nsew')
            
            ttk.Label(frame, text=label, style="TLabel").pack(pady=(10,5))
            text = tk.Text(frame, height=8, width=50, wrap=tk.WORD, font=('Arial', 10),
                           bg=color, relief=tk.FLAT, padx=5, pady=5)
            text.pack(padx=10, pady=(0,10), fill=tk.BOTH, expand=True)
            self.dafo_texts[label] = text

        for i in range(2):
            dafo_frame.columnconfigure(i, weight=1)
            dafo_frame.rowconfigure(i, weight=1)

    def create_came_tab(self):
        came_frame = ttk.Frame(self.notebook)
        self.notebook.add(came_frame, text='Estrategias CAME')

        labels = ['Corregir', 'Afrontar', 'Mantener', 'Explotar']
        colors = ['#FFE5E5', '#FFFDE7', '#E8F5E9', '#E0F7FA']
        self.came_texts = {}

        for i, (label, color) in enumerate(zip(labels, colors)):
            frame = ttk.Frame(came_frame, style="TFrame")
            frame.grid(row=i//2, column=i%2, padx=10, pady=10, sticky='nsew')
            
            ttk.Label(frame, text=label, style="TLabel").pack(pady=(10,5))
            text = tk.Text(frame, height=8, width=50, wrap=tk.WORD, font=('Arial', 10),
                           bg=color, relief=tk.FLAT, padx=5, pady=5)
            text.pack(padx=10, pady=(0,10), fill=tk.BOTH, expand=True)
            self.came_texts[label] = text

        for i in range(2):
            came_frame.columnconfigure(i, weight=1)
            came_frame.rowconfigure(i, weight=1)

        button_frame = ttk.Frame(came_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        ttk.Button(button_frame, text="Generar CAME", command=self.generate_came).pack()

    def generate_came(self):
        strategies = {
            'Corregir': 'Debilidades',
            'Afrontar': 'Amenazas',
            'Mantener': 'Fortalezas',
            'Explotar': 'Oportunidades'
        }

        for came, dafo in strategies.items():
            dafo_text = self.dafo_texts[dafo].get("1.0", tk.END).strip()
            came_text = f"Estrategias para {came.lower()} las {dafo.lower()}:\n\n"
            came_text += "\n".join(f"- {line}" for line in dafo_text.split('\n') if line.strip())
            
            self.came_texts[came].delete("1.0", tk.END)
            self.came_texts[came].insert(tk.END, came_text)

        messagebox.showinfo("CAME Generado", "El análisis CAME ha sido generado basado en el DAFO.")

if __name__ == "__main__":
    app = CAMEAnalysis()
    app.mainloop()