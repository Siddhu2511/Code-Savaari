import flet as ft
import math
def welcome_screen(page:ft.Page):
    page.theme_mode="light"
    page.window_width=400
    page.window_height=600
    page.fonts={
        "Merienda-Bold":"fonts/Merienda/Merienda-Bold.ttf"
    }
    heading = ft.Text(value="WasteZeroConnect",style=ft.TextThemeStyle.HEADLINE_MEDIUM,color=ft.colors.ORANGE,
                      font_family="Merienda-Bold")
    moto = ft.Text(value="Connecting Communities, Eradicating Waste: Together, We Nourish a Sustainable Future.", style=ft.TextThemeStyle.TITLE_MEDIUM, color=ft.colors.ORANGE,
                      font_family="Merienda-Bold")

    page.add(
        ft.Container(
            ft.Column(
                controls=[heading,
                          moto,
                          ft.OutlinedButton(text="LOGIN"),
                          ft.Text(value="Don't have an Account ?",color=ft.colors.BLACK),
                          ft.OutlinedButton(text="SIGN UP")
                ]


            ),
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(0.8, 1),
                colors=[
                    "0xff00FF00",
                    "0xff99FF99",
                    "0xffF5FFF5",
                    "0xffCCF0FF",
                    "0xff008AE6",

                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            ),
            width=page.window_width,
            height=page.window_height,
            border_radius=5,
        )
    )



ft.app(target=welcome_screen,assets_dir="assets")
