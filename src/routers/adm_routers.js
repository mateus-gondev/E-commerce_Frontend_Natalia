export default [
        {
    path: '/adm',
    component: () => import('@/views/AdmPage/AdmHome.vue'),
        children: [
            {
            path: '',
            name: 'AdmPedidos', 
            component: () => import('@/components/Adm/AdmPedidos.vue')
            },
            {
            path: 'produtos',
            name: 'AdmProdutos',
            component: () => import('@/views/AdmPage/AdmProdutos.vue')
            },
            {
            path: 'produto/novo',
            name: 'AdmFormProduto',
            component: () => import('@/views/AdmPage/Forms/AdmFormProduto.vue')
            },
            {
            path: 'usuario',
            name: 'AdmUsuario',
            component: () => import('@/views/AdmPage/AdmUsuario.vue')
            },
            {
            path: 'usuario/novo',
            name: 'AdmForm',
            component: () => import('@/views/AdmPage/Forms/AdmForm.vue')
            }
            
        ]
    }
];
