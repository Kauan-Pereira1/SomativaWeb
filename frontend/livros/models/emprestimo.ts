import type { Livro } from "./livros";
import type { Usuario } from "./usuario";

export enum PAGAMENTOS {
    'PENDENTE' = "PENDENTE",
    'APROVADO' = "APROVADO",
    'CANCELADO' = "CANCELADO",
    'RECUSADO' = "RECUSADO",
}

export type Emprestimo = {
    id?: number,
    usuarioFK: string;
    dataHora?: string;
    status: PAGAMENTOS;
    dataPrevista: string;
    dataDevolucao: string;
}

export type EmprestimoLivros = {
    livroFK: Livro;
    quantidade: number;
    emprestimoFK: Emprestimo;
}

export type EmprestimoLivrosBody = {
    livroFK: number;
    quantidade: number;
    emprestimoFK: number;
}
