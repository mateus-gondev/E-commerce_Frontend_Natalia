import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import ProdutoDetalhe from '../views/ProdutoDetalhe.vue';
import Login from '../views/LoginPage/Login.vue';
import Cadastro from '../views/LoginPage/Cadastro.vue';
import Redefinir from '../views/LoginPage/Redefinir.vue';
import AdmHome from '../views/AdmPage/AdmHome.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    //Rota detalhe do produto
    { 
        path: '/produto/:id',
        name: 'ProdutoDetalhe',
        component: ProdutoDetalhe 
    },
    //Rota Login
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    //Rota Cadastro
    {
        path: '/cadastro',
        name: 'Cadastro',
        component: Cadastro,
    },
    //Rota redefinir
    {
        path: '/redefinir',
        name: 'Redefinir',
        component: Redefinir,
    },
    //Rotas ADM
    {
    path: '/adm',
    name: 'AdmHome',
    component: AdmHome,
    }


];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;