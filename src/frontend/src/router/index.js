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
    path: '/book/index',
    name: 'Book',
    component: () => import('../views/Book/Index.vue')
  },
  {
    path: '/movie/index',
    name: 'Movie',
    component: () => import('../views/Movie/Index.vue')
  },
  {
    path: '/topic/index',
    name: 'Topic',
    component: () => import('../views/Topic/Index.vue')
  },
  {
    path: '/group/index',
    name: 'Group',
    component: () => import('../views/Group/Index.vue')
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
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/Admin.vue')
  },
  {
    path: '/book/book',
    name: 'Book',
    component: () => import('../views/Book/Book.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
