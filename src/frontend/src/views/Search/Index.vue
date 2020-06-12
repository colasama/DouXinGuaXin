<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content style="margin-top:15%;margin-bottom:15%">
          <h1 style="font-size:40px">千度搜索</h1>
          
        <div style="text-align:center">
          <a-input-group compact style="height:100px;margin-top:14px">
            <a-select size="large" v-model="value" style="width:70px;height:50px;text-align:center">
              <a-select-option value="book">
                书籍
              </a-select-option>
              <a-select-option value="movie">
                影视
              </a-select-option>
              <a-select-option value="group">
                小组
              </a-select-option>
              <a-select-option value="topic">
                话题
              </a-select-option>
              <a-select-option value="topic_content">
                图文
              </a-select-option>
              <a-select-option value="group_content">
                帖子
              </a-select-option>
            </a-select>
            <a-input-search placeholder="搜索" style="width: 400px;" size="large" @search="onSearch" v-model="keywords"/>
          </a-input-group>
      </div>

      </a-layout-content>
    </a-layout>
  </div>
</template>
<script>
  export default{
    data() {
      return{
        value:"book",
        keywords:""
      }
    },
    methods:{
      onSearch(){
        this.$router.push({
          path: "/search/result/" + this.value + "/" + this.keywords
        })
      }
    }
  }
</script>
