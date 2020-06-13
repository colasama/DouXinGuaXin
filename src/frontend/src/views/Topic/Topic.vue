<template>
  <div>
    <a-layout style="min-height:100%">
      <a-layout-content style="min-width:1200px;margin:0 auto;">
        <a-page-header style="margin-left:24px;margin-top:30px" title="话题" sub-title="Groups" />

        <div class="header">
          <div>
            <h1 style="color:white;font-size:40px">#{{info.Topic_name}}</h1>
            <div style="color:white;margin:24px">话题简介：{{info.Topic_intro}}</div>
            <a-button
              style="text-align:center;border:1px"
              v-if="!ifJoinedTopic"
              type="default"
              @click="jointopic"
            >
              <b>参与话题</b>
            </a-button>
            <a-button v-if="ifJoinedTopic" type="default" @click="showPost">
              <b>发表图文</b>
            </a-button>
            <div style="margin-top:50px">
              <span style="color:white;margin:24px">
                <a-icon type="profile" style="margin:5px" />
                话题相关：{{info.Topic_related}}
              </span>
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
            <a-textarea
              style="margin-top:10px"
              v-model="topic_content_content"
              placeholder="请填写图文内容，图片可以点击下方上传按钮上传哦~"
              :auto-size="{ minRows: 5, maxRows: 5 }"
            ></a-textarea>
            <div style="margin-top:10px">
              <a-upload
                action="http://182.92.57.178:5000/pictures/add"
                method="post"
                list-type="picture-card"
                :file-list="fileList"
                :before-upload="beforeUpload"
                @preview="handlePreview"
                @change="handleChange"
              >
                <div v-if="fileList.length < 3">
                  <!--最大上传三张图片-->
                  <a-icon type="plus" />
                  <div class="ant-upload-text">上传图片</div>
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

        <a-modal :visible="previewVisible" :footer="null" @cancel="handleUCancel">
          <img alt="example" style="width: 100%" :src="previewImage" />
        </a-modal>

        <!--帖子渲染部分-->
        <a-list
          class="comment-list"
          item-layout="vertical"
          :data-source="posts"
          style="margin:24px;text-align:center"
        >
          <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
            <img
              v-for="pic in item.Topic_content_image"
              :key="pic"
              slot="extra"
              width="272"
              alt="logo"
              style="cursor: pointer;"
              :src="pic"
              @click="handlePreviewForNormalUse(pic)"
            />
            <a-list-item-meta :description="item.Topic_content_content">
              <a-avatar slot="avatar">{{item.User_name.substring(0,1)}}</a-avatar>
              <a slot="title" :href="'/object/'+item.Topic_content_id">{{item.Topic_content_title}}</a>
              <!--a-avatar slot="avatar" :src="item.avatar" /-->
            </a-list-item-meta>
            <template slot="actions">
              <span>
                <a-icon type="user" style="margin-left: 8px" />
                {{item.User_name}}
              </span>
              <a-tooltip :title="item.Create_time">
                <span>{{ item.Create_time}}</span>
              </a-tooltip>
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
  background: rgb(62, 47, 146);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
<script>
import global_ from "../../components/Global";
import Vue from "vue";
function getBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
  });
}

export default {
  components: {},
  mounted: function() {
    this.id = this.$route.params.id;
    console.log(this.id);
    this.load_data();
  },
  data() {
    return {
      posts: [],
      info: [],
      postVisible: false,
      ifJoinedTopic: false,
      previewVisible: false,
      previewImage: "",
      fileList: [],
      topic_content_content: "",
      pics: []
    };
  },
  methods: {
    load_data() {
      this.$http
        .get("http://182.92.57.178:5000/topics/" + this.$route.params.id)
        .then(response => {
          this.info = response.data.result.info;
          this.posts = response.data.result.contents;
          for (let index = 0; index < this.posts.length; index++) {
            console.log(this.posts[index].Topic_content_image);
            if (this.posts[index].Topic_content_image == "None") {
              this.posts[index].Topic_content_image = [];
            } else {
              var images_src = this.posts[index].Topic_content_image.split(",");
              this.posts[index].Topic_content_image = images_src;
            }
          }
          console.log(this.info);
          console.log(this.posts);
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
    jointopic() {
      if (global_.loginStatus == false) {
        alert("请先登录");
        return;
      }
      console.log(global_.token);
      Vue.axios
        .post(
          "http://182.92.57.178:5000/topics/" + this.id + "/join",
          {},
          {
            headers: {
              token: global_.token
            }
          }
        )
        .then(res => {
          console.log(res);
          this.ifJoinedTopic = true;
          global_.my_topics.push({
            Group_id: res.data.result.Topic_id,
            User_id: res.data.result.User_id
          });
        })
        .catch(res => {
          console.log(res);
        });
    },
    showPost() {
      this.postVisible = true;
    },
    beforeUpload() {},
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
      console.log(file);
    },
    handlePreviewForNormalUse(src) {
      this.previewImage = src;
      this.previewVisible = true;
    },
    //这几个是发表图文的函数
    handleChange(info) {
      let fileList = [...info.fileList];
      fileList = fileList.map(file => {
        if (file.response) {
          file.url = file.response.url;
        }
        return file;
      });
      this.fileList = fileList;
    },
    showReport() {
      this.postVisible = true;
    },
    handleOk(e) {
      console.log(e);
      var src = "None";
      if (this.fileList.length > 0) {
        src = "";
        for (let index = 0; index < this.fileList.length - 1; index++) {
          const element = this.fileList[index].url;
          src += element + ",";
        }
        src += this.fileList[this.fileList.length - 1].url;
      }
      Vue.axios
        .post(
          "http://182.92.57.178:5000/topics/" + this.id + "/add_content",
          {
            topic_content_content: this.topic_content_content,
            topic_content_image: src
          },
          {
            headers: {
              token: global_.token
            }
          }
        )
        .then(res => {
          console.log(res);
          this.postVisible = false;
          this.load_data();
          this.showSuccess();
        })
        .catch(res => {
          console.log(res);
        });
    },
    handleCancel() {
      this.postVisible = false;
    },
    destroyALL() {
      this.$destroyAll();
    },
    showSuccess() {
      this.$success({
        centered: true,
        title: "发表成功",
        content: "成功发表图文！", //<a-result status="success" title=""/>,
        onOK() {
          this.destroyALL();
        }
      });
    }
  }
};
</script>