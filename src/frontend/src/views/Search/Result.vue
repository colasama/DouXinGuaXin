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
            <a-select size="large" v-model="kind" style="width:70px;height:50px;text-align:center" @change="handleChange">
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
          <div style="max-width:1000px;min-width:1000px;margin:0 auto">
          <a-card style="width:100%;text-align:left">
            <a :href="'/#/'+ kind.substr(0,5) + '/' + object + '/' + item.cid">
          <a-list-item-meta
            :description="item.des||item.content"
          >
            <img
                    height="120px"
                    slot="avatar"
                    v-if="kind =='book'||kind =='movie'||kind =='topic_content'"
                    :src="item.img"
            />
            <a slot="title" :href="'/#/'+ kind.substr(0,5) + '/' + object + '/' + item.id">
              <b style="font-size:20px">{{ item.title }}</b>
            </a>
          </a-list-item-meta>
            <b>{{item.time}}</b>
            </a>
          </a-card>
          </div>
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
        object: "",
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
        if(this.kind == 'movie'||this.kind == 'book')
          this.object = 'object'
        else{
          this.object = this.kind.substr(0,5)
          console.log("New:"+this.object)
        }
        this.results = res.data.result
        this.show()
      }).catch(function(error){
        console.log(error);
      })
    },
    methods:{
      handleChange(value){
        if(value == 'movie'||value == 'book')
          this.object = 'object'
        else{
          this.object = value.substr(0,5)
          console.log("New:"+this.object)
        }
      },
      show(){
        console.log("Show:"+this.kind)
        var name = this.kind[0].toUpperCase() + this.kind.substr(1,this.kind.length)
        for(var i=0;i<this.results.length;i++){
          var id = this.results[i][name + "_id"]
          var cid = id
          if(this.kind=='topic_content'||this.kind=='group_content')
            cid = this.results[i][name.substr(0,5) +"_id"]
          console.log("cid:"+cid)
          var title = this.results[i][name + "_name"]
          var des = this.results[i][name + "_intro"]
          var img = this.results[i][name + "_src"]
          if(img == null || img == undefined){
            img = this.results[i][name + "_image"]
            if(img != null && img != undefined)
              img = this.results[i][name + "_image"].split(',')[0]
          }
          if(title == null || title == undefined)
            title = this.results[i][name + "_title"]
          var time = this.results[i]["Create_time"]
          var content = this.results[i][name + "_content"]
          if(img == 'None') img = 'https://i.loli.net/2020/06/14/5OyIpPzjRFB1Xos.png'
          this.data.push({"id":id, "title":title, "des":des, "img":img, "content":content, "time":time, "cid":cid})
          console.log("Show() finished.")
        }
        console.log(this.data)
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