import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/book',
    name: 'Book',
    component: () => import('../views/Book.vue')
  },
  {
    path: '/movie',
    name: 'Movie',
    component: () => import('../views/Movie.vue')
  },
  {
    path: '/topic',
    name: 'Topic',
    component: () => import('../views/Topic.vue')
  },
  {
    path: '/group',
    name: 'Group',
    component: () => import('../views/Group.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
