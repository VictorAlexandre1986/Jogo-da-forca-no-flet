import flet as ft
import string 
import random
"""
    BreakPoint  Dimension
    xs          <576px
    sm          >=576
    md          >=768
    lg          >=992
    xl          >=1200
    xxl         >=1400
"""
def main(page: ft.Page):
    page.bgcolor = ft.colors.BROWN_600

    scene = ft.Image(col=12, src='images/scene.png')
    



    victim = ft.Image(
        data = 0,
        src = 'images/hangman_0.png',
        repeat = ft.ImageRepeat.NO_REPEAT,
        height=300
    )

    available_words = ['python','flet','programador']
    choiced = random.choice(available_words).upper()

    word = ft.Row(
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls = [ letter_to_guess('_') for letter in choiced ]
    )

    def validate_letter(evento):
        for pos, letter in enumerate(choiced):
            if evento.control.content.value == letter:
                word.controls[pos] = letter_to_guess(letter=letter)
                word.update()
        
        if evento.control.content.value not in choiced:
            victim.data += 1

            
            if victim.data > 7:
                page.dialog = ft.AlertDialog(title=ft.Text(value='Você perdeu!'), open=True )
                page.update()

            errors = victim.data
            victim.src = f'images/hangman_{errors}.png'
            victim.update()
        
        evento.control.disabled=True
        evento.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        evento.control.update()

    game = ft.Container(
        col={'xs':12, 'lg':6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word
            ]
        )
    )

    keyboard = ft.Container(
        col={'xs':12, 'lg':6},
        image_src='images/keyboard.png',
        image_repeat= ft.ImageRepeat.NO_REPEAT,
        image_fit = ft.ImageFit.FILL,
        padding = ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    # bgcolor= ft.colors.ORANGE
                    gradient =ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end= ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE]
                    ),
                    on_click=validate_letter
                ) for letter in string.ascii_uppercase ]
        )
    )
    
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            scene,
            game,
            keyboard,
            scene
        ]
    )

    page.add(layout)

def letter_to_guess(letter):
    return ft.Container(
                bgcolor = ft.colors.AMBER_500,
                height = 50,
                width = 50,
                border_radius = ft.border_radius.all(5),
                content=ft.Text(
                    value=letter,
                    color=ft.colors.WHITE,
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD
                )
            )

if __name__=='__main__':
    ft.app(target = main, assets_dir='assets')