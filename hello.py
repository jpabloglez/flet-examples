import flet as ft

def main(page: ft.Page):
    page.title = "Flet"
    # configure background color
    page.add(ft.Text("Hello, world!"))

ft.app(main, view=ft.WEB_BROWSER)    