import { createRouter, createWebHistory} from "vue-router";
// import App from '../App.vue'
import AppLayout from '../components/AppLayout.vue';
import Login from '@/views/LoginView';

const routes = [
    {
        path: '/',
        name: 'home',
        component: AppLayout,
        children: [
            { path: '/', component:()=>import('@/components/NavBar.vue') },
            { path: '/MovieSearch/:id?', name: 'search', component:()=>import('@/components/MovieSearch.vue') },
            { path: '/movies/:id', component:()=>import('@/components/MovieDetailPage.vue')},
            { path: '/Test', component:()=>import('@/components/FunctionTest.vue')},
            { path: '/personal/:id', name: 'personal', component: () => import('@/views/PersonalView')},
            { path: '/rank', component: () => import('@/views/RankView.vue')},
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    // {
    //     path: '/personal/:id',
    //     name: 'personal',
    //     component: () => import('@/views/PersonalView')
    // },
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router