<template>

    <!--Importação - NAVBAR-->
    <div class="header">
        <navbar />
    </div>

    <!--Banner das joias-->
    < <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
                aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
                aria-label="Slide 3"></button>
        </div>

        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="@/assets/imgs/banner1.jpg" class="d-block w-100" alt="..." />
            </div>
            <div class="carousel-item">
                <img src="@/assets/imgs/banner2.jpg" class="d-block w-100" alt="..." />
            </div>
            <div class="carousel-item">
                <img src="@/assets/imgs/banner3.jpg" class="d-block w-100" alt="..." />
            </div>
        </div>

        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Anterior</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Próximo</span>
        </button>
        </div>

</template>

<script>
import navbar from '@/components/navbar.vue'

export default {
    name: "Home",
    components: {
        navbar
    }

};
</script>

<style scoped>
    .carousel.slide {
        margin-top: 18rem;
    }

    .carousel.slide img {
        width: 100%;
        height: 300px;
        object-fit: cover;
    }

    .carousel-control-prev-icon,
    .carousel-control-next-icon {
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 50%;
        width: 45px;
        height: 45px;
        background-size: 60%;
        background-position: center;
    }

    .carousel-control-prev-icon:hover,
    .carousel-control-next-icon:hover {
        background-color: rgba(0, 0, 0, 0.8);
        transform: scale(1.1);
        transition: all 0.3s ease;
    }

    .carousel-control-prev,
    .carousel-control-next {
        width: 5%;
        opacity: 1;
    }
</style>
