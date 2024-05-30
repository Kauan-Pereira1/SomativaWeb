<script setup lang="ts">
import { computed } from "#imports";
import { type Livro } from "~/models/livros";
import { carrinho } from "#imports";
const { adicionarNoCarrinho, getCarrinho, estaNoCarrinho } = carrinho();

type propType = {
  livro: Livro;
};

const props = defineProps<propType>();


const emit = defineEmits(['eventoAdicionado']);

const adicionarItem = (e: any) => {
  e.stopPropagation()
  adicionarNoCarrinho(props.livro);
  emit('eventoAdicionado');
  console.log("CARRINHO ATUAL: ", getCarrinho());
}

const navegarDetalhesLivro = () => {
  navigateTo(`/livros/${props.livro.id}`);
}


const produtoNoCarrinho = computed(() => {
  return estaNoCarrinho(props.livro);
});

console.log(props.livro.precoEmprestimo)


</script>

<template>
  <section class="cartao flex flex-column align-items-center justify-content-center" v-if="props.livro"
    @click="navegarDetalhesLivro">
    <div class="check text-right">
      <Checkbox v-model="produtoNoCarrinho" :binary="true" :readonly="true" />
    </div>
    <div class="livro-imagem">
      <img :src="props.livro.fotos[0]">
    </div>
    <div>
      <h4 class="livro-nome">{{ props.livro.nome }}</h4>
    </div>
    <div class="flex flex-row">
      <span>{{ formatCurrency(props.livro.precoEmprestimo) }}</span>
    </div>
    <div class="ml-2">
      <label>Qtd.Dísponivel:</label>
      <span>{{ props.livro.quantidade }}</span>
    </div>
    <div class="ml-2">
      <label>Qtd.Estrelas:</label>
      <i v-for=" n  in  props.livro.stars " :key="n" class="pi pi-star"></i>
    </div>
    <div>
      <Button @click="adicionarItem" class="botao-add" label="Adicionar" />
    </div>
  </section>
</template>

<style scoped lang="scss">
.cartao {
  width: 300px;
  max-width: 300px;
  height: 350px;
  max-height: 350px;
  background-color: white;
  border-radius: 1.5rem;
  margin: 1.5rem;
  cursor: pointer;

  &:hover {
    transform: scale(1.1);
    transition: 2s;
  }

  .livro-imagem {
    width: 90%;
    height: 55%;
    max-width: 200px;
    max-height: 230px;

    img {
      width: 100%;
      height: 100%;
    }
  }

  .livro-nome {
    margin: 0.5rem;
  }

  .botao-add {
    width: 80%;
    height: 2rem;
    margin: 1rem;
  }

  .check {
    width: 95%;

  }

  .pi {
    color: #ffc107;
  }
}
</style>