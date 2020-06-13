<template>
  <div>
    <a-layout style="min-height:100%">
      <a-layout-content style="min-width:1200px;margin:0 auto;">
        <a-page-header style="margin-left:24px;margin-top:30px" title="小组" sub-title="Groups" />

        <div class="header">
          <div>
            <h1 style="color:white;font-size:40px">#{{info.Group_name}}</h1>
            <div style="color:white;margin:24px">小组简介：{{info.Group_intro}}</div>
            <a-button
              style="text-align:center;border:1px"
              v-if="!ifJoinedGroup||!ifLoggedIn"
              type="default"
              @click="joingroup"
            >
              <b>加入小组</b>
            </a-button>
            <a-button v-if="ifJoinedGroup&&ifLoggedIn" type="default">
              <b>发表帖子</b>
            </a-button>
            <div style="margin-top:50px">
              <span style="color:white;margin:24px">
                <a-icon type="profile" style="margin:5px" />
                小组相关：{{info.Group_related}}
              </span>
              <span style="color:white;margin:24px">
                <a-icon type="user" />
                管理员ID：{{info.User_id}}
              </span>
            </div>
          </div>
        </div>

        <!--发帖框，由postVisible控制-->
            <a-modal  
                centered="true"
                title="发表帖子"
                :visible="postVisible"
                :confirm-loading="confirmLoading"
                @ok="handleOk"
                @cancel="handleCancel"
                okText="发表"
                cancelText="取消"
                >
                <div>
                        <a-input style="margin-top:10px" placeholder="请填写帖子标题" />
                        <a-textarea style="margin-top:10px" placeholder="请填写帖子内容，要大于25字哦~" :auto-size="{ minRows: 5, maxRows: 5 }"></a-textarea>
                        <!--a-button style="margin-top:10px">提交</a-button-->
                </div>
            </a-modal>

            <a-divider>
                <div style="font-size:18px">共有{{posts.length}}条帖子</div>
            </a-divider>

        <!--帖子渲染部分-->
        <a-list
                class="comment-list"
                item-layout="vertical"
                :data-source="posts"
                style="margin:24px;text-align:center"
            >
            <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                <a-list-item-meta :description="item.Group_content_content">
                  <a-avatar slot="avatar">{{item.User_name.substring(0,1)}}</a-avatar>
                    <a slot="title" :href="'/object/'+item.Group_content_id">
                    {{item.Group_content_title}}
                    <a-tag style="margin-left:8px" color="red">精华</a-tag>
                    <a-tag style="margin-left:8px" color="orange">置顶</a-tag>
                    </a>
                    <!--a-avatar slot="avatar" :src="item.avatar" /-->
                </a-list-item-meta>
                <template slot="actions" >
                    <span> <a-icon type="user" style="margin-left: 8px" /> {{item.User_name}}</span>
                    <a-tooltip :title="item.Create_time"><span>{{ item.Create_time}}</span></a-tooltip>    
                </template>
            </a-list-item>
            </a-list>
      </a-layout-content>
    </a-layout>
  </div>
</template>
<style>
.header {
  height: 400px;
  margin: 24px;
  text-align: center;
  background: rgb(47, 146, 116);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
<script>
import global_ from "../../components/Global";
import Vue from "vue";
export default {
  components: {},
  data() {
    return {
      posts: [
        {
          Group_content_id: 4,
          Group_content_content: "testtesttest",
          Group_content_title: "test",
          Group_id: 1,
          User_id: 15,
          Username: "test",
          Group_content_image: "/example",
          Create_time: "2020-06-03 17:50:52",
          Is_highlighted: 1,
          Is_pinned: 1
        },
        {
          Group_content_id: 5,
          Group_content_content: "testtesttest123",
          Group_content_title: "test123",
          Group_id: 1,
          User_id: 15,
          Username: "test",
          Group_content_image: "/example",
          Create_time: "2020-06-03 18:30:04",
          Is_highlighted: 1,
          Is_pinned: 1
        }
      ],
      postVisible:true,
      ifJoinedGroup:false,
      ifLoggedIn:false,
      id:-1,
      info:[],
    };
  },
  mounted: function() {
    this.ifLoggedIn = global_.loginStatus;
    this.id = this.$route.params.id;
    console.log(this.id);
    this.$http
      .get("http://182.92.57.178:5000/groups/" + this.$route.params.id)
      .then(response => {
        this.info = response.data.result.info;
        this.posts = response.data.result.contents;
        console.log(this.info);
      })
      .catch(response => {
        console.log(response);
      });
    global_.my_groups.forEach(element => {
      if (element.Group_id == this.$route.params.id) {
        this.ifJoinedGroup = true;
      }
    });
  },
  methods: {
    //估计得有一个getUsernameByID一个getPosts
    joingroup() {
      if (global_.loginStatus == false) {
        alert("请先登录");
        return;
      }
      console.log(global_.token);
      Vue.axios
        .post(
          "http://182.92.57.178:5000/groups/" + this.id + "/join",
          {},
          {
            headers: {
              token: global_.token
            }
          }
        )
        .then(res => {
          console.log(res);
          this.ifJoinedGroup = true;
          global_.my_groups.push({
            Group_id: res.data.result.Group_id,
            User_id: res.data.result.User_id
          });
        })
        .catch(res => {
          console.log(res);
        });
    },
    //发表帖子的函数们
    handleChange({ fileList }) {
      this.fileList = fileList;
    },
    showReport(){
      this.postVisible=true;
      },
    handleOk(e){
      console.log(e);
      this.postVisible=false;
      this.showSuccess();
    },
    handleCancel(){
                this.postVisible=false;
            },
    destroyALL(){
                this.$destroyAll();
            },
    showSuccess(){
                this.$success({
                    centered: true,
                    title: '发表成功',
                    content: "成功发表帖子！",//<a-result status="success" title=""/>,
                    onOK(){
                        this.destroyALL();
                    }
                })
    },
  }
};
</script>