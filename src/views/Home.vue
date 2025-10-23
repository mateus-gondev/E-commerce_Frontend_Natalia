<template>
    <div class="header">
        <navbar />
    </div>

    <main>
        <!-- Banner -->
        <div class="container-banner">
            <div class="fundo">
                <h1 class="fw-light">Descrição</h1>
                <p class="letras">
                    Something short and leading about the collection below—its contents,
                    the creator, etc. Make it short and sweet, but not too short so folks
                    don’t simply skip over it entirely.
                </p>
                <p><a href="#" class="btn btn-primary my-2">Comprar Agora</a></p>
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
    padding-top: 16rem;
}

.container-banner {
    text-align: center;
    margin: 0 auto;
    padding: 4rem 1rem;
    max-width: 1200px;
}

.fundo {
    color: rgb(0, 0, 0);
}

.container-fundo {
    align-items: center;
    text-align: center;
    display: flex;
    justify-content: center;
}
</style>
