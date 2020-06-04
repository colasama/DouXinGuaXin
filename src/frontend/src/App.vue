<template>
  <div id="app">
    <AppHeader></AppHeader>
    <router-view style="text-align: center;margin-top:4px;"/>
    <AppFooter></AppFooter>
  </div>
</template>

<style>
html,body,#app{
  height: 100%;
  width: 100%;
  margin: 0;
}
</style>


<script>
import AppHeader from './components/Header.vue';
import AppFooter from './components/Footer.vue';
export default {
  components:{
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      
    };
  },
  created: function(){
    document.title = this.$route.meta.title || this.$route.meta.pathName
  },
  watch:{
    $route(){
      document.title = this.$route.meta.title || this.$route.meta.pathName
    }
  },
  methods: {
  }
};
</script>