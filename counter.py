import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            background=ft.colors.WHITE,
            primary=ft.colors.BLUE,
            secondary=ft.colors.BLUE,
    ))

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            #page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")


    container = ft.Container(
    width=200,
    height=200,
    #border=ft.border.all(1, ft.colors.BLACK),
    content=ft.FilledButton("Primary color"),
    theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.YELLOW)))

    page.add(container)

    # Inherited theme with primary color overridden
    container2 = ft.Container(
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PINK)),
        content=ft.ElevatedButton("Inherited theme button"),
        bgcolor=ft.colors.SURFACE_VARIANT,
        padding=20,
        width=500,
    )

    page.add(
        container2,
        ft.Row( 
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            # background=ft.colors.SURFACE_VARIANT,
            #theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE)),
        )
    )
    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))


ft.app(target=main)