import { BACKEND_URL } from "~/models/app";
import type { Emprestimo, EmprestimoLivros, EmprestimoLivrosBody } from "~/models/emprestimo";

export const salvarEmprestimo = (emprestimo: Emprestimo): Promise<Emprestimo | null> => {
    return useFetch<Emprestimo>(`${BACKEND_URL}/emprestimo/`, {
        method: 'POST',
        body: emprestimo
    })
        .then(resposta => {
            return Promise.resolve(resposta.data.value);
        })
        .catch(error => {
            console.log("error", error);
            return Promise.resolve(null);
        })
};


export const salvarEmprestimoLivros = (emprestimos: Array<EmprestimoLivrosBody>): Promise<EmprestimoLivros | null> => {
    return useFetch<EmprestimoLivros>(`${BACKEND_URL}/emprestimo-livros/`, {
        method: 'POST',
        body: emprestimos
    })
        .then(resposta => {
            return Promise.resolve(resposta.data.value);
        })
        .catch(error => {
            console.log("error", error);
            return Promise.resolve(null);
        })
};