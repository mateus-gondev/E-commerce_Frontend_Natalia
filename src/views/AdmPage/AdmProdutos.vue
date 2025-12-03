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
                        <tr v-for="produto in produtos" :key="produto.id_produtos">
                            <td>{{ produto.id_produtos }}</td>
                            <td>{{ produto.nome }}</td>
                            <td>{{ produto.descricao }}</td>
                            <td>{{ produto.preco }}</td>
                            <td>{{ produto.imagem_url }}</td>
                            <td>
                                <button class="btn-edit" @click="abrirModal(user)">Editar</button>
                                <button class="btn-delete" @click="abrirModalExcluir(user)">Excluir</button>
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
                    <input v-model="produto.name" type="text" placeholder="Nome">

                    <label>Descrição:</label>
                    <input v-model="produto.description" type="text" placeholder="Descrição">

                    <label>Preço:</label>
                    <input v-model="produto.prince" type="number" placeholder="Preço">

                    <label>Imagem URL:</label>
                    <input v-model="produto.image" type="text" placeholder="Imagem URL">

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
                        <button @click="excluirProduto()Sim"></button>
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

export default {
    name: "AdmProdutos",
    components: {AdmNavbar},
    data(){
        return {
            produtos: [],
            produtoAtual: { id_produto: null, name: "", description: "", prince: "", image: ""},
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
                u.prince.toLowerCase().includes(termo)
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
            this.produtoAtual = {id_produto: null, name: "", description: "", prince: "", image: ""}
        },

        async salvarProduto(dados){
            try{
                if (this.modoEdicao){
                    await api.put(`/product/${this.produtoAtual.id_produto}`,{
                        name: this.produtoAtual.name,
                        description: this.produtoAtual.description,
                        prince: this.produtoAtual.prince,
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
            this.ModalExcluirAberto = false
            this.produtoAtual = {id_produto: null, name: "", description: "", prince: "", image: ""}
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

.mensagem-vazia {
    text-align: center;
    padding: 2rem;
    color: #777;
    font-style: italic;
}

/* Conteúdo principal */
.adm-content {
    margin-left: 250px;
    padding: 2rem;
    width: 100%;
    min-height: 100vh;
}

</style>