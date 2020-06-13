<template>
  <div>
    {{this.$route.params.id}}
    <a-layout style="min-height:100%">
      <a-layout-content style="margin-top:30px;text-align:center">
        <a-layout>
          <a-layout-content>
            <a-page-header style="margin-left:0" title="返回上一页" @back="back" />
            <div style="margin:0 auto;max-width:1200px">
              <a-card style="margin:0 20px 0 20px;max-width:1200px;">
                <a-row>
                  <img style="text-align:left" :src="info.Book_src" height="500px" />
                </a-row>
                <a-row>
                  <h style="font-size:40px">{{info.Book_name}}</h>
                  <div style="font-size:18px">{{info.Book_writer}}</div>
                </a-row>
                <a-row>
                  <a-rate :value="parseInt(info.Book_score)/2" disabled allow-half />
                </a-row>
                <a-row>
                  <div style="font-size:32px">
                    <h1>{{info.Book_score.toFixed(1)}}</h1>
                  </div>
                </a-row>
                <a-row>
                  <div style="margin:0 50px 0 50px">{{info.Book_intro}}</div>
                </a-row>
              </a-card>
            </div>
          </a-layout-content>
        </a-layout>
        <a-page-header style="margin-left:10%;margin-top:30px" title="评论列表" sub-title="Comments" />
        <a-row type="flex" justify="space-around" align="middle">
          <a-col :span="24">
            <div>
              <a-avatar icon="user" />
              <a-avatar>
                <a-icon slot="icon" type="user" />
              </a-avatar>
              <a-avatar>U</a-avatar>
              <a-avatar>USER</a-avatar>
              <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
              <a-avatar style="color: #f56a00; backgroundColor: #fde3cf">U</a-avatar>
              <a-avatar style="backgroundColor:#87d068" icon="user" />
            </div>

            <!--以下是列表渲染部分-->
            <div style="margin:0 auto;max-width:1000px;text-align:center">
              <a-list
                class="comment-list"
                :header="`共有${comments.length}条评论`"
                item-layout="vertical"
                :data-source="comments"
                style="margin:20px;text-align:center"
              >
                <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                  <a-list-item-meta :description="item.Book_comment_content">
                    <a slot="title">
                      <b>{{item.Book_comment_title}}</b>
                    </a>
                    <a-avatar slot="avatar">{{item.User_name.substring(0,1)}}</a-avatar>
                  </a-list-item-meta>
                  <template slot="actions">
                    <span>作者：{{item.User_name}}</span>
                    <span>
                      <a-icon type="like-o" style="margin-left: 8px" />赞
                    </span>
                    <span>
                      <a-icon type="dislike-o" style="margin-left: 8px" />踩
                    </span>
                    <span>
                      <a-icon type="warning" style="margin-left: 8px" />举报
                    </span>
                    <a-tooltip :title="item.Create_time">
                      <span>{{ item.Create_time}}</span>
                    </a-tooltip>
                  </template>
                </a-list-item>
              </a-list>
            </div>

            <div style="margin:0 auto;max-width:1000px">
              <a-card title="发表评论" style="text-align:center;margin:24px">
                <div style="font-size:30px" v-if="commentRate">{{commentRate*2}}</div>评分：
                <a-rate v-model="commentRate" allow-half />
                <a-input v-model="commentTitle" placeholder="请输入标题" style="margin:14px 5px 0 5px;" />
                <a-textarea
                  v-model="commentValue"
                  placeholder="请输入评论内容"
                  :auto-size="{ minRows: 4, maxRows: 4 }"
                  style="margin:14px 5px 0 5px;"
                />
                <a-button style="margin:15px 5px 0 5px;" @click="comment" v-if="!iscomment">发表</a-button>
                <div style="font-size:30px" v-if="iscomment">您已经评论过了</div>
              </a-card>
            </div>
          </a-col>
        </a-row>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
import moment from "moment";
import global_ from "../../components/Global";
import Vue from "vue";
export default {
  data() {
    return {
      commentRate: 0,
      info: {},
      comments: {},
      iscomment: false,
      moment
    };
  },
  mounted: function() {
    console.log(this.$route.params.id);
    this.$http
      .get("http://182.92.57.178:5000/books/" + this.$route.params.id)
      .then(response => {
        this.info = response.data.result.info;
        this.comments = response.data.result.comments;
        console.log(this.info);
        console.log(this.comments.length);
      })
      .catch(response => {
        console.log(response);
      });
    global_.my_book_comments.forEach(element => {
      if (element.Book_id == this.$route.params.id) {
        this.iscomment = true;
      }
    });
  },
  methods: {
    back() {
      this.$router.push({ path: "/book/index" });
    },
    comment() {
      if (this.commentRate == 0) {
        alert("请打分");
        return;
      }
      Vue.axios
        .post(
          "http://182.92.57.178:5000/books/" +
            this.$route.params.id +
            "/comments",
          {
            book_comment_title: this.commentTitle,
            book_comment_content: this.commentValue
          },
          {
            headers: {
              token: global_.token
            }
          }
        )
        .then(response => {
          console.log(response);
          this.$http
            .get("http://182.92.57.178:5000/books/" + this.$route.params.id)
            .then(response => {
              this.info = response.data.result.info;
              this.comments = response.data.result.comments;
              console.log(this.info);
              console.log(this.comments.length);
            })
            .catch(response => {
              console.log(response);
            });
        })
        .catch(response => {
          console.log(response);
          alert("评论失败");
        });
      Vue.axios
        .post(
          "http://182.92.57.178:5000/books/" +
            this.$route.params.id +
            "/scores",
          {
            book_score: this.commentRate*2
          },
          {
            headers: {
              token: global_.token
            }
          }
        )
        .then(ans => {
          console.log(ans);
          alert("评论成功");
          this.iscomment = true;
          Vue.axios
            .get("http://182.92.57.178:5000/users/book_comments", {
              headers: { token: global_.token }
            })
            .then(function(res) {
              global_.my_book_comments = res.data.result;
            })
            .catch(function(error) {
              console.log(error);
            });
        })
        .catch(response => {
          console.log(response);
          alert("评分失败");
        });
    }
  }
};
</script>