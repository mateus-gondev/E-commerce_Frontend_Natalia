<template>
    <div class="adm-layout">
        <AdmNavbar />

        <main class="adm-content">
            <div class="header">
                <h1>Lista Produtos</h1>
                <button class="btn-add" @click="irParaFormulario()">+ Novo Produto</button>
            </div>

            <div class="buscar">
                <img src="@/assets/icons/iconLupa.png" alt="Buscar" />
                <input
                type="text"
                v-model="termoBusca"
                placeholder="Encontre Usuário..."
                />
            </div>

            <div class="lista-produtos" v-if="produtosFiltrados.length > 0" >
                <table class="tabela-produtos">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Descrição</th>                            
                            <th>Preço</th>
                            <th>Imagem URL</th>
                            <th>Ações</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="produto in produtos" :key="produto.id_produto">
                            <td>{{ produto.id_produto }}</td>
                            <td>{{ produto.name }}</td>
                            <td>{{ produto.description }}</td>
                            <td>{{ formatarPreco(produto.price) }}</td>
                            <td>
                                <a :href="produto.image" target="_blank">Ver imagem</a>
                            </td>

                            <td>
                                <button class="btn-edit" @click="abrirModal(produto)">Editar</button>
                                <button class="btn-delete" @click="abrirModalExcluir(produto)">Excluir</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="mensagem-vazia" v-else>
                <p> Nenhum produto encontrado no momento.</p>
            </div>

            <!--Modal Edição e Cadastro-->
            <div v-if="modalAberto" class="modal">
                <div class="modal-content">
                    <h3>{{ modoEdicao ? 'Editar Produto' : 'Novo Produto' }}</h3>
                    
                    <label>Nome:</label>
                    <input v-model="produtoAtual.name" type="text" placeholder="Nome">

                    <label>Descrição:</label>
                    <input v-model="produtoAtual.description" type="text" placeholder="Descrição">

                    <label>Preço:</label>
                    <input v-model="produtoAtual.price" type="number" placeholder="Preço">

                    <label>Imagem URL:</label>
                    <input v-model="produtoAtual.image" type="text" placeholder="Imagem URL">

                    <div class="modal-actions">
                        <button @click="salvarProduto(produtoAtual)">Salvar</button>
                        <button @click="fecharModal()">Cancelar</button>
                    </div>
                </div>
            </div>

            <!-- Modal Exclusao-->
            <div v-if="modalExcluirAberto" class="modal">
                <div class="modal-content">
                    <h3>Deseja realmente excluir {{ produtoAtual.name }}?</h3>
                    <div class="modal-actions">
                        <button @click="excluirProduto()">Sim</button>
                        <button @click="fecharModalExcluir()">Cancelar</button>
                    </div>
                </div>  
            </div>  

        </main>

    </div>
</template>

<script>
import api from "@/services/api";
import AdmNavbar from "@/components/Adm/AdmNavbar.vue";

export default {
    name: "AdmProdutos",
    components: {AdmNavbar},
    data(){
        return {
            produtos: [],
            produtoAtual: { id_produto: null, name: "", description: "", price: "", image: ""},
            modalAberto: false,
            modalExcluirAberto: false,
            modoEdicao: false,
        };        
    },
    computed: {
        produtosFiltrados(){
            if (!this.termoBusca) return this.produtos;
            const termo = this.termoBusca.toLowerCase();
            return this.produtos.filter(
                (u) =>
                u.name.toLowerCase().includes(termo) ||
                u.description.toLowerCase().includes(termo) ||
                u.price.toLowerCase().includes(termo)
            );
        },
    },

    mounted(){
        this.carregarProdutos();
    },

    methods: {
        async carregarProdutos(){
        try {
            const res = await api.get("/product");
            this.produtos = res.data;        
        } catch (error) {
            console.error("Erro ao carregar produtos:", error);
        }
        },

        irParaFormulario() {
            this.$router.push("/adm/produto/novo");
        },

        abrirModal(produto){
            this.produtoAtual = {...produto};
            this.modoEdicao = true;
            this.modalAberto = true;
        },

        fecharModal(){
            this.modalAberto = false;
            this.modoEdicao = false;
            this.produtoAtual = {id_produto: null, name: "", description: "", price: "", image: ""}
        },

        async salvarProduto(dados){
            try{
                if (this.modoEdicao){
                    await api.put(`/product/${this.produtoAtual.id_produto}`,{
                        name: this.produtoAtual.name,
                        description: this.produtoAtual.description,
                        price: this.produtoAtual.price,
                        image: this.produtoAtual.image,
                    });
                    alert("Produto atualizado com sucesso!");                
                } else{
                    await api.post("/product/", dados);
                    alert("Produto cadastrado com sucesso!")
                }

                this.fecharModal();
                this.carregarProdutos();
            } catch (error){
                console.error(error);
                alert(error.response?.data?.error || "Erro ao salvar produto.");
            }
        },

        abrirModalExcluir(produto){
            this.produtoAtual = { ...produto};
            this.modalExcluirAberto = true;
        },

        fecharModalExcluir(){
            this.modalExcluirAberto = false
            this.produtoAtual = {id_produto: null, name: "", description: "", price: "", image: ""}
        },

        async excluirProduto(){
            try{
                await api.delete(`/product/${this.produtoAtual.id_produto}`);
                alert("Produto excluído com sucesso!");
                this.fecharModalExcluir();
                this.carregarProdutos();
            } catch (error){
                console.error("Erro ao excluir produto:", error);
            }
        },

        formatarPreco(valor) {
            if (!valor) return "0,00 R$";
            return Number(valor).toLocaleString("pt-BR", {
                style: "currency",
                currency: "BRL"
            });
            }


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
    background-color: #d9d9d9;
    border-radius: 20px;
    padding: 6px 12px;
    width: 240px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.buscar:hover {
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
    width: 100%;
    font-size: 14px;
    color: #333;
}

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

.tabela-produtos {
    width: 100%;
    border-collapse: collapse;
    border-radius: 12px;
    overflow: hidden;
    background: #fff;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

.tabela-produtos th,
.tabela-produtos td {
    padding: 14px 18px;
    text-align: left;
    border-bottom: 1px solid #eee;
}

.tabela-produtos th {
    background-color: #222;
    color: #fff;
    font-weight: 600;
}

.tabela-produtos tr:hover td {
    background-color: #f6f6f6;
}

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

.mensagem-vazia {
    text-align: center;
    padding: 2rem;
    color: #777;
    font-style: italic;
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
