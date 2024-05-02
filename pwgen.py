import string,random,flet as fl
def main(page:fl.Page):
    def xit(e):
        page.window_destroy()
    def generate(e):
        generated.value=''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(8))
        page.update()
    generated=fl.TextField(label='GENERATED',disabled=True)
    page.add(fl.Text('RANDOM PASSWORD GENERATOR'),
             fl.ElevatedButton('GENERATE',on_click=generate),
             generated,
             fl.ElevatedButton('EXIT',on_click=xit))
fl.app(target=main)