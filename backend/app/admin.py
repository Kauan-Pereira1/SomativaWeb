from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminUsuarioCustomizado(UserAdmin):
    model=UsuarioCustomizado
    list_display = ['id', 'email', 'cpf']
    list_display_links = ('id', 'email', 'cpf',)
    fieldsets = (
        (None,{'fields': ('email','password')}),
        ('Permissions', {'fields': ('is_staff','is_active','groups','user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf','telefone','endereco',)}),
    )
    filter_horizontal = ('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2', 'is_staff','is_active','groups','user_permissions',)
        }),
    )    
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(UsuarioCustomizado,AdminUsuarioCustomizado)

class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(CategoriaLivros,AdminCategoria)

class AdminAutor(admin.ModelAdmin):
    list_display = ['id', 'nome', 'biografia', 'foto',]
    list_display_links = ('id', 'nome', 'biografia', 'foto',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Autor,AdminAutor)

class AdminLivros(admin.ModelAdmin):
    list_display = ['id', 'nome', 'categoriaFK', 'description', 'precoEmprestimo', 'quantidade', 'stars', 'autorFK', 'numeroPaginas', 'formato', 'numeroEdicao', 'anoPublicacao',]
    list_display_links = ('id', 'nome', 'categoriaFK', 'description', 'precoEmprestimo', 'quantidade', 'stars', 'autorFK', 'numeroPaginas', 'formato', 'numeroEdicao', 'anoPublicacao',)
    search_fields = ('nome',)
    list_per_page = 10
    
admin.site.register(Livros,AdminLivros)

class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['id', 'usuarioFK', 'status', 'dataHoraEmprestimo', 'dataPrevista', 'dataDevolucao',]
    list_display_links = ('id', 'usuarioFK', 'status', 'dataHoraEmprestimo', 'dataPrevista', 'dataDevolucao',)
    search_fields = ('usuarioFK',)
    list_per_page = 10
    
admin.site.register(Emprestimo,AdminEmprestimo)

class AdminEmprestimoLivros(admin.ModelAdmin):
    list_display = ['id', 'livroFK', 'quantidade', 'emprestimoFK',]
    list_display_links = ('id', 'livroFK', 'quantidade', 'emprestimoFK',)
    search_fields = ('livroFK',)
    list_per_page = 10
    
admin.site.register(EmprestimoLivros,AdminEmprestimoLivros)

class AdminFoto(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10
    
admin.site.register(Foto,AdminFoto)