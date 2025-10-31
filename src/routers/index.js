import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import ProdutoDetalhe from '../views/ProdutoDetalhe.vue';
import Login from '../views/LoginPage/Login.vue';
import Cadastro from '../views/LoginPage/Cadastro.vue';
import Redefinir from '../views/LoginPage/Redefinir.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    { 
        path: '/produto/:id',
        name: 'ProdutoDetalhe',
        component: ProdutoDetalhe 
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/cadastro',
        name: 'Cadastro',
        component: Cadastro,
    },
    {
        path: '/redefinir',
        name: 'Redefinir',
        component: Redefinir,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;