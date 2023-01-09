import flet as ft


# to run in debug
# flet .\Shift\01_Flet_test\main.py
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK

    page.window_height = 680
    page.window_width = 440

    page.title = 'Example clicker'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    number = ft.TextField(value='0',
                          width=100,
                          text_align=ft.TextAlign.CENTER)
    def add(e: str) -> None:
        number.value = str(int(number.value) + 1)
        page.update()

    def sub(e: str) -> None:
        if number.value != '0':
            number.value = str(int(number.value) - 1)
        page.update()

    def reset(e: str) -> None:
        number.value = '0'
        page.update()


    page.add(
        ft.Container(content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            scale=1.2,
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE,
                              icon_color=ft.colors.RED,
                              on_click=sub),
                number,
                ft.IconButton(icon=ft.icons.ADD,
                              icon_color=ft.colors.CYAN,
                              on_click=add)
            ]
        ),
            margin=14
        ),
    ft.Container(content=ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        scale=1.4,
        controls=[
            ft.IconButton(icon=ft.icons.CHANGE_CIRCLE_SHARP,
                          icon_color=ft.colors.YELLOW,
                          on_click=reset),
        ]
    ),
        margin=14)
    )

    # page.update()  #.update() is not needed when using .add()


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
