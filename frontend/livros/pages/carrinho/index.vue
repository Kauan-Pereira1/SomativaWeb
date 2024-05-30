<script setup lang="ts">
import { computed } from "#imports";
import { carrinho, type CarrinhoItem } from "#imports";
const { getCarrinho, removerDoCarinho, getValorTotalDoCarrinho, esvaziarCarrinho } = carrinho();
import { salvarEmprestimo, salvarEmprestimoLivros } from "~/services/emprestimos";
const { data } = useAuth();
import { PAGAMENTOS, type EmprestimoLivrosBody } from "~/models/emprestimo";
import { type Usuario } from "~/models/usuario";

definePageMeta({
  middleware: "auth",
});


const usuarioLogado = computed<Usuario | null>(() => {
  if (data.value) {
    // return data.value?.results[0] ? data.value?.results[0] as Usuario : null;
    console.log(data.value)
  }
  return null;
});

//pegando os itens que estão no carrinho e salvando
//na variavel
const itensNoCarrinho = computed<Array<CarrinhoItem>>(() => getCarrinho());
const valorTotal = computed(() => getValorTotalDoCarrinho().toPrecision(5));

const carregando = ref(false);
const salvo = ref(false);

console.log("itens No carrinho.....", itensNoCarrinho);

const deletarDoCarrinho = (itemParaRemover: CarrinhoItem) => {
  removerDoCarinho({
    livro: itemParaRemover.livro,
    quantidade: 0
  });
}

// Defina as datas previstas e de devolução
const dataPrevista = new Date().toISOString(); // ou qualquer outra lógica para definir a data prevista
const dataDevolucao = new Date().toISOString(); // ou qualquer outra lógica para definir a data de devolução


const salvarPedido = () => {
  if (getCarrinho().length) {
    carregando.value = true;
    console.log("data", data.value)
    salvarEmprestimo({
      status: PAGAMENTOS.PENDENTE,
      usuarioFK: usuarioLogado.value ? `${usuarioLogado.value.id}` : '',
      dataPrevista, // ou qualquer outra lógica para definir a data prevista
      dataDevolucao
    }).then(emprestimoSalvo => {
      console.log("emprestimo salvo: ", emprestimoSalvo);
      let payload: Array<EmprestimoLivrosBody> = [];
      getCarrinho().forEach(item => {
        payload.push({
          emprestimoFK: emprestimoSalvo?.id ?? 0,
          livroFK: item.livro.id ?? 0,
          quantidade: item.quantidade,
        })
      });

      salvarEmprestimoLivros(payload).then(resposta => {
        console.log("ITENS DE VENDA SALVOS!", resposta);
        setTimeout(() => {
          salvo.value = true;

          esvaziarCarrinho();
        }, 3000);
      }).catch(error => {
        console.error("Erro ao salvar emprestimo! ", error);
      });

    }).catch(error => {
      console.error("Erro ao salvar emprestimo! ", error);
    })
      .finally(() => {
        setTimeout(() => {
          carregando.value = false;
        }, 3000);
      });
  }

}

</script>

<template>
  <main class="carrinho-container flex flex-column align-items-center">
    <h2 class="mt-4 mb-4">🛒 Seu carrinho de compras</h2>
    <div class="card flex justify-content-center" v-if="carregando">
      <ProgressSpinner />
    </div>
    <table v-if="!carregando">
      <thead>
        <tr class="text-center">
          <td>Item</td>
          <td>Livro</td>
          <td>Descrição</td>
          <td>Categoria</td>
          <td>Preço Unitário</td>
          <td>Quantidade</td>
          <td>Subtotal</td>
          <td>Ações</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(itemCarrinho, index) in itensNoCarrinho" :key="index" class="text-center">
          <td>{{ index + 1 }}</td>
          <td><img class="fotoLivro" :src="itemCarrinho.livro.fotos[0]" alt="foto livro" /></td>
          <td>{{ itemCarrinho.livro.nome }}</td>
          <td>{{ itemCarrinho.livro.categoriaFK.nome }}</td>
          <td>R$ {{ itemCarrinho.livro.precoEmprestimo }}</td>
          <td>{{ itemCarrinho.quantidade }}</td>
          <td>R$ {{ itemCarrinho.quantidade * itemCarrinho.livro.precoEmprestimo }}</td>
          <td>
            <Button @click="deletarDoCarrinho(itemCarrinho)" label=""><i class="pi pi-trash"></i></Button>
          </td>
        </tr>
      </tbody>
      <tfoot>
        <tr class="text-center">
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th>Valor Total:</th>
          <th>R${{ valorTotal }}</th>
        </tr>
      </tfoot>
    </table>
    <Button :disabled="salvo" v-if="!carregando" @click="salvarPedido" class="mt-2 botao-pedido bg-primary"
      label="Fechar pedido" />
    <Message v-if="salvo" severity="success">
      <p>Pedido realizado com sucesso!</p>
      <p>Consulte seus itens em <NuxtLink to="/pedidos">Meus Pedidos</NuxtLink>
      </p>
    </Message>

  </main>
</template>

<style scoped lang="scss">
$largura-tabela: 90vw;

.carrinho-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: red;
  background-image: url("biblioteca.jpg");
  background-repeat: repeat;
  background-size: cover;
}

table {
  width: $largura-tabela;
  background-color: white;
  border-radius: 1rem;
}

thead {
  font-weight: bold;

  tr {
    border-bottom: 2px solid black
  }
}

td {
  padding: 1rem;
}

.fotoLivro {
  width: 50px;
  height: 50px;
}

Button {
  background-color: white;
  color: rgb(114, 15, 15);
  border: none;
}

.valor-total {
  font-weight: bold;
  width: 900px
}

.botao-pedido {
  width: $largura-tabela;
  height: 30px;

  &:hover {
    transform: scale(1.05);
    transition: 2s;
  }
}
</style>