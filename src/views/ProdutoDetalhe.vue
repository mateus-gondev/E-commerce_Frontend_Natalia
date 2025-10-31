<template>

    <!--NAVBAR-->
    <div class="header">
        <navbar />
    </div>

    <main class="container-detalhes">
        <!--DETALHE DO PRODUTO-->
        <div class="container py-5">

            <router-link to="/" class="btn btn-outline-primary mb-4">
                <i class="bi bi-arrow-left me-2"></i> Voltar à loja
            </router-link>

            <div v-if="produto" class="row align-items-center">
                <div class="col-md-6">
                    <img :src="produto.img" class="img-fluid rounded shadow" :alt="produto.title" />
                </div>
                <div class="col-md-6">
                    <h2 class="mb-3">{{ produto.title }}</h2>
                    <p class="mb-4">{{ produto.desc }}</p>
                    <h4 class="text-primary mb-4">{{ produto.preco }}</h4>
                    <button class="btn btn-primary mt-3">Adicionar ao Carrinho</button>
                    <button class="btn btn-primary mt-3">Comprar</button>
                </div>
            </div>
        </div>
    </main>


    <!-- Cards -->
    <div id="pro">
        <Cards />
    </div>

    <!--FOOTER-->
    <div id="con">
        <Footer />
    </div>

</template>

<script>

import navbar from '@/components/navbar.vue'
import Cards from '@/components/Cards.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: "ProdutoDetalhe",
    components: {
        navbar,
        Cards,
        Footer
    },
    data() {
        return {
            produto: null
        };
    },
    methods: {
        carregarProduto(id) {
            const produtos = [
                {
                    id: 1,
                    img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_namoro_mini_encanto_2mm_anel_solitario_109_1_80e2a18588a47e1153771a7cb2a33777.jpeg",
                    title: "Anel Brilhante",
                    desc: "Anel delicado em ouro 18k com pedras de zircônia.",
                    preco: "R$ 200,00"
                },
                {
                    id: 2,
                    img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_namoro_mini_dulce_2mm_anel_solitario_103_1_b27b4a8587b80ff651e130218bd63b7e.jpeg",
                    title: "Anel de Ouro",
                    desc: "Peça elegante, perfeita para momentos especiais.",
                    preco: "R$ 320,00"
                },
                {
                    id: 3,
                    img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_casamento_italian_ouro_10k_1_5mm_anel_brinde_715_1_df6ce4eab3b68f75bd641d92fe52ab42.jpeg",
                    title: "Anel de Casamento",
                    desc: "Par de alianças em ouro 10k, design clássico e sofisticado.",
                    preco: "R$ 180,00"
                },
                {
                    id: 4,
                    img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_namoro_mini_encanto_2mm_anel_solitario_109_1_80e2a18588a47e1153771a7cb2a33777.jpeg",
                    title: "Anel Encanto",
                    desc: "Modelo exclusivo com acabamento em ouro e detalhes únicos.",
                    preco: "R$ 200,00"
                }
            ];

            this.produto = produtos.find(p => Number(p.id) === Number(id)) || null;
        }
    },
    created() {
        const id = this.$route.params.id;
        this.carregarProduto(id);
    },
    watch: {
        '$route.params.id'(novoId) {
        this.carregarProduto(novoId);
        }
    }

};
</script>

<style scoped>
img {
    max-height: 400px;
    object-fit: cover;
}

.container-detalhes {
    margin-top: 300px;

}

/* Botão voltar */
.btn-outline-primary {
    border-color: #b28b49;
    color: #b28b49;
    font-weight: 500;
    border-radius: 10px;
    transition: all 0.3s ease;
}

.btn-outline-primary:hover {
    background-color: #b28b49;
    color: #fff;
}

/* Imagem do produto */
img {
    max-height: 420px;
    object-fit: cover;
    border-radius: 16px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
}

/* Informações do produto */
h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #2b2b2b;
}

p {
    color: #5f5f5f;
    font-size: 1.05rem;
    line-height: 1.6;
}

.text-primary {
    color: #b28b49 !important;
    font-weight: 600;
}

/* Botões principais */
.btn.btn-primary {
    background-color: #b28b49;
    border: none;
    font-weight: 600;
    border-radius: 10px;
    padding: 10px 24px;
    margin-right: 10px;
    transition: all 0.3s ease;
}

.btn.btn-primary:hover {
    background-color: #a17a38;
    transform: translateY(-2px);
}

.btn.btn-primary:last-of-type {
    background-color: #000;
    color: #fff;
}

.btn.btn-primary:last-of-type:hover {
    background-color: #333;
}

/* Layout responsivo */
@media (max-width: 992px) {
    .container-detalhes {
        margin-top: 120px;
        padding: 20px;
    }

    img {
        max-height: 320px;
        width: 100%;
    }

    h2 {
        font-size: 1.7rem;
        margin-top: 20px;
    }

    .btn.btn-primary {
        width: 100%;
        margin-bottom: 10px;
    }
}
</style>
