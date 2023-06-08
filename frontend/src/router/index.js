import { createRouter, createWebHistory} from "vue-router";
// import App from '../App.vue'
import AppLayout from '../components/AppLayout.vue'
const routes = [
    {
        path: '/',
        name: 'home',
        component: AppLayout,
        children: [
            { path: '/', component:()=>import('@/components/NavBar.vue') },
            { path: '/MovieSearch', component:()=>import('@/components/MovieSearch.vue') },
            { path: '/movies/:id', component:()=>import('@/components/MovieDetailPage.vue')},
        ]
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router