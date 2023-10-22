import flet as ft
import sys

sys.path.append("..")
from utils import fonts
from utils import views

def welcome_screen(page: ft.Page):
    page.theme_mode = "light"
    page.padding = 0
    page.window_width = 380
    page.window_height = 700
    page.window_max_width = 380
    page.window_height = 700
    page.fonts = fonts.fonts
    heading = ft.Text(
        value="WasteZeroConnect",
        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        color=ft.colors.WHITE,
        font_family="Poppins-Bold"
    )
    moto = ft.Text(
        value="Connecting Communities, Eradicating Waste: Together, We Nourish a Sustainable Future.",
        style=ft.TextThemeStyle.TITLE_MEDIUM,
        color=ft.colors.WHITE70,
        font_family="Poppins-Regular"
    )

    def route_change():
        page.views.clear()
        page.views.append(
            views.views_handler()['/home']
        )

    page.on_route_change = route_change

    def login(e):
        print("enthu")
        page.go('/home')

    page.add(
        ft.Container(
            ft.Column(
                controls=[heading,
                          moto,
                          ft.OutlinedButton(text="LOGIN",on_click=login),
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


