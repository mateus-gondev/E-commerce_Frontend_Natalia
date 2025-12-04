<template> 
    <div class="adm-layout">
        <AdmNavbar />
    </div>

    <main class="adm-content">
        <div class="form-container">
            <h1>{{ modoEdicao ? "Editar Produto" : "Cadastrar Novo Produto" }}</h1>

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
                    <input type="text" id="imagem" v-model="produto.image">
                </div>

                <div class="acoes">
                    <button type="submit" class="btn-save">Salvar</button>
                    <button type="button" class="btn-cancel" @click="voltar">Cancelar</button>
                </div>
            </form>
        </div>
    </main>
</template>


<script>
import api from "@/services/api";
import AdmNavbar from "@/components/Adm/AdmNavbar.vue";

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
                const res = await api.get(`/product/${this.idProduto}`);
                this.produto = res.data;
            }
        },      
    methods: {
        async enviar(){
            try{
                if(this.modoEdicao){
                    await api.put(`/product/${this.idProduto}`, this.produto);
                    alert("Produto editado com sucesso!");
                }else{
                    await api.post("/product", this.produto);
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

<style scoped>

.adm-content {
    padding: 2rem;
    display: flex;
    justify-content: center;
}

.form-container {
    background: #fff;
    border-radius: 12px;
    padding: 2rem;
    max-width: 600px;
    width: 100%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.form-container h1 {
    margin-bottom: 1.5rem;
    font-size: 1.6rem;
    color: #2c3e50;
    text-align: center;
}

.form-group {
    margin-bottom: 1.2rem;
}

label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.5rem;
    }

input, select {
    width: 100%;
    padding: 0.6rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    }

.acoes {
    display: flex;
    justify-content: space-between;
    margin-top: 1.5rem;
}

.btn-save {
    background-color: #2c3e50;
    color: white;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}

.btn-save:hover {
    background-color: #34495e;
}

.btn-cancel {
    background-color: #ddd;
    color: #333;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}

.btn-cancel:hover {
    background-color: #bbb;
}
</style>
