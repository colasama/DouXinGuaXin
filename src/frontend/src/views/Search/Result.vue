<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content style="margin-top:25px">
        <a-page-header
          style="text-align:center"
          title="搜索结果"
        />
        <a-select style="width: 70px;height: 40px;" v-model="kind">
          <a-select-option value="book">
            书籍
          </a-select-option>
          <a-select-option value="movie">
            影视
          </a-select-option>
          <a-select-option value="posts">
            帖子
          </a-select-option>
          <a-select-option value="topic">
            图文
          </a-select-option>
        </a-select>
        <a-input-search placeholder="书籍搜索" style="width: 400px;height:40px;" @search="refresh" v-model="keywords"/>
      
      <a-list item-layout="horizontal" :data-source="data">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-card style="width:100%">
          <a-list-item-meta
            :description="item.des"
          >
            <a slot="title" :href="'/#/'+ kind + '/object/' + item.id">{{ item.title }}</a>
            <!--a-avatar
              slot="avatar"
              src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
            /-->
          </a-list-item-meta>
          </a-card>
        </a-list-item>
        
      </a-list>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
  export default{
  data() {
      return {
        kind: this.$route.params.kind,
        keywords: this.$route.params.keywords,
        results: [],
        data:[]
      };
    },
    mounted() {
      this.$http.get('http://182.92.57.178:5000/search/' + this.kind + 's', {
        params:{keywords:this.keywords}
      }).then(res=>{
        console.log(res)
        console.log(this.kind)
        this.results = res["data"]["result"]
        this.show()
      }).catch(function(error){
        console.log(error);
      })
    },
    methods:{
      show(){
        var name = this.kind[0].toUpperCase() + this.kind.substr(1,this.kind.length)
        for(var i=0;i<this.results.length;i++){
          var id = this.results[i][name + "_id"]
          var title = this.results[i][name + "_name"]
          var des = this.results[i][name + "_intro"]
          this.data.push({"id":id,"title":title,"des":des})
        }
      },
      refresh(){
        this.data.length = 0
        this.$http.get('http://182.92.57.178:5000/search/' + this.kind + 's', {
          params:{keywords:this.keywords}
        }).then(res=>{
          console.log(res)
          console.log(this.kind)
          this.results = res["data"]["result"]
          this.show()
        }).catch(function(error){
          console.log(error);
        })
      }
    },
  }
</script>