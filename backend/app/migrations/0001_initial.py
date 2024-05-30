# Generated by Django 5.0.5 on 2024-05-21 22:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaLivros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCustomizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='endereço de email')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=20)),
                ('biografia', models.CharField(blank=True, max_length=5000, null=True)),
                ('foto', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraEmprestimo', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'PENDENTE'), ('A', 'APROVADO'), ('R', 'RECUSADO'), ('C', 'CANCELADO')], max_length=20)),
                ('dataPrevista', models.DateTimeField(auto_now_add=True)),
                ('dataDevolucao', models.DateTimeField(auto_now_add=True, null=True)),
                ('usuarioFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioVendas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=3500)),
                ('precoEmprestimo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade', models.IntegerField()),
                ('stars', models.IntegerField()),
                ('numeroPaginas', models.IntegerField()),
                ('formato', models.CharField(choices=[('E', 'Ebook'), ('F', 'Fisíco')], max_length=20)),
                ('numeroEdição', models.IntegerField()),
                ('anoPublicação', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to=settings.AUTH_USER_MODEL)),
                ('categoriaFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriaLivros', to='app.categorialivros')),
                ('fotos', models.ManyToManyField(to='app.foto')),
            ],
        ),
        migrations.CreateModel(
            name='EmprestimoLivros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('emprestimoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimoFK', to='app.emprestimo')),
                ('livroFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimoLivros', to='app.livros')),
            ],
        ),
    ]
