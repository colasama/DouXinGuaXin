<template>
    <div style="text-align:center">
        <a-select v-model="value" style="width: 70px">
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
        <a-input-search placeholder="搜索" style="width: 200px" @search="onSearch" v-model="keywords"/>
    </div>
</template>
<script>
    import Vue from "vue";
    export default{
        data() {
            return{
                value:"book",
                keywords:""
            }
        },
        methods:{
            onSearch(){
                Vue.axios.get('http://182.92.57.178:5000/search/' + this.value + 's', {
                    params:{keywords:this.keywords}
                }).then(res=>{
                    console.log(res)    //后续处理
                }).catch(function(error){
                    console.log(error);
                })
                console.log(this.value) //可删
            }
        }
    }
</script>