<template>
    <header :class="{ 'scrolled': isScrolled }">
        <nav class="navbar">
        <!-- Logo -->
        <div class="navbar-top" v-show="!isScrolled">
            <img src="@/assets/imgs/logo_natalia.jpeg" alt="Logo" class="logo" />
        </div>

        <div class="navbar-bottom">
            <!-- Ícone de menu hamburguer -->
            <img
                src="@/assets/icons/iconMenu.png"
                alt="Menu"
                class="icon-menu"
                @click="toggleMenu"
            />

            <!-- Campo de busca -->
            <div class="buscar">
                <img src="@/assets/icons/iconLupa.png" alt="Buscar" />
                <input type="text" placeholder="Encontre sua joia..." />
            </div>

            <!-- Menu normal apenas desktop -->
            <ul class="menu-desktop">
                <li class="link"><a href="#">Home</a></li>
                <li class="link"><a href="#cate">Categorias</a></li>
                <li class="link"><a href="#pro">Produtos</a></li>
                <li class="link"><a href="#con">Contato</a></li>
            </ul>

            <!-- Lado direito -->
            <div class="navbar-right">
                <button class="btn-carrinho" @click="abrirCarrinho" title="Ver carrinho">
                    <img src="@/assets/icons/iconCarrinho.png" alt="Carrinho" />
                </button>

                <CarrinhoLateral ref="carrinhoRef" />
                <p class="divisao"> | </p>

                <div v-if="!user" class="cont-bentrar">
                    <button class="btn-Entrar" @click="abrirMenu" title="Entrar">
                        <img src="@/assets/icons/iconEntrar.png" alt="Entrar" />
                    </button>
                </div>

                <div v-else class="dropdown perfil">
                <a
                    href="#"
                    class="d-flex align-items-center text-decoration-none dropdown-toggle"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                >
                    <img
                    src="@/assets/imgs/perfil.png"
                    alt="Perfil"
                    width="35"
                    height="35"
                    class="rounded-circle me-2"
                    />
                    <strong>{{ user.name }}</strong>
                </a>
                <ul class="dropdown-menu text-small shadow">
                    <li><a class="dropdown-item" href="#">Meu Perfil</a></li>
                    <li><a class="dropdown-item" href="#">Minhas Compras</a></li>
                    <li><hr class="dropdown-divider" /></li>
                    <li><a class="dropdown-item" href="#" @click="logout">Sair</a></li>
                </ul>
                </div>

                <ModalLogin ref="modalRef" />
            </div>

            <!-- Menu Celular em ajustes -->
            <div class="menu-mobile" v-if="menuAberto">
                <div class="menu-overlay" @click="toggleMenu"></div>
                <div class="menu-content">
                <button class="close-btn" @click="toggleMenu">×</button>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#cate">Categorias</a></li>
                    <li><a href="#pro">Produtos</a></li>
                    <li><a href="#con">Contato</a></li>
                </ul>
                <div class="menu-login-mobile" v-if="!user">
                    <button class="btn-Entrar" @click="abrirMenu">
                    <img src="@/assets/icons/iconEntrar.png" alt="Entrar" />
                    Entrar
                    </button>
                </div>
                </div>
            </div>
            </div>

        </nav>
    </header>
</template>

<script>
import CarrinhoLateral from "../components/CarrinhoLateral.vue";
import ModalLogin from "../components/Login/ModalLogin.vue";
import storage from "@/services/storage";
import "@/assets/css/responsivo/navbar_responsivo.css";

export default {
    name: "navbar",
    components: { CarrinhoLateral, ModalLogin },
    data() {
        return {
        isScrolled: false,
        user: null,
        menuAberto: false,
        };
    },
    mounted() {
        window.addEventListener("scroll", this.handleScroll);
        window.addEventListener("user-login", this.loadUser);
        this.loadUser();
    },
    beforeUnmount() {
        window.removeEventListener("scroll", this.handleScroll);
        window.removeEventListener("user-login", this.loadUser);
    },
    methods: {
        handleScroll() {
            this.isScrolled = window.scrollY > 80;
        },
        abrirCarrinho() {
            this.$refs.carrinhoRef.abrirCarrinho();
        },
        abrirMenu() {
            setTimeout(() => {
                this.$router.push('/login');
            }, 400);
        },
        loadUser() {
            this.user = storage.getUser();
        },
        logout() {
            storage.clearUser();
            alert("👋 Você saiu da conta!");
            this.$router.push("/login");
        },
        toggleMenu() {
            this.menuAberto = !this.menuAberto;
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


.navbar-right {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}
/* ===== MENU DESKTOP (restaurando o estilo original) ===== */
.menu-desktop {
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 25px;
    margin-right: 180px;
    padding: 0;
}

/* Cada item do menu */
.menu-desktop .link {
    display: flex;
    align-items: center;
    position: relative;
}

/* Separador entre os itens */
.menu-desktop li:not(:last-child)::after {
    content: "|";
    margin-left: 25px;
    color: var(--banco-cinza);
    font-weight: 300;
}

/* Links */
.menu-desktop .link a {
    text-decoration: none;
    color: var(--preto);
    font-weight: 600;
    font-size: 15px;
    transition: color 0.3s ease;
}

/* Hover nos links */
.menu-desktop .link a:hover {
    color: rgb(214, 171, 41);
}

/* ===== RESPONSIVIDADE (esconde menu desktop em telas pequenas) ===== */
@media (max-width: 991px) {
    .menu-desktop {
        display: none !important;
    }
}



.carrinho img {
    width: 28px;
    cursor: pointer;
    transition: transform 0.3s ease;
}

.carrinho img:hover {
    transform: scale(1.1);
}

.divisao {
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
