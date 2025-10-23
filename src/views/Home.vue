<template>
    <div class="header">
        <navbar />
    </div>

    <main>
        <!-- Banner -->
        <div class="container-carrossel">
            <div id="myCarousel" class="carousel slide mb-6" data-bs-ride="carousel">
                <div class="carousel-indicators"> <button type="button" data-bs-target="#myCarousel"
                        data-bs-slide-to="0" class="" aria-label="Slide 1"></button> <button type="button"
                        data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2" class="active"
                        aria-current="true"></button> <button type="button" data-bs-target="#myCarousel"
                        data-bs-slide-to="2" aria-label="Slide 3" class=""></button> </div>
                <div class="carousel-inner">
                    <div class="carousel-item"> <svg aria-hidden="true" class="bd-placeholder-img " height="100%"
                            preserveAspectRatio="xMidYMid slice" width="100%" xmlns="http://www.w3.org/2000/svg">
                            <rect width="100%" height="100%" fill="var(--bs-secondary-color)"></rect>
                        </svg>
                        <div class="container">
                            <div class="carousel-caption text-start">
                                <h1>Example headline.</h1>
                                <p class="opacity-75">Some representative placeholder content for the first slide of the
                                    carousel.</p>
                                <p><a class="btn btn-lg btn-primary" href="#">Sign up today</a></p>
                            </div>
                        </div>
                    </div>
                    <div class="carousel-item active">
                        <img src="@/assets/imgs/banner1.png" class="d-block w-100" alt="Banner 1" />
                        <div class="carousel-caption">
                            <h1>Nova coleção de joias 2025</h1>
                            <p>Peças exclusivas com até 30% de desconto.</p>
                            <p><a class="btn btn-lg btn-primary" href="#">Ver agora</a></p>
                        </div>
                    </div>

                    <div class="carousel-item"> <svg aria-hidden="true" class="bd-placeholder-img " height="100%"
                            preserveAspectRatio="xMidYMid slice" width="100%" xmlns="http://www.w3.org/2000/svg">
                            <rect width="100%" height="100%" fill="var(--bs-secondary-color)"></rect>
                        </svg>
                        <div class="container">
                            <div class="carousel-caption text-end">
                                <h1>One more for good measure.</h1>
                                <p>Some representative placeholder content for the third slide of this carousel.</p>
                                <p><a class="btn btn-lg btn-primary" href="#">Browse gallery</a></p>
                            </div>
                        </div>
                    </div>
                </div> <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel"
                    data-bs-slide="prev"> <span class="carousel-control-prev-icon" aria-hidden="true"></span> <span
                        class="visually-hidden">Previous</span> </button> <button class="carousel-control-next"
                    type="button" data-bs-target="#myCarousel" data-bs-slide="next"> <span
                        class="carousel-control-next-icon" aria-hidden="true"></span> <span
                        class="visually-hidden">Next</span> </button>
            </div>
        </div>
        <!-- Cards -->
        <Cards />
    </main>
</template>


<script>
import navbar from '@/components/navbar.vue'
import Cards from '@/components/Cards.vue'

export default {
    name: "Home",
    components: {
        navbar,
        Cards
    }

};
</script>

<style scoped>
.header {
    position: relative;
    z-index: 1000;
}

main {
    padding-top: 8rem;
}

.container-carrossel {
    width: 100%;
    max-height: 500px;
    overflow: hidden;
    margin-top: 4rem;
}


.carousel-item img {
    width: 100%;
    height: 600px;
    object-fit: cover;
    filter: brightness(0.7);
}

.carousel-caption {
    bottom: 20%;
}

.carousel-caption h1 {
    font-size: 3rem;
    font-weight: 600;
    color: #fff;
    text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
}

.carousel-caption p {
    color: #f1f1f1;
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
}

.carousel-caption .btn {
    padding: 0.8rem 1.5rem;
    font-size: 1rem;
    border-radius: 50px;
}

.carousel-indicators button {
    background-color: #fff;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    opacity: 0.6;
}

.carousel-indicators .active {
    opacity: 1;
}

/* Botões de navegação */
.carousel-control-prev-icon,
.carousel-control-next-icon {
    filter: invert(100%);
}

/* Responsividade */
@media (max-width: 768px) {
    .carousel-caption h1 {
        font-size: 2rem;
    }

    .carousel-caption p {
        font-size: 1rem;
    }

    .carousel-item img {
        height: 400px;
    }
}
</style>
