import flet as ft

def main(page:ft.Page):

    # Align the calculator to the center of the window

    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    
    # Changes the sign of the equation
    
    def sign_change(e):
        eqn.value="-"+"("+eqn.value+")"
        page.update()
        
    # Displays the equation

    def display(e):
        eqn.value+=e.control.text
        page.update()

    # Calculates the final result of the equation
    
    def calc_op(e):
        result.value=eval(eqn.value)
        page.update()
    
    # Clears the equation and Result Text Fields
    
    def clear_op(e):
        result.value=eqn.value=""
        page.update()
    
    # Deletes the last character from the equation
        
    def delete_op(e):
        s=eqn.value
        s=s[:-1]
        eqn.value=s
        page.update()
        
    result=ft.TextField(label="Result")
    eqn=ft.TextField()
    
    zero_btn=ft.FilledTonalButton(text="0",on_click=display,width=100)
    one_btn=ft.FilledTonalButton(text="1",on_click=display,width=100)
    two_btn=ft.FilledTonalButton(text="2",on_click=display,width=100)
    three_btn=ft.FilledTonalButton(text="3",on_click=display,width=100)
    four_btn=ft.FilledTonalButton(text="4",on_click=display,width=100)
    five_btn=ft.FilledTonalButton(text="5",on_click=display,width=100)
    six_btn=ft.FilledTonalButton(text="6",on_click=display,width=100)
    seven_btn=ft.FilledTonalButton(text="7",on_click=display,width=100)
    eight_btn=ft.FilledTonalButton(text="8",on_click=display,width=100)
    nine_btn=ft.FilledTonalButton(text="9",on_click=display,width=100)
    
    sign_change_btn=ft.OutlinedButton(text="+/-",on_click=sign_change,width=100)
    dec_btn=ft.OutlinedButton(text=".",on_click=display,width=100)
    sum_btn=ft.OutlinedButton(text="+",on_click=display,width=100)
    diff_btn=ft.OutlinedButton(text="-",on_click=display,width=100)
    prod_btn=ft.OutlinedButton(text="*",on_click=display,width=100)
    div_btn=ft.OutlinedButton(text="/",on_click=display,width=100)
    mod_btn=ft.OutlinedButton(text="%",on_click=display,width=100)
    
    calc_btn=ft.FilledButton(text="=",on_click=calc_op,width=100)
    clear_btn=ft.FilledButton(text="AC",on_click=clear_op,width=100)
    delete_icon=ft.FilledButton(text="C",on_click=delete_op,width=100)
    
    page.add(
        ft.Container(
            content=ft.Column([
                result,eqn,
                ft.Row(controls=[clear_btn,delete_icon,div_btn,sign_change_btn]),
                ft.Row(controls=[seven_btn,eight_btn,nine_btn,prod_btn]),
                ft.Row(controls=[four_btn,five_btn,six_btn,diff_btn]),
                ft.Row(controls=[one_btn,two_btn,three_btn,sum_btn]),
                ft.Row(controls=[mod_btn,zero_btn,dec_btn,calc_btn])
                ]),
            margin=10,
            padding=10,
            bgcolor=ft.colors.GREY_200,
            border_radius=10,
            width=450
            )
        )
ft.app(target=main)
