# Addition and Clear operation

import flet as ft

def main(page:ft.Page):
    num1=ft.TextField(label="Enter first number")
    num2=ft.TextField(label="Enter second number")
    Sum=ft.TextField()
    def sum_op(e):
        Sum.value=int(num1.value)+int(num2.value)
        page.update()
    plus_btn=ft.ElevatedButton(text="+",on_click=sum_op)
    def clear_op(e):
        num1.value=""
        num2.value=""
        Sum.value=""
        page.update()
    clear_btn=ft.ElevatedButton(text="AC",on_click=clear_op)
    page.add(ft.Row(controls=[num1,num2,plus_btn,clear_btn,Sum]))

ft.app(target=main)