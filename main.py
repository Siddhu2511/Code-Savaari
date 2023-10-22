
import flet
from flet import Page as page

from utils import views


def route_change(route):
    flet.Page.views.clear()
    flet.Page.views.append(
        views.views_handler()['/welcome']
    )


page.on_route_change = route_change
page.go('/welcome')
