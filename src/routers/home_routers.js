
export default [
    //Rota padrao
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/Home.vue')
    },
    //Rota detalhe do produto
    { 
        path: '/produto/:id',
        name: 'ProdutoDetalhe',
        component: () => import('../views/ProdutoDetalhe.vue')
    }
]