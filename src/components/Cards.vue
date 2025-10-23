<template>
    <div class="container-carrossel">
        <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">

                <!-- SLIDE 1 -->
                <div class="carousel-item active">
                    <div class="card-group">
                        <div class="card" v-for="(card, index) in cards" :key="'slide1-' + index">
                            <img :src="card.img" class="card-img-top" :alt="card.title">
                            <div class="card-body">
                                <h5 class="card-title">{{ card.title }}</h5>
                                <p class="card-text">{{ card.desc }}</p>
                                <p class="card-preco">{{ card.preco }}</p>
                                <a href="#" class="btn btn-primary">Adicionar</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- SLIDE 2 -->
                <div class="carousel-item">
                    <div class="card-group">
                        <div class="card" v-for="(card, index) in cards" :key="'slide2-' + index">
                            <img :src="card.img" class="card-img-top" :alt="card.title">
                            <div class="card-body">
                                <h5 class="card-title">{{ card.title }}</h5>
                                <p class="card-text">{{ card.desc }}</p>
                                <p class="card-preco">{{ card.preco }}</p>
                                <a href="#" class="btn btn-primary">Adicionar</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- SLIDE 3 -->
                <div class="carousel-item">
                    <div class="card-group">
                        <div class="card" v-for="(card, index) in cards" :key="'slide3-' + index">
                            <img :src="card.img" class="card-img-top" :alt="card.title">
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

            <!-- Botões do carrossel -->
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Anterior</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Próximo</span>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "Cards",
    data() {
        return {
            cards: [
                {
                    img: "https://img.irroba.com.br/fit-in/250x250/filters:format(webp):fill(fff):quality(80)/inspiryc/catalog/whatsapp-image-2025-02-04-at-181126.jpeg",
                    title: "Anel Brilhante",
                    desc: "Anel delicado em ouro 18k com pedras de zircônia.",
                    preco: "R$ 200,00"
                },
                {
                    img: "https://img.irroba.com.br/fit-in/250x250/filters:format(webp):fill(fff):quality(80)/inspiryc/catalog/whatsapp-image-2025-10-10-at-122405.jpeg",
                    title: "Colar Elegance",
                    desc: "Colar refinado com acabamento de alta joalheria.",
                    preco: "R$ 320,00"
                },
                {
                    img: "https://img.irroba.com.br/fit-in/250x250/filters:format(webp):fill(fff):quality(80)/inspiryc/catalog/whatsapp-image-2025-08-07-at-124409.jpeg",
                    title: "Brincos Clássicos",
                    desc: "Par de brincos folheados a ouro com design sofisticado.",
                    preco: "R$ 180,00"
                }
            ]
        };
    }
};
</script>

<style scoped>
.container-carrossel {
    margin: 5rem auto;
    max-width: 1200px;
}

.card-group {
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
}

.card {
    width: 18rem;
    border: none;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease-in-out;
    background: #fff;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.card-img-top {
    height: 250px;
    object-fit: cover;
    border-bottom: 2px solid #f5f5f5;
}

.card-body {
    text-align: center;
    padding: 1rem 1.2rem;
}

.card-title {
    font-weight: 600;
    color: #222;
    margin-bottom: 0.5rem;
}

.card-text {
    font-size: 0.9rem;
    color: #555;
    margin-bottom: 0.7rem;
}

.card-preco {
    font-size: 1.1rem;
    font-weight: bold;
    color: #0d6efd;
    margin-bottom: 1rem;
}

.btn-primary {
    background-color: #0d6efd;
    border: none;
    border-radius: 50px;
    padding: 0.5rem 1.2rem;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background-color: #084298;
}

/* Ajustes do carrossel */
.carousel-control-prev-icon,
.carousel-control-next-icon {
    background-color: rgba(0, 0, 0, 0.6);
    border-radius: 50%;
    width: 45px;
    height: 45px;
    background-size: 60%;
    transition: all 0.3s ease;

}

.carousel-control-prev-icon:hover,
.carousel-control-next-icon:hover {
    background-color: rgba(0, 0, 0, 0.8);
    transform: scale(1.1);
}
</style>
