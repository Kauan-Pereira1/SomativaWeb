import { BACKEND_URL } from "~/models/app";
import type { Usuario } from "~/models/usuario";

export const cadastrarUsuario = (novoUsuario: Usuario): Promise<Usuario | null> => {
    return fetch(`${BACKEND_URL}/usuarios/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(novoUsuario),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao cadastrar usuário');
            }
            return response.json();
        })
        .then(data => {
            return data; // O novo usuário cadastrado
        })
        .catch(error => {
            console.error('Erro ao cadastrar usuário:', error);
            return null;
        });
};
