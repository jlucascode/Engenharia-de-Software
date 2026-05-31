import os
from fpdf import FPDF

def convert_to_pdf(folder_path, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Lista de extensões de código para buscar
    extensions = ('.py', '.js', '.cpp', '.h', '.java', '.txt', '.css', '.html')

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                
                pdf.add_page()
                pdf.set_font("Courier", size=8) # Fonte monoespaçada é melhor para código
                
                # Título do arquivo
                pdf.cell(0, 10, f"Arquivo: {file}", ln=True)
                pdf.ln(5)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            # Adiciona linha do código, evitando erros de caracteres especiais
                            pdf.cell(0, 5, line.encode('latin-1', 'replace').decode('latin-1'), ln=True)
                except Exception as e:
                    pdf.cell(0, 5, f"Erro ao ler arquivo: {e}", ln=True)
                    
    pdf.output(output_path)

# Uso
convert_to_pdf('caminho/para/sua/pasta/de/codigos', 'todos_os_codigos.pdf')
