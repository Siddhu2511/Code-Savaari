import flet as ft
def user_profile(page:ft.Page):
    page.add(ft.Image(src="/uploads/<some-uploaded-picture.png>"))
ft.app(target=user_profile, assets_dir="assets",upload_dir="assets/uploads")
