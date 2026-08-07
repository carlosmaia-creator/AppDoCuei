import flet as ft
import traceback
import sys

def main(page: ft.Page):
    page.title = "Diagnóstico Vida do Cuei"
    page.bgcolor = "#05070A"
    page.scroll = ft.ScrollMode.AUTO

    try:
        # TENTA IMPORTAR E RODAR O CÓDIGO ORIGINAL
        import os, sqlite3
        from datetime import date, datetime, timedelta

        # Se chegar aqui sem dar erro imediato, mostra avisos
        page.add(
            ft.Text("🔍 MODO DIAGNÓSTICO", size=20, color="yellow", weight="bold"),
            ft.Text("Se você está vendo esta tela, o Flet no Android ESTÁ FUNCIONANDO!", color="white"),
            ft.Text("Verificando banco de dados...", color="gray"),
        )

        try:
            PASTA_SEGURA = os.path.expanduser("~")
            teste = os.path.join(PASTA_SEGURA, ".teste_gravacao")
            with open(teste, "w") as f: pass
            os.remove(teste)
            db_path = os.path.join(PASTA_SEGURA, "life_os.db")
        except:
            db_path = os.path.join(os.getcwd(), "life_os.db")

        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS teste (id INTEGER PRIMARY KEY)")
        conn.close()

        page.add(ft.Text(f"✅ Banco de dados OK em: {db_path}", color="green"))

    except Exception as e:
        # SE QUALQUER COISA QUEBRAR, MOSTRA O ERRO EXATO NA TELA DO CELULAR
        erro_completo = traceback.format_exc()
        page.add(
            ft.Text("🚨 ERRO ENCONTRADO NO ANDROID:", size=18, color="red", weight="bold"),
            ft.Container(
                content=ft.Text(erro_completo, color="white", size=10, selectable=True),
                bgcolor="#220000",
                padding=10,
                border_radius=5
            )
        )

if __name__ == "__main__":
    ft.app(target=main)
