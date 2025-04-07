from jinja2 import Environment, FileSystemLoader
import os

class TemplateEmail:
    def __init__(self):
        # Caminho absoluto até a pasta 'templates'
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Vai até 'app'
        templates_dir = os.path.join(base_dir, "templates")  # app/templates
        print("📁 Template está procurando em:", templates_dir)  # opcional para debug

        self.env = Environment(loader=FileSystemLoader(templates_dir))

    def gerar_html_email(self, dados_erros, dados_qtd, dados_diferenca):
        template = self.env.get_template("email.html")
        html_email = template.render(
            erros=dados_erros.to_dict(orient="records"),
            quantidade=dados_qtd.to_dict(orient="records"),
            diferenca=dados_diferenca.to_dict(orient="records")
        )
        
        # Salvar prévia do HTML
        self.salvar_previa_html(html_email)
        
        return html_email


    def salvar_previa_html(self, html):
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output")
        os.makedirs(output_dir, exist_ok=True)
        preview_path = os.path.join(output_dir, "email_preview.html")

        try:
            with open(preview_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"✅ Prévia do e-mail salva em: {preview_path}")
        except Exception as e:
            print(f"❌ Erro ao salvar a prévia do e-mail: {e}")
