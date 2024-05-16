import flet as ft

def main(page:ft.Page):
    page.title='Contador'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_number = ft.TextField(value='0', text_align=ft.TextAlign.CENTER, width=100, disabled=True)

    def decremento(evento):
        text_number.value = str(int(text_number.value)-1)
        text_number.update()

    def incremento(evento):
        text_number.value = str(int(text_number.value)+1)
        text_number.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE, on_click=decremento),
                text_number,
                ft.IconButton(icon=ft.icons.ADD, on_click=incremento)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.update()


# if __name__=='__main__':
#     ft.app(target=main)