import flet
import flet as ft

import sys

sys.path.append("..")
from pages import welcome_screen
from pages import home_dashboard


def views_handler():
    return {
        '/home': ft.View(
            route='/home',
            controls=[]
        ),
        '/welcome': ft.View(
            route='/welcome',
            controls=[welcome_screen.welcome_screen(ft.Page)]
        ),
        '/community': ft.View(),
    }
