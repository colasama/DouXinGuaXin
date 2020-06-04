<template>
  <div>
    <AppHeader></AppHeader>
    <router-view style="text-align: center;margin-top:4px;"/>
    <AppFooter></AppFooter>
  </div>
</template>

<style>

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