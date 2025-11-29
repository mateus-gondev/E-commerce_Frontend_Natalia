import { createRouter, createWebHistory } from 'vue-router';
import adm_routers from './adm_routers';
import logins_routers from './logins_routers';
import home_routers from './home_routers';

const routes = [
    ...adm_routers,
    ...logins_routers,
    ...home_routers
];


const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;