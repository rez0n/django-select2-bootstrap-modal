from .models import Post
from bootstrap_modal_forms.forms import BSModalModelForm
from django_select2 import forms as s2forms

class CategoryPickWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]



class PostCategoryForm(BSModalModelForm):
    class Meta:
        model = Post
        fields = ['category',]
        widgets = {
            "category": CategoryPickWidget(select2_options={'width': '100%', }),
        }
