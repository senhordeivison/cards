import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    images = [
        "images/Poster1.jpg",
        "images/Poster2.jpg",
        "images/Poster3.jpg",
        "images/Poster4.jpg",
        "images/Poster5.jpg",
        "images/Poster6.jpg",
        "images/Poster7.jpg",
        "images/Poster8.jpg",
        "images/Poster9.jpg",
        "images/Poster10.jpg",
        "images/Poster11.jpg",
        "images/Poster12.jpg",
    ]

    def change_posters():
        for poster in posters.controls:
            poster.content.offset.x += poster.data * 0.2
            poster.content.scale.scale -= poster.data * 0.1
            poster.content.opacity -= poster.data * 0.3

        posters.update()

    def handle_dismiss(e):
        for num, poster in enumerate(posters.controls):
            if e.control == posters.controls[0]:
                posters.controls.clear()
                posters.controls.extend([
                    ft.Dismissible(
                        content=ft.Container(
                            image_src=img,
                            border_radius=ft.border_radius.all(10),
                            image_fit=ft.ImageFit.COVER,
                            aspect_ratio=9 / 16,
                            offset=ft.Offset(x=0, y=0),
                            scale=ft.Scale(scale=1),
                            opacity=1,
                            shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.BLACK),
                            animate=ft.Animation(duration=300, curve=ft.AnimationCurve.DECELERATE),
                            animate_offset=True,
                            animate_scale=True,
                            animate_opacity=True,
                        ),
                        data=pos,
                        on_dismiss=handle_dismiss
                    ) for pos, img in reversed(list(enumerate(images)))
                ])
                break

            poster.data -= 1
            poster.content.offset.x = 0
            poster.content.opacity = 1
            poster.content.scale.scale = 1

        change_posters()

    posters = ft.Stack(
        height=500,
        controls=[
            ft.Dismissible(
                content=ft.Container(
                    image_src=img,
                    border_radius=ft.border_radius.all(10),
                    image_fit=ft.ImageFit.COVER,
                    aspect_ratio=9 / 16,
                    offset=ft.Offset(x=0, y=0),
                    scale=ft.Scale(scale=1),
                    opacity=1,
                    shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.BLACK),
                    animate=ft.Animation(duration=300, curve=ft.AnimationCurve.DECELERATE),
                    animate_offset=True,
                    animate_scale=True,
                    animate_opacity=True,
                ),
                data=pos,
                on_dismiss=handle_dismiss
            )
            for pos, img in reversed(list(enumerate(images)))
        ],
    )
    layout = ft.Row(controls=[posters], alignment=ft.MainAxisAlignment.CENTER)
    page.add(layout)


    change_posters()



ft.app(target=main, assets_dir="assets")
