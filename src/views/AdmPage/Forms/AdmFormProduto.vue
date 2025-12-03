<template>
    <div class="adm-layout">
        <AdmNavbar />
    </div>

    <main class="adm-content">
        <div class="form-container">
            <h1>{{ modoEdicao ? "Editar Usuário" : "Cadastrar Novo Produto" }}</h1>

            <form @submit.prevent="enviar">
                <div class="form-group">
                    <label for="nome">Nome:</label>
                    <input type="text" id="nome" v-model="produto.name">
                </div>

                <div class="form-group">
                    <label for="descricao">Descrição:</label>
                    <input type="text" id="descricao" v-model="produto.description">
                </div>

                <div class="form-group">
                    <label for="preco">Preço:</label>
                    <input type="number" id="preco" v-model="produto.price">
                </div>

                <div class="form-group">
                    <label for="imagem">Imagem:</label>
                    <input type="file" id="imagem" accept="image/*" v-model="produto.image">
                </div>
            </form>
        </div>
    </main>
</template>  

<script>
import api from "@/services/api";
import AdmNavbar from "../../components/Adm/AdmNavbar.vue";

export default {
    name: "AdmFormProduto",
    components: { AdmNavbar },
    data(){
        return {
            idProduto: null,
            modoEdicao: false,
            produto: {
                name: "",
                description: "",
                price: 0,
                image: null
            },
        };
    },
        async mounted() {
            this.idProduto = this.$route.params.id;
            if(this.idProduto){ 
                this.modoEdicao = true;
                const res = await api.get(`/products/${this.idProduto}`);
                this.produto = res.data;
            }
        },      
    methods: {
        async enviar(){
            try{
                if(this.modoEdicao){
                    await api.put(`/products/${this.idProduto}`, this.produto);
                    alert("Produto editado com sucesso!");
                }else{
                    await api.post("/products", this.produto);
                    alert("Produto cadastrado com sucesso!");
                } 
                this.voltar();
            }catch(error){
                alert(error.response?.data?.error || "Erro ao cadastrar produto");
            }
        },
        voltar(){
            this.$router.push("/adm/produtos");
        },
    },
}

</script>