from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'category')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name').split()
        for word in self.ban_words:
            if word in cleaned_data:
                raise forms.ValidationError('Недопустимое слово в имени')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description').split()
        for word in self.ban_words:
            if word in cleaned_data:
                raise forms.ValidationError('Недопустимое слово в описании')
        return cleaned_data
