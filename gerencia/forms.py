from django import forms
from .models import Noticia, Categoria

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'texto': forms.Textarea(attrs={'class': 'form-control'}),  
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
            'image': forms.FileInput(attrs={'class': 'form-control'}), 
            'categoria': forms.Select(attrs={'class': 'form-control'}),

        }

class CategoriaForm(forms.ModelForm):
        
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}), 
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError("O nome da categoria é obrigatório.")
        
        # Verifica se já existe uma categoria com o mesmo nome
        if Categoria.objects.filter(nome__iexact=nome).exists():
            raise forms.ValidationError("Uma categoria com este nome já existe.")
        
        return nome


from django import forms
from .models import Categoria
from usuarios.models import UserBlog  # Importe o modelo de usuário personalizado

class NoticiaFilterForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        required=False,
        label='Título',
        widget=forms.TextInput(attrs={'placeholder': 'Digite o título','class': 'form-control'})
    )
    data_publicacao_inicio = forms.DateField(
        required=False,
        label='Data de Publicação (Início)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_publicacao_fim = forms.DateField(
        required=False,
        label='Data de Publicação (Fim)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label='Categoria',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
  
class CategoriaFiltroForm(forms.Form):
    nome = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome da categoria'
        })
    )