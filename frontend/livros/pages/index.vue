<script setup lang="ts">
import { getLivros } from "~/services/livros";
import { type Livro } from "~/models/livros";
import { type Ref, ref } from "vue";
import { useToast } from "primevue/usetoast";
const toast = useToast();

const show = () => {
    toast.add({ severity: 'success', summary: '  Livro Adicionado', detail: 'Acesse-o em seu carrinho', life: 30000 });
};

const livros: Ref<Array<Livro>> = ref([]);

definePageMeta({
    middleware: 'auth'
})

const atualizarLivros = () => {
    getLivros().then((livrosEncontrados) => {
        console.log("livros encontrados: ", livrosEncontrados?.results[0].nome);
        livros.value = livrosEncontrados?.results ?? [];
    });
};

atualizarLivros();

</script>

<template>
    <main class="home-container flex flex-column align-items-center">
        <h2 class="mt-4 mb-4">🥃 Nossos Livros</h2>
        <Toast />
        <div class="livros-container grid align-items-center justify-content-center">
            <div v-for="(livro, index) in livros">
                <LivroItem :key="index" class="col-4" :livro="livro" @eventoAdicionado="show" />
            </div>
        </div>
    </main>
</template>

<style scoped lang="scss">
.home-container {
    margin: 0;
    width: 100vw;
    min-height: calc(100vh - 80px);
    background-image: url("biblioteca.jpg");
    background-repeat: repeat;
    background-size: cover;


}

.p-toast-summary {
    padding: 1.5rem !important;
}
</style>