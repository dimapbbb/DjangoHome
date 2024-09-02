from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProductForm(StyleFormMixin, forms.ModelForm):
    ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'category')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in self.ban_words:
            if word in cleaned_data.split():
                raise forms.ValidationError('Недопустимое слово в имени')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in self.ban_words:
            if word in cleaned_data.split():
                raise forms.ValidationError('Недопустимое слово в описании')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('name', 'number', 'current')
