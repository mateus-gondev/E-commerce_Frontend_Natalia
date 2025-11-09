<template>
    <div class="adm-layout">
        <AdmNavbar />
        <main class="adm-content">
        <div class="header">
            <h1>Lista Usuários</h1>
            <button class="btn-add" @click="irParaFormulario()">+ Novo Usuário</button>
        </div>

        <div class="buscar">
            <img src="@/assets/icons/iconLupa.png" alt="Buscar" />
            <input type="text" placeholder="Encontre sua joia..." />
        </div>

        <table class="tabela-usuarios">
            <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Cargo</th>
                <th>Ações</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="user in usuarios" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.name }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.cargo }}</td>
                <td>
                <button class="btn-edit" @click="abrirModal(user)">Editar</button>
                <button class="btn-delete" @click="abrirModalExcluir(user)">Excluir</button>
                </td>
            </tr>
            </tbody>
        </table>

        <!-- Modal de Edição / Cadastro -->
        <div v-if="modalAberto" class="modal">
            <div class="modal-content">
            <h3>{{ modoEdicao ? "Editar Usuário" : "Novo Usuário" }}</h3>

            <label>Nome:</label>
            <input v-model="usuarioAtual.name" type="text" placeholder="Nome" />

            <label>Email:</label>
            <input v-model="usuarioAtual.email" type="email" placeholder="E-mail" />

            <label>Cargo:</label>
            <select v-model="usuarioAtual.cargo">
                <option disabled value="">Selecione um cargo</option>
                <option value="Administrador">Administrador</option>
                <option value="Funcionario">Funcionário</option>
                <option value="Cliente">Cliente</option>
            </select>

            <label>Senha (opcional para editar):</label>
            <input v-model="usuarioAtual.password" type="password" placeholder="Senha" />

            <div class="modal-actions">
                <button @click="salvarUsuario(usuarioAtual)">Salvar</button>
                <button @click="fecharModal()">Cancelar</button>
            </div>
            </div>
        </div>

        <!-- Modal de Exclusão -->
        <div v-if="modalExcluirAberto" class="modal">
            <div class="modal-content">
            <h3>Deseja realmente excluir {{ usuarioAtual.name }}?</h3>
            <div class="modal-actions">
                <button @click="excluirUsuario()">Sim</button>
                <button @click="fecharModalExcluir()">Cancelar</button>
            </div>
            </div>
        </div>
        </main>
    </div>
</template>

<script>
import api from "@/services/api";
import AdmNavbar from "../../components/Adm/AdmNavbar.vue";
import AdmForm from "../AdmPage/AdmForm.vue";

export default {
    name: "AdmUsuario",
    components: { AdmNavbar, AdmForm },
    data() {
        return {
        usuarios: [],
        usuarioAtual: { id: null, name: "", email: "", password: "", cargo: "" },
        modalAberto: false,
        modalExcluirAberto: false,
        modoEdicao: false,
        };
    },

    mounted() {
        this.carregarUsuarios();
    },

    methods: {
        async carregarUsuarios() {
        try {
            const res = await api.get("/users");
            this.usuarios = res.data;
        } catch (error) {
            console.error("Erro ao carregar usuários:", error);
        }
        },

        irParaFormulario() {
        this.$router.push("/adm/usuario/novo");
        },

    abrirModal(usuario) {
        this.usuarioAtual = { ...usuario };
        this.modoEdicao = true;
        this.modalAberto = true;
    },

    fecharModal() {
      this.modalAberto = false;
      this.modoEdicao = false;
      this.usuarioAtual = { id: null, name: "", email: "", password: "", cargo: "" };
    },

    async salvarUsuario(dados) {
        try {
            if (this.modoEdicao) {
                await api.put(`/users/${this.usuarioAtual.id}`, {
                    name: this.usuarioAtual.name,
                    email: this.usuarioAtual.email,
                    password: this.usuarioAtual.password || undefined,
                    cargo: this.usuarioAtual.cargo,
                });
                alert("Usuário atualizado com sucesso!");
            } else {
                await api.post("/users", dados);
                alert("Usuário cadastrado com sucesso!");
            }

            this.fecharModal();
            this.carregarUsuarios();
        } catch (error) {
            console.error(error);
            alert(error.response?.data?.error || "Erro ao salvar usuário.");
        }
        },

    abrirModalExcluir(usuario) {
        this.usuarioAtual = { ...usuario };
        this.modalExcluirAberto = true;
    },

    fecharModalExcluir() {
        
    },

    async excluirUsuario() {
        try {
            await api.delete(`/users/${this.usuarioAtual.id}`);
            alert("Usuário excluído com sucesso!");
            this.fecharModalExcluir();
            this.carregarUsuarios();
        } catch (error) {
            console.error("Erro ao excluir usuário:", error);
        }
        },
    },
};
</script>


<style scoped>
.adm-layout {
    display: flex;
    background-color: #f9f9fb;
    font-family: 'Poppins', sans-serif;
    overflow: visible !important;
}


.buscar {
    display: flex;
    align-items: center;
    background-color: var(--banco-cinza);
    border-radius: 20px;
    padding: 6px 12px;
    width: 240px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.buscar{
    background-color: #d9d9d9;
    margin-bottom: 20px;
}
.buscar:hover{
    background-color: #dcd7d780;

}

.buscar img {
    width: 18px;
    margin-right: 8px;
    opacity: 0.8;
}

.buscar input {
    background: none;
    border: none;
    outline: none;
    color: var(--preto);
    width: 100%;
    font-size: 14px;
}

/* Conteúdo principal */
.adm-content {
    margin-left: 250px;
    padding: 2rem;
    width: 100%;
    min-height: 100vh;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #fff;
    padding: 1rem 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
}

.header h1 {
    font-size: 1.4rem;
    color: #333;
    margin-top: 15px;
}

.btn-add {
    background-color: #d4af37;
    color: #fff;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-add:hover {
    background-color: #b8962d;
    transform: translateY(-2px);
}

/* Tabela dos usuários */
.tabela-usuarios {
    width: 100%;
    border-collapse: collapse;
    border-radius: 12px;
    overflow: hidden;
    background: #fff;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

.tabela-usuarios th,
.tabela-usuarios td {
    padding: 14px 18px;
    text-align: left;
    border-bottom: 1px solid #eee;
}

.tabela-usuarios th {
    background-color: #222;
    color: #fff;
    font-weight: 600;
}

.tabela-usuarios tr:hover td {
    background-color: #f6f6f6;
}

/* Botões da tabela */
.btn-edit,
.btn-delete {
    border: none;
    padding: 6px 10px;
    border-radius: 6px;
    cursor: pointer;
    color: #fff;
    font-size: 0.9rem;
    transition: 0.3s ease;
    margin-left: 20px;
}

.btn-edit {
    background-color: #4a90e2;
}

.btn-edit:hover {
    background-color: #3a78c0;
}

.btn-delete {
    background-color: #e74c3c;
}

.btn-delete:hover {
    background-color: #c0392b;
}


.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(15, 15, 15, 0.45);
    backdrop-filter: blur(4px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
    animation: fadeIn 0.3s ease;
}

.modal-content {
    background: #ffffff;
    padding: 2rem;
    border-radius: 14px;
    width: 420px;
    max-width: 90%;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    animation: slideUp 0.35s ease;
    font-family: 'Poppins', sans-serif;
}

.modal-content h3 {
    margin-bottom: 1.2rem;
    text-align: center;
    color: #333;
    font-size: 1.4rem;
    font-weight: 600;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 0.8rem;
}

select {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 14px;
    background-color: #fff;
}


.modal-content label {
    display: block;
    margin-bottom: 0.3rem;
    font-weight: 500;
    color: #555;
}

.modal-content input {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #ccc;
    border-radius: 8px;
    outline: none;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    margin-bottom: 1rem;
}

.modal-content input:focus {
    border-color: #d4af37;
    box-shadow: 0 0 4px rgba(212, 175, 55, 0.3);
}

.modal-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 1rem;
}

.modal-actions button {
    padding: 10px 18px;
    border-radius: 8px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    font-size: 0.95rem;
    transition: all 0.25s ease;
}

.modal-actions button:first-child {
    background: #2c3e50;
    color: #fff;
}

.modal-actions button:first-child:hover {
    background: #b8942f;
    transform: translateY(-2px);
}

.modal-actions button:last-child {
    background: #777;
    color: #fff;
}

.modal-actions button:last-child:hover {
    background: #555;
    transform: translateY(-2px);
}

/* Animações */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideUp {
    from {
        transform: translateY(30px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}


</style>
