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
                        data-bs-slide-to="2" aria-label="Slide 3" class=""></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="@/assets/imgs/banner1.png" class="d-block w-100" alt="Banner 1" />
                        <div class="carousel-caption">
                            <h1>Nova coleção de joias 2025</h1>
                            <p>Peças exclusivas com até 30% de desconto.</p>
                            <p><a class="btn btn-lg btn-primary" href="#">Ver agora</a></p>
                        </div>
                    </div>
                    <div class="carousel-item active">
                        <img src="@/assets/imgs/banner2.png" class="d-block w-100" alt="Banner 1" />
                        <div class="carousel-caption">
                            <h1>Nova coleção de joias 2025</h1>
                            <p>Peças exclusivas com até 30% de desconto.</p>
                            <p><a class="btn btn-lg btn-primary" href="#">Ver agora</a></p>
                        </div>
                    </div>

                    <div class="carousel-item active">
                        <img src="@/assets/imgs/banner3.png" class="d-block w-100" alt="Banner 1" />
                        <div class="carousel-caption">
                            <h1>Nova coleção de joias 2025</h1>
                            <p>Peças exclusivas com até 30% de desconto.</p>
                            <p><a class="btn btn-lg btn-primary" href="#">Ver agora</a></p>
                        </div>
                    </div>
                </div>

                <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span> <span
                        class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span> <span
                        class="visually-hidden">Next</span>
                </button>
            </div>
        </div>

        <h2 class="titulo-categoria">Encontre a sua joia</h2>
        <p class="subtitulo-categoria">Luxo e design para quem é livre para brilhar</p>


        <!--Categorias-->
        <div class="container-categoria">

            <!--Cad-Categoria-->
            <div class="col-lg-4"> 
                <img src="@/assets/imgs/categoria1.png" class="d-block w-100" alt="Cat" />
                <h2 class="fw-normal">Anéis</h2>
                <p><a class="btn btn-secondary" href="#">Ver detalhes »</a></p>
            </div>

            <!--Cad-Categoria-->
            <div class="col-lg-4"> 
                <img src="@/assets/imgs/categoria2.png" class="d-block w-100" alt="Cat" />
                <h2 class="fw-normal">Anéis</h2>
                <p><a class="btn btn-secondary" href="#">Ver detalhes »</a></p>
            </div>

            <!--Cad-Categoria-->
            <div class="col-lg-4"> 
                <img src="@/assets/imgs/categoria3.png" class="d-block w-100" alt="Cat" />
                <h2 class="fw-normal">Anéis</h2>
                <p><a class="btn btn-secondary" href="#">Ver detalhes »</a></p>
            </div>

            <!--Cad-Categoria-->
            <div class="col-lg-4"> 
                <img src="@/assets/imgs/categoria4.png" class="d-block w-100" alt="Cat" />
                <h2 class="fw-normal">Anéis</h2>
                <p><a class="btn btn-secondary" href="#">Ver detalhes »</a></p>
            </div>

        </div>

        <!-- Cards -->
        <Cards />

        

    </main>
    <footer>
        <Footer />
    </footer>
</template>


<script>
import navbar from '@/components/navbar.vue'
import Cards from '@/components/Cards.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: "Home",
    components: {
        navbar,
        Cards,
        Footer
    }
}
    
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

/* ====== CONTAINER DE CATEGORIAS ====== */
.container-categoria {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2.5rem;
    max-width: 1200px;
    margin: 4rem auto 6rem auto;
    padding: 0 1.5rem;
    text-align: center;
}

/* ====== CARD INDIVIDUAL ====== */
.col-lg-4 {
    width: 220px;
    background: #fff;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    transition: all 0.35s ease;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.col-lg-4 img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-bottom: 1px solid #eee;
    transition: transform 0.4s ease;
}

.col-lg-4:hover img {
    transform: scale(1.05);
}

.col-lg-4 h2 {
    font-size: 1.1rem;
    font-weight: 600;
    color: #222;
    margin-top: 1rem;
    margin-bottom: 0.3rem;
}

.col-lg-4 p {
    margin-bottom: 1.2rem;
}

.col-lg-4 p a {
    display: inline-block;
    font-size: 0.9rem;
    font-weight: 500;
    color: #222;
    text-decoration: none;
    border: 1px solid #ccc;
    padding: 0.45rem 1.2rem;
    border-radius: 50px;
    background-color: #fff;
    transition: all 0.3s ease;
}

.col-lg-4 p a:hover {
    background-color: #b38b59;
    color: #fff;
    border-color: #b38b59;
}


.col-lg-4:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}


.titulo-categoria {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    color: #222;
    margin-top: 3rem;
}

.subtitulo-categoria {
    text-align: center;
    font-size: 1rem;
    color: #666;
    margin-bottom: 2rem;
}

/* ====== RESPONSIVIDADE ====== */
@media (max-width: 768px) {
    .container-categoria {
        gap: 1.5rem;
    }

    .col-lg-4 {
        width: 160px;
    }

    .col-lg-4 img {
        height: 160px;
    }

    .col-lg-4 h2 {
        font-size: 1rem;
    }
}


</style>
