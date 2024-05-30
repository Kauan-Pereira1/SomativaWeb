export type CategoriaLivro = {
    id: number;
    nome: string;
}

export type Autor = {
    id: number;
    nome: string;
    biografia: string;
    foto: string;
}

export type Livro = {
    id: number;
    nome: string;
    description: string;
    precoEmprestimo: number;
    quantidade: number;
    stars: number;
    numeroPaginas: number;
    formato: string;
    numeroEdicao: number;
    anoPublicacao: number;
    categoriaFK: CategoriaLivro;
    autorFK: Autor;
    fotos: Array<string>;
}