import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    meta:{title: '豆辛瓜辛 - 一个书籍影视交流平台',},
    component: Home
  },
  {
    path: '/book/index',
    name: 'Book',
    meta:{title: '书籍 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Book/Index.vue')
  },
  {
    path: '/movie/index',
    name: 'Movie',
    meta:{title: '电影 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Movie/Index.vue')
  },
  {
    path: '/topic/index',
    name: 'Topic',
    meta:{title: '话题 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Topic/Index.vue')
  },
  {
    path: '/group/index',
    name: 'Group',
    meta:{title: '小组 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Group/Index.vue')
  },
  {
    path: '/register',
    name: 'Register',
    meta:{title: '注册 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Register.vue')
  },
  {
    path: '/login',
    name: 'Login',
    meta:{title: '登录 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Login.vue')
  },
  {
    path: '/admin',
    name: 'Admin',
    meta:{title: '后台管理 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Admin.vue')
  },
  {
    path: '/book/object/:id',
    name: 'Object',
    meta:{title: '书籍 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Book/Object.vue')
  },
  {
    path: '/search/index',
    name: 'Search',
    meta:{title: '搜索 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Search/Index.vue')
  },
  {
    path: '/search/result/',
    name: 'SearchResult',
    meta:{title: '搜索结果 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/Search/Result.vue')
  },
  {
    path: '/user/index',
    name: 'User',
    meta:{title: '个人主页 - 豆辛瓜辛 - 一个书籍影视交流平台',},
    component: () => import('../views/User/Index.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
