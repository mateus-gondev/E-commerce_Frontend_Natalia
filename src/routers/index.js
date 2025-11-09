import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import ProdutoDetalhe from '../views/ProdutoDetalhe.vue';
import Login from '../views/LoginPage/Login.vue';
import Cadastro from '../views/LoginPage/Cadastro.vue';
import Redefinir from '../views/LoginPage/Redefinir.vue';
import AdmHome from '../views/AdmPage/AdmHome.vue';
import AdmUsuario from '../views/AdmPage/AdmUsuario.vue';

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
    //Rotas ADM ----------------------------------
        {
        path: '/adm',
        name: 'AdmHome',
        component: AdmHome,
        },
        {
        path: '/adm/usuario',
        name: 'AdmUsuario',
        component: AdmUsuario,
        },
        {
        path: '/adm/usuario/novo',
        name: 'AdmForm',
        component: () => import('@/views/AdmPage/AdmForm.vue')
        }

];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;