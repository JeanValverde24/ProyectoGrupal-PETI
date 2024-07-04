import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import webbrowser
import os

class CAMEAnalysis(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")

        self.title("Matriz CAME - TechInnovate")
        self.geometry("1000x800")
        self.configure(bg="#0077be")

        self.style = ttk.Style(self)
        self.style.configure("TFrame", background="#ffffff")
        self.style.configure("TLabel", background="#ffffff", font=('Arial', 11))
        self.style.configure("TButton", padding=10, font=('Arial', 10))
        self.style.configure("Header.TLabel", font=('Arial', 12, 'bold'), foreground="#ffffff", background="#0077be")

        main_frame = ttk.Frame(self, padding="20 20 20 20")
        main_frame.pack(expand=True, fill='both')

        ttk.Label(main_frame, text="MATRIZ CAME", style="Header.TLabel").pack(pady=(0, 20))
        ttk.Label(main_frame, text="Reflexione y anote acciones a llevar a cabo, teniendo en cuenta que estas\nacciones deben favorecer la ejecución exitosa de la estrategia general", style="Header.TLabel").pack(pady=(0, 20))

        self.create_came_table(main_frame)
        
        # Botón para abrir la versión web
        ttk.Button(main_frame, text="Abrir versión web", command=self.open_web_version).pack(pady=20)

        # Generar y abrir la versión web automáticamente
        self.generate_web_version()
        self.open_web_version()

    def create_came_table(self, parent):
        columns = ('Acciones', 'Estrategias')
        tree = ttk.Treeview(parent, columns=columns, show='headings', height=20)
        tree.pack(expand=True, fill='both')

        tree.heading('Acciones', text='Acciones')
        tree.heading('Estrategias', text='Estrategias')

        tree.column('Acciones', width=100, anchor='center')
        tree.column('Estrategias', width=800)

        came_data = [
            ('C', 'Corregir las debilidades', [
                'Implementar un programa de capacitación en nuevas tecnologías',
                'Mejorar la infraestructura de TI',
                'Optimizar los procesos internos para reducir costos'
            ]),
            ('A', 'Afrontar las amenazas', [
                'Desarrollar un plan de contingencia para ciberataques',
                'Diversificar la cartera de productos para reducir la dependencia',
                'Establecer alianzas estratégicas con proveedores clave'
            ]),
            ('M', 'Mantener las fortalezas', [
                'Continuar invirtiendo en I+D',
                'Mantener la cultura de innovación',
                'Reforzar el programa de retención de talentos'
            ]),
            ('E', 'Explotar las oportunidades', [
                'Expandir a nuevos mercados internacionales',
                'Lanzar una nueva línea de productos IoT',
                'Implementar un programa de sostenibilidad para atraer clientes conscientes'
            ])
        ]

        for category, strategy, actions in came_data:
            parent_id = tree.insert('', 'end', values=(category, strategy), tags=('category',))
            for i, action in enumerate(actions, start=1):
                tree.insert(parent_id, 'end', values=(f"{i}", action))

        tree.tag_configure('category', background='#0077be', foreground='white')

    def generate_web_version(self):
        html_content = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matriz CAME - TechInnovate</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #ffffff;
            background-color: #0077be;
            padding: 10px;
            margin: 0 0 20px 0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #0077be;
            color: white;
        }
        .category {
            background-color: #0077be;
            color: white;
            font-weight: bold;
        }
        .action {
            padding-left: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>MATRIZ CAME</h1>
        <h2>Reflexione y anote acciones a llevar a cabo, teniendo en cuenta que estas acciones deben favorecer la ejecución exitosa de la estrategia general</h2>
        
        <table id="cameTable">
            <thead>
                <tr>
                    <th>Acciones</th>
                    <th>Estrategias</th>
                </tr>
            </thead>
            <tbody>
                <!-- El contenido de la tabla se llenará con JavaScript -->
            </tbody>
        </table>
    </div>

    <script>
        const cameData = [
            {
                category: 'C',
                strategy: 'Corregir las debilidades',
                actions: [
                    'Implementar un programa de capacitación en nuevas tecnologías',
                    'Mejorar la infraestructura de TI',
                    'Optimizar los procesos internos para reducir costos'
                ]
            },
            {
                category: 'A',
                strategy: 'Afrontar las amenazas',
                actions: [
                    'Desarrollar un plan de contingencia para ciberataques',
                    'Diversificar la cartera de productos para reducir la dependencia',
                    'Establecer alianzas estratégicas con proveedores clave'
                ]
            },
            {
                category: 'M',
                strategy: 'Mantener las fortalezas',
                actions: [
                    'Continuar invirtiendo en I+D',
                    'Mantener la cultura de innovación',
                    'Reforzar el programa de retención de talentos'
                ]
            },
            {
                category: 'E',
                strategy: 'Explotar las oportunidades',
                actions: [
                    'Expandir a nuevos mercados internacionales',
                    'Lanzar una nueva línea de productos IoT',
                    'Implementar un programa de sostenibilidad para atraer clientes conscientes'
                ]
            }
        ];

        function populateTable() {
            const tableBody = document.querySelector('#cameTable tbody');
            cameData.forEach(item => {
                // Añadir fila de categoría
                const categoryRow = document.createElement('tr');
                categoryRow.innerHTML = `
                    <td class="category">${item.category}</td>
                    <td class="category">${item.strategy}</td>
                `;
                tableBody.appendChild(categoryRow);

                // Añadir filas de acciones
                item.actions.forEach((action, index) => {
                    const actionRow = document.createElement('tr');
                    actionRow.innerHTML = `
                        <td class="action">${index + 1}</td>
                        <td class="action">${action}</td>
                    `;
                    tableBody.appendChild(actionRow);
                });
            });
        }

        // Llamar a la función para llenar la tabla cuando la página cargue
        window.onload = populateTable;
    </script>
</body>
</html>
        '''
        
        with open('matriz_came.html', 'w', encoding='utf-8') as f:
            f.write(html_content)

    def open_web_version(self):
        webbrowser.open('file://' + os.path.realpath('matriz_came.html'))

if __name__ == "__main__":
    app = CAMEAnalysis()
    app.mainloop()