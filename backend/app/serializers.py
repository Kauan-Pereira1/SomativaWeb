from rest_framework import serializers
from .models import *


class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True

class CategoriaLivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaLivros
        fields = '__all__'
        many = True

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        nome = UsuarioCustomizadoSerializer(read_only=True)
        fields = '__all__'
        many = True

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Foto
        fields = '__all__'
        many = True

class LivrosSerializer(serializers.ModelSerializer):
    #fotos = FotoSerializer(read_only=True) #fazer o join com tabelas separadas
    fotos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    ) #join com many to many field
    categoriaFK = CategoriaLivrosSerializer(read_only=True)
    autorFK = AutorSerializer(read_only=True)
    class Meta:
        model = Livros
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        many = True

class EmprestimoLivrosSerializer(serializers.ModelSerializer):
    livroFK = LivrosSerializer

    class Meta:
        many = True
        model = EmprestimoLivros
        fields = '__all__'