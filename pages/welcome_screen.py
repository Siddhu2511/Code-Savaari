import flet as ft
import math


def welcome_screen(page: ft.Page):
    page.theme_mode = "light"
    page.padding = 0
    page.window_width = 380
    page.window_height = 700
    page.window_max_width = 380
    page.window_height = 700
    page.fonts = {
        "Merienda-Bold": "fonts/Merienda/Merienda-Bold.ttf"
    }
    heading = ft.Text(
        value="WasteZeroConnect",
        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        color=ft.colors.WHITE,
        font_family="Merienda-Bold"
    )
    moto = ft.Text(
        value="Connecting Communities, Eradicating Waste: Together, We Nourish a Sustainable Future.",
        style=ft.TextThemeStyle.TITLE_MEDIUM,
        color=ft.colors.WHITE70,
        font_family="Merienda-Bold"
    )

    page.add(
        ft.Container(
            ft.Column(
                controls=[heading,
                          moto,
                          ft.OutlinedButton(text="LOGIN"),
                          ft.Text(
                              value="Don't have an Account ?",
                              color=ft.colors.WHITE54
                          ),
                          ft.OutlinedButton(text="SIGN UP")
                          ]

            ),
            image_src="images/splash.png",
            image_fit=ft.ImageFit.COVER,
            expand=True,
            width=page.window_width,
            height=page.window_height,
            border_radius=5,
            alignment=ft.alignment.center
        )
    )
    page.update()


ft.app(target=welcome_screen, assets_dir="../assets")
