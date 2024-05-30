<script setup lang="ts">
import { reactive, ref } from 'vue';
const { signIn } = useAuth();

definePageMeta({
  layout: 'login'
})


const credenciais = reactive({
  email: '',
  password: ''
});
const mensagemErro = ref('');

const SubmitLogin = () => {
  console.log("login: ", credenciais);
  signIn(credenciais, { redirect: false })
    .then(() => {
      console.log("logado com sucesso....");
      navigateTo('/');
    })
    .catch((error) => {
      console.error("error: ", error);
      mensagemErro.value = 'Não foi possível fazer o login com estas credenciais...';
      setTimeout(() => {
        mensagemErro.value = '';
        credenciais.email = '';
        credenciais.password = '';
      }, 3000);
    })
}

const painel = ref();

const toggle = (event: any) => {
  painel.value.toggle(event);
}


</script>

<template>
  <main class="login-main flex align-items-center justify-content-center">
    <section class="login-container flex flex-column align-items-center justify-content-center">
      <h4 class="row-login">Livraria do Estoque</h4>
      <div class="row-login">
        <FloatLabel>
          <InputText v-model="credenciais.email" type="email" id="email-input" class="input-text" />
          <label for="email-input">Email</label>
        </FloatLabel>
      </div>
      <div class="row-login">
        <FloatLabel>
          <InputText v-model="credenciais.password" type="password" id="password-input" class="input-text" />
          <label for="password-input">Password</label>
        </FloatLabel>
      </div>
      <div class="row-login" v-if="mensagemErro !== ''">
        <p id="erro">{{ mensagemErro }}</p>
      </div>
      <div class="row-login">
        <Button @click="SubmitLogin" label="Entrar" id="login-button"></Button>
      </div>
    </section>
  </main>
</template>

<style scoped lang="scss">
.login-main {
  width: 100vw;
  height: 100vh;
  background-image: url('biblioteca.jpg');
  background-repeat: repeat;
  background-size: cover;

  .login-container {
    width: 30vw;
    height: 70vh;
    background-color: white;

  }

  .row-login {
    margin: 1rem 0 1rem 0;

    .input-text {
      height: 2.5rem;
      width: 250px;
    }

    #login-button {
      width: 250px;
      height: 30px;
    }

    #erro {
      color: tomato;
      font-size: 0.9rem;
    }
  }
}
</style>