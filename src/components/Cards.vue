<template>
    <div class="container-carrossel">
        <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <!-- SLIDES -->
            <div
            v-for="(slide, slideIndex) in responsiveSlides"
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
                    <a href="#" class="btn btn-primary">Adicionar</a>
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
import "../assets/css/responsivo/cards_responsivo.css";

export default {
    name: "Cards",
    data() {
        return {
            cards: [
                {
                id: 1,
                img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_namoro_mini_encanto_2mm_anel_solitario_109_1_80e2a18588a47e1153771a7cb2a33777.jpeg",
                title: "Anel Brilhante",
                desc: "Anel delicado em ouro 18k com pedras de zircônia.",
                preco: "R$ 200,00",
                },
                {
                id: 2,
                img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_namoro_mini_dulce_2mm_anel_solitario_103_1_b27b4a8587b80ff651e130218bd63b7e.jpeg",
                title: "Anel Ouro Rosé",
                desc: "Anel romântico com banho de ouro rosé.",
                preco: "R$ 320,00",
                },
                {
                id: 3,
                img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_casamento_italian_ouro_10k_1_5mm_anel_brinde_715_1_df6ce4eab3b68f75bd641d92fe52ab42.jpeg",
                title: "Anel Clássico",
                desc: "Anel em ouro 10k, símbolo de união e elegância.",
                preco: "R$ 180,00",
                },
                {
                id: 4,
                img: "https://images.tcdn.com.br/img/img_prod/1373873/180_aliancas_de_namoro_mini_encanto_2mm_anel_solitario_109_1_80e2a18588a47e1153771a7cb2a33777.jpeg",
                title: "Anel Minimalista",
                desc: "Design simples e elegante para o dia a dia.",
                preco: "R$ 250,00",
                },
            ],
        };
    },
    computed: {
        responsiveSlides() {
        // Detecta se está em modo mobile
        const isMobile = window.innerWidth < 992;
        const chunkSize = isMobile ? 1 : 3;

        const slides = [];
        for (let i = 0; i < this.cards.length; i += chunkSize) {
            slides.push(this.cards.slice(i, i + chunkSize));
        }
        return slides;
        },
    },
    methods: {
        verDetalhes(id) {
        this.$router.push(`/produto/${id}`);
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
