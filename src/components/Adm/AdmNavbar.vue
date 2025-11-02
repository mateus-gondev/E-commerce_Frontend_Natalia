<template>
    <header>
        <nav class="AdmNavbar">
            <div class="sidebar">
                <div href="/" class="logo">
                    <img class="icon-logo" src="@/assets/icons/iconLogo.png" alt="logo" />
                    <span class="fs-4">Acesso Adm</span>
                </div>
                <hr>
                <ul class="menu">
                    <li>
                        <a href="#" class="active">
                            <img src="@/assets/icons/iconPedido.png" alt="Pedido" />
                            Pedido
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <img src="@/assets/icons/iconProdutos.png" alt="Produtos" />
                            Produtos
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <img src="@/assets/icons/iconUser.png" alt="Usuários" />
                            Usuários
                        </a>
                    </li>
                    <li>
                        <a class="cont-sair" href="#" >
                            <img src="@/assets/icons/iconSair.png" alt="Sair" />
                            Sair
                        </a>
                    </li>
                </ul>
                <hr>
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
    --preto: #141414;
    --azul: #4e31d0;
    --branco: #ffffff;
    --banco-cinza: #c5c5c5;
}

.icon-logo{
    width: 40px;
    height: 40px;
    margin-bottom: 10px;
    margin-left: -5px;
}

.AdmNavbar {
    background-color: var(--preto);
    width: 250px;
    height: 100vh;
    padding: 1.5rem;
    box-shadow: 4px 0 15px rgba(0, 0, 0, 0.2);
    color: var(--branco);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: fixed;
    left: 0;
    top: 0;
}

.sidebar .fs-4 {
    font-weight: 700;
    margin-left: 10px;
}

.sidebar hr {
    border: none;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    margin: 1.5rem 0;
}

.sidebar .menu {
    list-style: none;
    padding: 0;
    margin: 0;
}

.sidebar .menu li {
    margin-bottom: 1rem;
}

.sidebar .menu li:hover{
    color: rgb(214, 171, 41);
}

.sidebar .menu a {
    color: var(--banco-cinza);
    display: flex;
    align-items: center;
    font-weight: 500;
    border-radius: 12px;
    padding: 0.75rem 1rem;
    text-decoration: none;
    transition: all 0.3s ease;
}

.sidebar .menu a img {
    width: 22px;
    margin-right: 10px;
    opacity: 0.8;
    transition: 0.3s ease;
}

.sidebar .menu a:hover,
.sidebar .menu a.active {
    background-color: var(--azul);
    color: var(--branco);
}

.sidebar .menu a:hover img,
.sidebar .menu a.active img {
    opacity: 1;
    transform: scale(1.1);
}

.menu .cont-sair{
    margin-top: 250px;
    margin-left: 45px;
}

</style>
