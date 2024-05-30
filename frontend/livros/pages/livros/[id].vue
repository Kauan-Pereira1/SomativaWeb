<script setup lang="ts">
import { BACKEND_URL } from "~/models/app";
import { type Livro } from "~/models/livros";

const route = useRoute();
console.log(route.params.id);

const { data: livro, error } = await useFetch<Livro>(`${BACKEND_URL}/livros/${route.params.id}`);

if (error.value) {
    console.error("Error fetching livro data:", error.value);
} else {
    console.log("Livro data:", livro.value);
    console.log("Autor foto:", livro.value?.autorFK.foto);
}
</script>

<template>
    <div class="livro-detalhes">
        <div class="livro-imagem">
            <!-- Exibir a primeira foto do livro -->
            <img :src="livro?.fotos[0]" alt="Imagem do Livro" />
        </div>
        <div class="livro-info">
            <h2>{{ livro?.nome }}</h2>
            <div class="info-autor">
                <span>Autor:</span>
                <p>{{ livro?.autorFK.nome }}</p>
                <div class="autor-biografia">
                    <span>Biografia do Autor:</span>
                    <p>{{ livro?.autorFK.biografia }}</p>
                </div>
                <div class="autor-foto">
                    <span>Foto do Autor:</span>
                    <img v-if="livro?.autorFK.foto" :src="livro?.autorFK.foto" alt="Foto do Autor"
                        class="autor-foto-img" />
                    <p v-else>Nenhuma foto disponível</p>
                </div>
            </div>
            <div class="info-categoria">
                <span>Categoria:</span>
                <p>{{ livro?.categoriaFK.nome }}</p>
            </div>
            <div class="info-descricao">
                <span>Descrição:</span>
                <p>{{ livro?.description }}</p>
            </div>
            <div class="info-preco">
                <span>Preço:</span>
                <p>{{ livro?.precoEmprestimo }} BRL</p>
            </div>
            <div class="info-outros">
                <span>Outros detalhes:</span>
                <p>Páginas: {{ livro?.numeroPaginas }}</p>
                <p>Formato: {{ livro?.formato }}</p>
                <p>Número de Edição: {{ livro?.numeroEdicao }}</p>
                <p>Ano de Publicação: {{ livro?.anoPublicacao }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
.livro-detalhes {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 20px;
    margin-top: 20px;
}

.livro-imagem img {
    max-width: 300px;
    height: auto;
    border-radius: 5px;
}

.livro-info {
    max-width: 600px;
}

.info-autor,
.info-categoria,
.info-descricao,
.info-preco,
.info-outros {
    margin-bottom: 15px;
}

.info-autor span,
.info-categoria span,
.info-descricao span,
.info-preco span,
.info-outros span {
    font-weight: bold;
}

.info-autor p,
.info-categoria p,
.info-descricao p,
.info-preco p,
.info-outros p {
    margin: 5px 0;
}

.autor-biografia {
    margin-top: 10px;
}

.autor-foto {
    margin-top: 10px;
}

.autor-foto-img {
    max-width: 350px;
    /* Aumenta o tamanho máximo da largura */
    height: auto;
    /* Mantém a proporção da altura */
    border-radius: 5px;
    margin-right: 10px;
}
</style>
