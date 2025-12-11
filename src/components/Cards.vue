<template>
    <div class="container-carrossel">
        <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <!-- SLIDES 1 -->
            <div
            v-for="(slide, slideIndex) in slides"
            :key="slideIndex"
            class="carousel-item"
            :class="{ active: slideIndex === 0 }"
            >
            <div class="card-group">
                <div
                class="card"
                v-for="(card, index) in slide"
                :key="`card-${slideIndex}-${index}`"
                @click="verDetalhes(card.id)"
                >
                <img :src="card.img" class="card-img-top" :alt="card.title" />
                <div class="card-body">
                    <h5 class="card-title">{{ card.title }}</h5>
                    <p class="card-text">{{ card.desc }}</p>
                    <p class="card-preco">{{ card.preco }}</p>
                </div>
                </div>
            </div>
            </div>
            <!-- SLIDES 2 -->
            <div
            v-for="(slide, slideIndex) in slides"
            :key="slideIndex"
            class="carousel-item"
            :class="{ active: slideIndex === 0 }"
            >
            <div class="card-group">
                <div
                class="card"
                v-for="(card, index) in slide"
                :key="`card-${slideIndex}-${index}`"
                @click="verDetalhes(card.id)"
                >
                <img :src="card.img" class="card-img-top" :alt="card.title" />
                <div class="card-body">
                    <h5 class="card-title">{{ card.title }}</h5>
                    <p class="card-text">{{ card.desc }}</p>
                    <p class="card-preco">{{ card.preco }}</p>
                    <button class="btn btn-primary mt-3 me-2" @click="addProduto(produto)">Adicionar ao Carrinho</button>
                </div>
                </div>
            </div>
            </div>
        </div>

        <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselExample"
            data-bs-slide="prev"
        >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Anterior</span>
        </button>

        <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselExample"
            data-bs-slide="next"
        >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Próximo</span>
        </button>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import "../assets/css/responsivo/cards_responsivo.css";

export default {
    name: "Cards",

    data() {
        return {
            cards: [],      // Agora vazio (preenchido pelo backend)
            slides: [],
            produto: null,
            produtos: [],
        };
    },

    async mounted() {
        await this.carregarCards();
        this.generateSlides();

        window.addEventListener("resize", this.generateSlides);
    },

    beforeUnmount() {
        window.removeEventListener("resize", this.generateSlides);
    },

    methods: {
        async carregarCards() {
            try {
                const response = await axios.get("http://10.100.0.158:5000/api/product");

                const produtos = response.data;

                // Adapta os nomes para o Vue (se quiser manter os mesmos nomes antigos)
                this.cards = produtos.map((p) => ({
                    id: p.id_produto,
                    img: p.image,
                    title: p.name,
                    desc: p.description,
                    preco: `R$ ${p.price}`,
                }));
            } catch (error) {
                console.error("Erro ao carregar os cards:", error);
            }
        },

        generateSlides() {
            const width = window.innerWidth;

            let chunkSize = 4;
            if (width < 768) chunkSize = 1;
            else if (width < 992) chunkSize = 2;
            else chunkSize = 4;

            const tempSlides = [];
            for (let i = 0; i < this.cards.length; i += chunkSize) {
                tempSlides.push(this.cards.slice(i, i + chunkSize));
            }

            this.slides = tempSlides;
        },

        verDetalhes(id) {
            this.$router.push(`/produto/${id}`);
        },

        async carregarProduto(id) {
      try {
        const response = await api.get("/product");
        const produtosAPI = response.data;

        // Produto atual
        const p = produtosAPI.find(item => Number(item.id_produto) === Number(id));
        if (!p) return;

        this.produto = {
          id: p.id_produto,
          img: p.image,
          title: p.name,
          desc: p.description,
          preco: `R$ ${p.price}`,
        };

        // Lista completa para o carrossel
        this.produtos = produtosAPI.map(prod => ({
          id: prod.id_produto,
          img: prod.image,
          title: prod.name,
          desc: prod.description,
          preco: `R$ ${prod.price}`,
        }));

        console.log("Produtos carregados:", this.produtos);
      } catch (err) {
        console.error("Erro ao carregar produto:", err);
      }
    },
        addProduto(produto) {
            cartStore.add(produto);
            window.dispatchEvent(new Event("cart-updated"));
            },

            comprar(produto) {
            this.addProduto(produto);
            },

            created() {
    const id = this.$route.params.id;
    this.carregarProduto(id);
    window.scrollTo({ top: 0, behavior: "smooth" });
  },

  watch: {
    "$route.params.id"(novoId) {
      this.carregarProduto(novoId);
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
  },

    },
};
</script>



<style scoped>
.container-carrossel {
    margin: 4rem auto;
    max-width: 1100px;
    margin-bottom: 5rem;
}

.card-group {
    display: flex;
    justify-content: center;
    align-items: stretch;
    gap: 1.8rem;
    flex-wrap: nowrap;
}

.card {
    width: 15rem;
    background: #fff;
    border: none;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
    cursor: pointer;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
}

.card-img-top {
    height: 180px;
    object-fit: cover;
    border-bottom: 1px solid #eee;
    transition: transform 0.4s ease;
}

.card:hover .card-img-top {
    transform: scale(1.05);
}

.card-body {
    text-align: center;
    padding: 1rem 1rem 1.3rem;
}

.card-title {
    font-size: 1rem;
    font-weight: 600;
    color: #222;
    margin-bottom: 0.3rem;
}

.card-text {
    font-size: 0.85rem;
    color: #666;
    margin-bottom: 0.6rem;
    line-height: 1.3rem;
}

.card-preco {
    font-size: 1rem;
    font-weight: 700;
    color: #b38b59;
    margin-bottom: 0.8rem;
}

.btn-primary {
    background-color: #b38b59;
    border: none;
    border-radius: 50px;
    padding: 0.4rem 1.2rem;
    font-size: 0.85rem;
    font-weight: 500;
    color: #fff;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background-color: #8f7045;
    transform: scale(1.05);
}

.carousel-control-prev,
.carousel-control-next {
    width: auto;
    top: 35%;
    transform: translateY(-50%);
    opacity: 0.9;
}

.carousel-control-prev {
    left: 10px;
}

.carousel-control-next {
    right: 10px;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
    background-color: rgba(0, 0, 0, 0.45);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    background-size: 60%;
    transition: all 0.3s ease;
}

.carousel-control-prev-icon:hover,
.carousel-control-next-icon:hover {
    background-color: rgba(0, 0, 0, 0.75);
    transform: scale(1.1);
}

</style>
