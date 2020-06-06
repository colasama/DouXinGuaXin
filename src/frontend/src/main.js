import Vue from 'vue'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.less'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

//Vue.prototype.axios = axios
Vue.config.productionTip = false

Vue.use(Antd);

new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  router,
  render: h => h(App)
}).$mount('#app')

/*import Vuex from 'vuex'
Vue.use(Vuex)
const state={
  token:"",
  User:""
}

const mutations={
  settoken(state,token){
    state.token=token;
  },
  setuser(state,user){
    state.user=user
  }
}

export default new Vuex.Store({
  state,
  mutations,
})*/

