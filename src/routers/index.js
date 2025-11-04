import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Cadastro from '../views/Cadastro.vue';
import RedSenha from '../views/RedSenha.vue';


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
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
        path: '/RedSenha',
        name: 'RedSenha',
        component: RedSenha,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;