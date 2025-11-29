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
            path: 'usuario',
            name: 'AdmUsuario',
            component: () => import('@/views/AdmPage/AdmUsuario.vue')
            },
            {
            path: 'usuario/novo',
            name: 'AdmForm',
            component: () => import('@/views/AdmPage/AdmForm.vue')
            }
        ]
    }
];
