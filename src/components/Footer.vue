<template>

    <div class="container-footer">
        <footer class="row row-cols-1 row-cols-sm-2 row-cols-md-5 py-5 my-5 border-top">

            <div class="col mb-3"> 
                <img src="@/assets/imgs/logo_natalia.jpeg" alt="Logo" class="logo-footer" />
            </div>

            <div class="col mb-3"></div>
            <div class="col mb-3">
                <h5>Caminhos</h5>
                <ul class="nav flex-column">
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Home</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Categoria</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Produto</a></li>
                </ul>
            </div>
            <div class="col mb-3">
                <h5>Contato</h5>
                <ul class="nav flex-column">
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Telefone</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">E-mail</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">WhatsApp</a></li>
                </ul>
            </div>
            <div class="col mb-3">
                <h5>Redes Socias</h5>
                <ul class="nav flex-column">
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Instagram</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Facebook</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Likedin</a></li>
                </ul>
            </div>
        </footer>
    </div>

</template>

<script>
    export default{
        name: "footer"
    }

</script>

<style scoped>

.logo-footer{
    height: 170px;
    width: 200px;
    transition: transform 0.3s ease;
    cursor: pointer;
    margin-left: 20px;
}

.logo-footer:hover {
    transform: scale(1.08);
}

</style>