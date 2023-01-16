# 1. Old form def __init__(self, *args, **kwargs):

def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            #print(field)
            new_data = {
                "placeholder": f"Recipe {str(field)}",
                "class": 'form-control',
                "hx-post": ".",
                "hx-trigger": "keyup change delay:500ms",
                "hx-target": "#recipe-container",
                "hx-swap": "outerHTML",
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        # self.fields['name'].label = ''
        # self.fields['name'].widget.attrs.update({"class": "form-control", "placeholder": "Recipe name"})
        self.fields['description'].widget.attrs.update({"rows": 2})
        self.fields['directions'].widget.attrs.update({"rows": 4})