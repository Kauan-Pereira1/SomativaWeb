<!-- <script setup lang="ts">
import { ref } from "vue";
import type { Usuario } from "~/models/usuario";
import { cadastrarUsuario } from "~/services/usuario";

const novoUsuario = ref<Usuario>({
    id: 0,
    email: "",
    nome: "",
    telefone: "",
    cpf: "",
    endereco: "",
    is_active: true,
    groups: [],
    user_permissions: [],
    password: "" // Adicionado campo de senha
});

const cadastroStatus = ref<string>(""); // Para controlar o feedback de sucesso/erro após o cadastro

const submitCadastro = async () => {
    try {
        const usuarioCadastrado = await cadastrarUsuario(novoUsuario.value);
        if (usuarioCadastrado) {
            cadastroStatus.value = "success"; // Exibir mensagem de sucesso
            // Limpar campos do formulário após o cadastro bem-sucedido
            novoUsuario.value = {
                id: 0,
                email: "",
                nome: "",
                telefone: "",
                cpf: "",
                endereco: "",
                is_active: true,
                groups: [],
                user_permissions: [],
                password: "" // Resetar o campo de senha
            };
        } else {
            cadastroStatus.value = "error"; // Exibir mensagem de erro
        }
    } catch (error) {
        console.error("Erro ao cadastrar usuário:", error);
        cadastroStatus.value = "error"; // Exibir mensagem de erro
    }
};
</script>

<template>
    <main class="cadastro-main flex align-items-center justify-content-center">
        <section class="cadastro-container flex flex-column align-items-center justify-content-center">
            <h4 class="row-cadastro">Cadastro de Usuário</h4>
            <form @submit.prevent="submitCadastro">
                <div class="row-cadastro">
                    <FloatLabel>
                        <InputText v-model="novoUsuario.nome" type="text" id="nome-input" required class="input-text" />
                        <label for="nome-input">Nome</label>
                    </FloatLabel>
                </div>
                <div class="row-cadastro">
                    <FloatLabel>
                        <InputText v-model="novoUsuario.email" type="email" id="email-input" required
                            class="input-text" />
                        <label for="email-input">E-mail</label>
                    </FloatLabel>
                </div>
                <div class="row-cadastro">
                    <FloatLabel>
                        <InputText v-model="novoUsuario.telefone" type="text" id="telefone-input" required
                            class="input-text" />
                        <label for="telefone-input">Telefone</label>
                    </FloatLabel>
                </div>
                <div class="row-cadastro">
                    <FloatLabel>
                        <InputText v-model="novoUsuario.cpf" type="text" id="cpf-input" required class="input-text" />
                        <label for="cpf-input">CPF</label>
                    </FloatLabel>
                </div>
                <div class="row-cadastro">
                    <FloatLabel>
                        <InputText v-model="novoUsuario.endereco" type="text" id="endereco-input" required
                            class="input-text" />
                        <label for="endereco-input">Endereço</label>
                    </FloatLabel>
                </div>
                <div class="row-cadastro">
                    <FloatLabel>
                        <InputText v-model="novoUsuario.password" type="password" id="password-input" required
                            class="input-text" />
                        <label for="password-input">Senha</label>
                    </FloatLabel>
                </div>
                <div class="row-cadastro">
                    <Button type="submit" label="Cadastrar" class="btn-cadastrar"></Button>
                </div>
                <p v-if="cadastroStatus === 'success'" class="success-message">Usuário cadastrado com sucesso!</p>
                <p v-if="cadastroStatus === 'error'" class="error-message">Erro ao cadastrar usuário. Por favor, tente
                    novamente.</p>
            </form>
        </section>
    </main>
</template>

<style scoped lang="scss">
.cadastro-main {
    width: 100vw;
    height: 100vh;
    background-image: url('biblioteca.jpg');
    background-repeat: repeat;
    background-size: cover;

    .cadastro-container {
        width: 30vw;
        height: auto;
        background-color: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .row-cadastro {
        margin: 1rem 0;

        .input-text {
            height: 2.5rem;
            width: 100%;
        }

        .btn-cadastrar {
            width: 100%;
            height: 2.5rem;
        }
    }

    .success-message,
    .error-message {
        margin-top: 1rem;
        text-align: center;
        font-size: 1rem;
    }

    .success-message {
        color: green;
    }

    .error-message {
        color: red;
    }
}
</style> -->

<script></script>
<template>
    <H1>CADASTRO</H1>
</template>
<style></style>