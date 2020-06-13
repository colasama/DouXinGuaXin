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

            <!--发帖框，由postVisible控制-->
            <a-modal  
                centered="true"
                title="发表图文"
                :visible="postVisible"
                :confirm-loading="confirmLoading"
                @ok="handleOk"
                @cancel="handleCancel"
                okText="发表"
                cancelText="取消"
                >
                <div>
                        <a-input style="margin-top:10px" placeholder="请填写图文标题" />
                        <a-textarea style="margin-top:10px" placeholder="请填写图文内容，图片可以点击下方上传按钮上传哦~" :auto-size="{ minRows: 5, maxRows: 5 }"></a-textarea>
                        <div style="margin-top:10px">
                          <a-upload
                            action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                            list-type="picture-card"
                            :file-list="fileList"
                            @preview="handlePreview"
                            @change="handleChange"
                          >
                            <div v-if="fileList.length < 3"><!--最大上传三张图片-->
                              <a-icon type="plus" />
                              <div class="ant-upload-text">
                                上传图片
                              </div>
                            </div>
                          </a-upload>
                          <a-modal :visible="previewVisible" :footer="null" @cancel="handleUCancel">
                            <img alt="example" style="width: 100%" :src="previewImage" />
                          </a-modal>
                        </div>
                </div>
            </a-modal>

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
                  <a-avatar slot="avatar">{{item.User_name.substring(0,1)}}</a-avatar>
                    <a slot="title" :href="'/object/'+item.Topic_content_id">
                    {{item.Topic_content_title}}
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
import Vue from 'vue'

function getBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
  });
}

export default {
  components:{
    
  },
  created:function(){
      this.id=this.$route.params.id;
      console.log(this.id);
      this.$http
      .get("http://182.92.57.178:5000/topics/" + this.$route.params.id)
      .then(response => {
        this.info = response.data.result.info;
        console.log(this.info);
      })
      .catch(response => {
        console.log(response);
      });
      Vue.axios.post(//判断是否加入了小组？不知道可不可行
          'http://182.92.57.178:5000/topics/'+this.id+'/join',
          {
          },
          {
            headers:{
              'token':global_.token
            }
          }
        ).then((res)=>{
        console.log(res)
      }).catch((res)=>{
        this.ifJoinedTopic=true
        console.log(res)
      })
  },
  data() {
    return {
        posts:[
            {"Topic_content_id": 4, "Topic_content_content": "testtesttest", "Topic_content_title": "test", "Topic_id":1, 
            "User_id": 15, "Username":"test","Topic_content_image": "/example", "Create_time": "2020-06-03 17:50:52", "Is_highlighted": 1, "Is_pinned": 1}, 
            {"Topic_content_id": 5, "Topic_content_content": "testtesttest123", "Topic_content_title": "test123", "Topic_id": 1, 
            "User_id": 15,  "Username":"test","Topic_content_image": "/example", "Create_time": "2020-06-03 18:30:04", "Is_highlighted": 1, "Is_pinned": 1}
        ],
        info:[],
        postVisible:true,
        ifJoinedTopic:false,
        previewVisible: false,
        previewImage: '',
        fileList: [
        {
          uid: '-1',
          name: 'image.png',
          status: 'done',
          url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
        },],
    };
  },
  methods: {
    //估计得有一个getUsernameByID一个getPosts
    //这几个是上传部分的函数
    handleUCancel() {
      this.previewVisible = false;
    },
    async handlePreview(file) {
      if (!file.url && !file.preview) {
        file.preview = await getBase64(file.originFileObj);
      }
      this.previewImage = file.url || file.preview;
      this.previewVisible = true;
    },
    //这几个是发表图文的函数
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
                    content: "成功发表图文！",//<a-result status="success" title=""/>,
                    onOK(){
                        this.destroyALL();
                    }
                })
    },
  },
};
</script>