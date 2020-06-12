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