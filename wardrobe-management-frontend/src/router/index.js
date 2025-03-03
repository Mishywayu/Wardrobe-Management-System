import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/Auth/Login.vue'
import Register from '@/components/Auth/Register.vue'


const routes = [
  { path: "/", redirect: "/register" }, //redirect to register by default
  { path: "/login", component: Login },
  { path: "/register", component: Register },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
