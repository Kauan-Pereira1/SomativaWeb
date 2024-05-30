from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

class Foto(models.Model):
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.url

class UsuarioCustomizado(AbstractBaseUser,PermissionsMixin):
     nome = models.CharField(max_length=150)
     email = models.EmailField("endereço de email", unique=True)
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
     telefone = models.CharField(max_length=15, null=True, blank=True)
     endereco = models.CharField(max_length=200)
     cpf = models.CharField(max_length=20)


     
     objects = Gerenciador()

     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = []

     def __str__(self):
          return self.email


class CategoriaLivros(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

FORMATO = [
     ("Ebook", "Ebook"),
     ("Fisico", "Fisico")
]

class Autor(models.Model):
     nome = models.ForeignKey(UsuarioCustomizado, related_name='autor', on_delete=models.CASCADE)
     biografia = models.CharField(max_length=5000, null=True, blank=True)
     foto = models.TextField(null=True, blank=True)

     def __str__(self):
        return self.nome

class Livros(models.Model):
    categoriaFK = models.ForeignKey(CategoriaLivros, related_name='categoriaLivros', on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    description = models.CharField(max_length=3500, null=False)
    precoEmprestimo = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    fotos = models.ManyToManyField(Foto)
    stars = models.IntegerField()
    autorFK = models.ForeignKey(Autor, related_name='autorLivro', on_delete=models.CASCADE) 
    numeroPaginas = models.IntegerField()
    formato = models.CharField(max_length=20, choices=FORMATO)
    numeroEdicao = models.IntegerField()
    anoPublicacao = models.IntegerField()

    def __str__(self):
        return self.nome

STATUS_EMPRESTIMO = [
    ("P","PENDENTE"),
    ("A","APROVADO"),
    ("R","RECUSADO"),
    ("C","CANCELADO"),
]


class Emprestimo(models.Model):
    usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='usuarioVendas', on_delete=models.CASCADE)
    dataHoraEmprestimo = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_EMPRESTIMO)
    dataPrevista = models.DateTimeField(auto_now_add=True) # Somar +14 dias a essa data, para deixar como previsão
    dataDevolucao = models.DateTimeField(auto_now_add=True, null=True) #Se tiver nula, significa que o leitor ainda não devolveu o livro.
    def __str__(self):
            return self.status

class EmprestimoLivros(models.Model):
     livroFK = models.ForeignKey(Livros, related_name='emprestimoLivros', on_delete=models.CASCADE)
     quantidade = models.IntegerField()
     emprestimoFK = models.ForeignKey(Emprestimo, related_name='emprestimoFK', on_delete=models.CASCADE)

     def __str__(self):
            return self.produtoFK.nome