<template>
    <header>
        <nav class="adm-navbar">
        <div class="sidebar">
        
            <div class="logo">
            <img class="icon-logo" src="@/assets/icons/iconLogo.png" alt="logo" />
            <span class="titulo">Gestão <span class="titulo-destaque">Site</span></span>
            </div>

            <hr />

            <ul class="menu">
                <li>
                    <router-link to="/adm">
                    <img src="@/assets/icons/iconPedido.png" alt="Pedido" />
                    Pedido
                    </router-link>
                </li>
                <li>
                    <router-link to="#">
                    <img src="@/assets/icons/iconProdutos.png" alt="Produtos" />
                    Produtos
                    </router-link>
                </li>
                <li>
                    <router-link to="/adm/usuario">
                    <img src="@/assets/icons/iconUser.png" alt="Usuários" />
                    Usuários
                    </router-link>
                </li>
            </ul>

            <div class="logout">
            <router-link to="/">
                <img src="@/assets/icons/iconSair.png" alt="Sair" />
                Sair
            </router-link>
            </div>
        </div>
        </nav>
    </header>
</template>

<script>
export default {
    name: "AdmNavbar"
}

</script>

<style scoped>
:root {
    --fundo: #1e1e1e;
    --branco: #ffffff;
    --cinza: #bdbdbd;
    --dourado: #d4af37;
    --dourado-escuro: #b18f2d;
}

.adm-navbar {
    background-color: var(--fundo);
    width: 250px;
    height: 100vh;
    padding: 2rem 1rem;
    color: var(--branco);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: fixed;
    left: 0;
    top: 0;
    box-shadow: 4px 0 20px rgba(0, 0, 0, 0.3);
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
}

.icon-logo {
    width: 38px;
    height: 38px;
}

.titulo {
    font-weight: 600;
    font-size: 1.2rem;
    letter-spacing: 0.5px;
    color: var(--branco);
}

.titulo-destaque {
    color: var(--dourado);
}

.sidebar hr {
    border: none;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    margin: 1.5rem 0;
}

.menu {
    list-style: none;
    padding: 0;
    margin: 0;
}

.menu li {
    margin-bottom: 0.6rem;
}

.menu a {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--cinza);
    font-weight: 500;
    border-radius: 10px;
    padding: 0.7rem 1rem;
    transition: all 0.3s ease;
}

.menu a img {
    width: 22px;
    opacity: 0.85;
    transition: transform 0.3s ease, opacity 0.3s ease;
}

.menu a:hover,
.menu a.router-link-exact-active {
    background-color: rgba(212, 175, 55, 0.1);
    color: var(--dourado);
}

.menu a:hover img,
.menu a.router-link-exact-active img {
    transform: scale(1.1);
    opacity: 1;
}

.menu a:hover {
    background-color: rgba(212, 175, 55, 0.06);
    color: var(--dourado);
}

.menu a.router-link-active,
.menu a.router-link-exact-active,
.menu a.is-active {  
    background-color: transparent;
    color: var(--dourado);
    position: relative;
    font-weight: 700;
}

.menu a.router-link-active::before,
.menu a.router-link-exact-active::before,
.menu a.is-active::before {
    content: "";
    position: absolute;
    left: 0;
    top: 8px;
    bottom: 8px;
    width: 4px;
    border-radius: 0 4px 4px 0;
    background: var(--dourado);
}

.menu a.router-link-active img,
.menu a.router-link-exact-active img,
.menu a.is-active img {
    opacity: 1;
    filter: none;
    transform: scale(1.03);
}

.menu a,
.menu a img {
    transition: background-color 0.18s ease, color 0.18s ease, transform 0.18s ease, opacity 0.18s ease;
}

.logout {
    margin-top: 280px;
    display: flex;
    justify-content: center;
}

.logout a {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    color: var(--dourado);
    font-weight: 600;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.logout a img {
    width: 22px;
    transition: transform 0.3s ease;
}

.logout a:hover {
    background-color: rgba(212, 175, 55, 0.15);
    color: var(--dourado-escuro);
}

.logout a:hover img {
    transform: translateX(-3px);
}
</style>

