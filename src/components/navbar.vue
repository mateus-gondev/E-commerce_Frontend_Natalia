<template>
    <header>
        <nav class="navbar">
            
            <div class="navbar-top">
                <img src="@/assets/imgs/logo_natalia.jpeg" alt="Logo" class="logo" />
            </div>

            <div class="navbar-bottom">
                
                <div class="buscar">
                    <img src="@/assets/icons/iconLupa.png" alt="Buscar" />
                    <input type="text" placeholder="Encontre sua joia..." />
                </div>

                <ul class="menu">
                    <li class="link"><router-link to="/">Home</router-link></li>
                    <li class="link"><router-link to="#">Categorias</router-link></li>
                    <li class="link"><router-link to="#">Produtos</router-link></li>
                    <li class="link"><router-link to="#">Contato</router-link></li>
                </ul>

                <div class="navbar-right">
                    <div class="ms-auto d-flex align-items-center">
                        <button class="btn-carrinho" @click="abrirCarrinho" title="Ver carrinho">
                            <img src="@/assets/icons/iconCarrinho.png" alt="Carrinho" />
                        </button>
                    </div>

                    <CarrinhoLateral ref="carrinhoRef" />

                    <div class="cadastro">
                        <a class="cad-a" href="#">Registre-se</a>
                    </div>

                    <div class="login">
                        <a class="log-a" href="#">Login</a>
                    </div>
                </div>
            </div>
        </nav>
    </header>
</template>

<script>
import CarrinhoLateral from "../components/CarrinhoLateral.vue";

export default {
    name: "navbar",
    components: {
        CarrinhoLateral
    },
    methods: {
        abrirCarrinho() {
            this.$refs.carrinhoRef.abrirCarrinho();
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
    margin-top: 8px;
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

.cadastro .cad-a,
.login .log-a {
    text-decoration: none;
    font-weight: 600;
    border-radius: 17px;
    padding: 6px 14px;
    transition: all 0.3s ease;
    display: inline-block;
}

.cadastro .cad-a {
    background-color: var(--azul);
    color: var(--branco);
}

.cadastro .cad-a:hover {
    background-color: #e6e6e6;
}

.login .log-a {
    background-color: var(--banco-cinza);
    color: var(--preto);
}

.login .log-a:hover {
    background-color: #e6e6e6;
}

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

.btn-carrinho img {
    width: 26px;
    height: 26px;
    transition: transform 0.3s ease;
    filter: brightness(0) saturate(100%) invert(15%) sepia(7%) saturate(700%) hue-rotate(180deg) brightness(90%) contrast(90%);
}

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
</style>
