import pyperclip,string,random,flet as fl
def main(page:fl.Page):
    def xit(e):
        page.window_destroy()
    def copy(e):
        pyperclip.copy(generated.value)
        copied.value='COPIED'
        copied.update()
    def generate(e):
        copied.value=''
        copied.update()
        generated.value=''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(8))
        page.update()
    page.window_width=500
    page.window_height=220
    page.theme_mode=fl.ThemeMode.LIGHT
    copied=fl.Text()
    generated=fl.TextField(label='GENERATED',disabled=True)
    page.add(fl.Text('RANDOM PASSWORD GENERATOR'),
             fl.ElevatedButton('GENERATE',on_click=generate),
             fl.Row(controls=[generated,fl.IconButton(icon=fl.icons.CONTENT_COPY,on_click=copy),copied]),
             fl.ElevatedButton('EXIT',on_click=xit))
fl.app(target=main)
