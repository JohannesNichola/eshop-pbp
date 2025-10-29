from django.forms import ModelForm
from main.models import Products
from django.utils.html import strip_tags

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
    
    def clean_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)
        