<template>
  <div>
  <a-layout style="min-height:100%">
        <a-layout-content style="min-width:1200px;margin:0 auto;">
            <a-page-header
                style="margin-left:24px;margin-top:30px"
                title="话题"
                sub-title="Groups"
            />

            <div class="header">
                <div>
                    <h1 style="color:white;font-size:40px">#{{info.Topic_name}} </h1>
                    <div style="color:white;margin:24px">话题简介：{{info.Topic_intro}}</div>
                    <a-button style="text-align:center;border:1px" v-if="!ifJoinedTopic" type="default" @click="jointopic"><b>参与话题</b></a-button>
                    <a-button v-if="ifJoinedTopic" type="default"><b>发表图文</b></a-button>
                    <div style="margin-top:50px">
                      <span style="color:white;margin:24px"><a-icon type="profile" style="margin:5px"/>话题相关：{{info.Topic_related}}</span>
                    </div>
                </div>
            </div>

            <a-divider>
                <div style="font-size:18px">共有{{posts.length}}条图文</div>
            </a-divider>

            <!--帖子渲染部分-->
            <a-list
                class="comment-list"
                item-layout="vertical"
                :data-source="posts"
                style="margin:24px;text-align:center"
            >
            <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                <a-list-item-meta :description="item.Topic_content_content">
                    <a slot="title" :href="'/object/'+item.Topic_content_id">
                    {{item.Topic_content_title}}
                    </a>
                    <!--a-avatar slot="avatar" :src="item.avatar" /-->
                </a-list-item-meta>
                <template slot="actions" >
                    <span> <a-icon type="like-o" style="margin-left: 8px" /> 赞</span>
                    <span> <a-icon type="dislike-o" style="margin-left: 8px" /> 踩</span>
                    <span> <a-icon type="warning" style="margin-left: 8px" /> 举报</span>
                    <a-tooltip :title="item.Create_time"><span>{{ item.Create_time}}</span></a-tooltip>    
                </template>
            </a-list-item>
            </a-list>
            
        </a-layout-content>
    </a-layout>
  </div>
</template>
<style>
.header{
    height:400px;
    margin:24px;
    text-align:center;
    background:rgb(62, 47, 146);
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
<script>
import global_ from '../../components/Global'
export default {
  components:{
    
  },
  mounted:function(){
      this.id=this.$route.params.id;
      console.log(this.id);
      this.$http
      .get("http://182.92.57.178:5000/topics/" + this.$route.params.id)
      .then(response => {
        this.info = response.data.result.info;
        this.posts = response.data.result.contents;
        console.log(this.info);
      })
      .catch(response => {
        console.log(response);
      });
      global_.my_topics.forEach(element => {
      if (element.Topic_id == this.$route.params.id) {
        this.ifJoinedTopic = true;
      }
    });
  },
  data() {
    return {
        posts:[
            {"Group_content_id": 4, "Group_content_content": "testtesttest", "Group_content_title": "test", "Group_id":1, 
            "User_id": 15, "Username":"test","Group_content_image": "/example", "Create_time": "2020-06-03 17:50:52", "Is_highlighted": 1, "Is_pinned": 1}, 
            {"Group_content_id": 5, "Group_content_content": "testtesttest123", "Group_content_title": "test123", "Group_id": 1, 
            "User_id": 15,  "Username":"test","Group_content_image": "/example", "Create_time": "2020-06-03 18:30:04", "Is_highlighted": 1, "Is_pinned": 1}
        ],
        info:[],
        ifJoinedTopic:false,
    };
  },
  methods: {
    //估计得有一个getUsernameByID一个getPosts
  }
};
</script>