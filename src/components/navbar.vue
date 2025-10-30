<template>
    <header :class="{ 'scrolled': isScrolled }">
        <nav class="navbar">

            <div class="navbar-top" v-show="!isScrolled">
                <img src="@/assets/imgs/logo_natalia.jpeg" alt="Logo" class="logo" />
            </div>

            <div class="navbar-bottom">
                <div class="buscar">
                    <img src="@/assets/icons/iconLupa.png" alt="Buscar" />
                    <input type="text" placeholder="Encontre sua joia..." />
                </div>

                <ul class="menu">
                    <li class="link"><a href="#">Home</a></li>
                    <li class="link"><a href="#cate">Categorias</a></li>
                    <li class="link"><a href="#pro">Produtos</a></li>
                    <li class="link"><a href="#con">Contato</a></li>
                </ul>

                <div class="navbar-right">
                    <div class="ms-auto d-flex align-items-center">
                        <button class="btn-carrinho" @click="abrirCarrinho" title="Ver carrinho">
                            <img src="@/assets/icons/iconCarrinho.png" alt="Carrinho" />
                        </button>
                    </div>

                    <CarrinhoLateral ref="carrinhoRef" />

                    <p class="divisao"> | </p>

                    <div class="cont-bentrar">
                        <button class="btn-Entrar" @click="abrirMenu" title="Entrar">
                            <img src="@/assets/icons/iconEntrar.png" alt="Ent" />
                        </button>
                    </div>

                    <ModalLogin ref="modalRef"/>

                </div>
            </div>
        </nav>
    </header>

</template>

<script>
import CarrinhoLateral from "../components/CarrinhoLateral.vue";
import ModalLogin from "../components/Login/ModalLogin.vue";

export default {
    name: "navbar",
    components: { 
        CarrinhoLateral,
        ModalLogin
    },
    data() {
        return {
            isScrolled: false,
        };
    },
    mounted() {
        window.addEventListener("scroll", this.handleScroll);
    },
    beforeUnmount() {
        window.removeEventListener("scroll", this.handleScroll);
    },
    methods: {
        handleScroll() {
            this.isScrolled = window.scrollY > 80; // ao rolar mais de 80px, ativa o modo compacto
        },
        abrirCarrinho() {
            this.$refs.carrinhoRef.abrirCarrinho();
        },
        abrirMenu() {
            this.$refs.modalRef.abrirMenu();
        },
    },
};
</script>


<style scoped>
:root {
    --preto: #141414;
    --azul: #4e31d0;
    --branco: #FFFFFF;
    --banco-cinza: #C5C5C5;
}

header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 9999;
    background-color: var(--branco);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.navbar {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 1050;
    background-color: #fff;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.navbar-top {
    display: flex;
    justify-content: center;
    align-items: center;
}

.logo {
    height: 150px;
    transition: transform 0.3s ease;
    cursor: pointer;
}

.logo:hover {
    transform: scale(1.08);
}

.navbar-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 85%;
    padding: 10px 0;
    border-top: 1px solid var(--banco-cinza);
    margin-bottom: 20px;
}

.buscar {
    display: flex;
    align-items: center;
    background-color: var(--banco-cinza);
    border-radius: 20px;
    padding: 6px 12px;
    width: 240px;
    transition: all 0.3s ease;
}

.buscar:hover {
    background-color: #d9d9d9;
}

.buscar img {
    width: 18px;
    margin-right: 8px;
    opacity: 0.8;
}

.buscar input {
    background: none;
    border: none;
    outline: none;
    color: var(--preto);
    width: 100%;
    font-size: 14px;
}

/* ===== MENU CENTRAL ===== */
.menu {
    list-style: none;
    display: flex;
    align-items: center;
    gap: 25px;
    margin-right: 180px;
}

.menu .link li {
    display: flex;
    align-items: center;
}

.menu li:not(:last-child)::after {
    content: "|";
    margin-left: 25px;
    color: var(--banco-cinza);
    font-weight: 300;
}

.menu .link a {
    text-decoration: none;
    color: var(--preto);
    font-weight: 600;
    font-size: 15px;
    transition: color 0.3s ease;
}

.menu .link a:hover {
    color: rgb(214, 171, 41);
}

.navbar-right {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}


.carrinho img {
    width: 28px;
    cursor: pointer;
    transition: transform 0.3s ease;
}

.carrinho img:hover {
    transform: scale(1.1);
}

.divisao{
    margin-top: 15px;
}

.btn-Entrar,
.btn-carrinho {
    background: none;
    border: none;
    padding: 6px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.2s ease, opacity 0.2s ease;
}

.btn-Entrar img,
.btn-carrinho img {
    width: 26px;
    height: 26px;
    transition: transform 0.3s ease;
    filter: brightness(0) saturate(100%) invert(15%) sepia(7%) saturate(700%) hue-rotate(180deg) brightness(90%) contrast(90%);
}

.btn-Entrar:hover img,
.btn-carrinho:hover img {
    transform: scale(1.15);
    filter: brightness(0) saturate(100%) invert(40%) sepia(90%) saturate(1000%) hue-rotate(200deg);
}

.btn-carrinho:active {
    transform: scale(0.9);
}

/* ===== RESPONSIVIDADE ===== */
@media (max-width: 950px) {
    .navbar-bottom {
        flex-direction: column;
        gap: 12px;
    }

    .menu {
        flex-direction: column;
        gap: 8px;
    }

    .menu li:not(:last-child)::after {
        content: none;
    }

    .buscar {
        width: 80%;
    }

    .logo {
        height: 60px;
    }
}

/* ===== ANIMAÇÃO SCROLL ===== */
header {
    transition: all 0.4s ease;
}

header.scrolled {
    background-color: #ffffffcc;
    backdrop-filter: blur(6px);
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

header.scrolled .navbar {
    padding: 6px 0;
}

header.scrolled .navbar-bottom {
    padding: 4px 0;
    margin-top: 10px;
    margin-bottom: -5px;
}

header.scrolled .logo {
    opacity: 0;
    visibility: hidden;
    height: 0;
    margin: 0;
    transition: all 0.3s ease;
}
</style>
