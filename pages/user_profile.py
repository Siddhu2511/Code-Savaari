import flet as ft
def user_profile(page:ft.Page):
    heading = ft.Text(value="Profile", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.colors.ORANGE,
                      font_family="Merienda-Bold")
    page.add(
        ft.Column(
            controls=[heading]
        ),
        ft.Image(src="/uploads/<some-uploaded-picture.png>")
    ),
ft.app(target=user_profile, assets_dir="assets",upload_dir="assets/uploads")
