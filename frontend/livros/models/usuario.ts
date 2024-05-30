export type Usuario = {
    id: number
    email: string;
    nome: string;
    telefone: string;
    cpf: string;
    endereco: string;
    is_active: boolean;
    groups: Array<string>;
    user_permissions: Array<string>;
    password: string;
}