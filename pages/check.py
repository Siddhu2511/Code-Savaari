import flet as ft


def check(pg: ft.Page):
    pg.padding = 0
    pg.spacing = 0
    pg.theme_mode = "light"
    pg.add(
        ft.Container(
            ft.Image(
                src='images/community.png',
                visible=True
            ),
            height=500,
            width=500,
            bgcolor=ft.colors.BLACK
        )
    )
    pg.update()


ft.app(target=check, assets_dir="../assets")
