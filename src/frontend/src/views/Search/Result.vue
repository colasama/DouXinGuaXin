<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content style="margin-top:25px">
        <a-page-header
          style="text-align:center"
          title="搜索结果"
          sub-title="Result"
          @back="() => this.$router.go(-1)"
        />
        
        <div style="text-align:center">
          <a-input-group compact style="height:100px;margin-top:14px">
            <a-select size="large" v-model="kind" style="width:70px;height:50px;text-align:center">
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
            <a-input-search placeholder="搜索" style="width: 400px;" size="large" @search="refresh" v-model="keywords"/>
          </a-input-group>
      </div>
      
      <a-list item-layout="horizontal" :data-source="data">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-card style="width:100%">
          <a-list-item-meta
            :description="item.des"
          >
            <a slot="title" :href="'/#/'+ kind + '/object/' + item.id">{{ item.title }}</a>
            <img
              width="60px"
              slot="avatar"
              :src="item.img"
            />
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
        this.results = res.data.result
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
          var img = this.results[i][name + "_src"]
          this.data.push({"id":id,"title":title,"des":des,"img":img})
        }
      },
      refresh(){
        this.data.splice(0,this.data.length)
        this.$http.get('http://182.92.57.178:5000/search/' + this.kind + 's', {
          params:{keywords:this.keywords}
        }).then(res=>{
          console.log(res)
          console.log(this.kind)
          this.results = res.data.result
          this.show()
        }).catch(function(error){
          console.log(error);
        })
      }
    },
  }
</script>