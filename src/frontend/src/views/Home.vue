<template>
  <div class="home">
    
    <a-layout style="min-height:100%">
      <a-layout-content>
      <a-carousel :after-change="onChange" autoplay arrows>
        <div
          slot="prevArrow"
          class="custom-slick-arrow"
          style="left: 20px;zIndex: 1"
        >
          <a-icon type="left-circle" />
        </div>
        <div slot="nextArrow"  class="custom-slick-arrow" style="right: 20px">
          <a-icon type="right-circle" />
        </div>
          <div><img :src="head[0]" style="width:100%" /></div>
          <div><img :src="head[1]" style="width:100%" /></div>
          <div><img :src="head[2]" style="width:100%" /></div>
          <div><img :src="head[3]" style="width:100%" /></div>
        </a-carousel>
        <a-tabs style="text-align: center" default-active-key="1" @change="callback">
          <a-tab-pane key="1" tab="书籍">
            <a-page-header
              style="margin-left:25%"
              title="热点书籍"
              sub-title="24小时内最热书籍"
            />
            <!--这里是书籍内容-->
            <div style="padding: 20px;margin: auto;">
              <a-row type="flex" justify="center" align="top">
                <a-col :span="4"/>

                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/book/object/'+books[0].Book_id">
                    <img
                      width="180px"
                      slot="cover"
                      alt="example"
                      :src="books[0].Book_src"
                    /></a>
                    <a-card-meta :title="books[0].Book_name" style="margin-top:10px">
                      <template slot="description">
                        {{books[0].Book_intro.substr(0,35)}}...
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>

                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/book/object/'+books[1].Book_id">
                      <img
                        width="180px"
                        slot="cover"
                        alt="example"
                        :src="books[1].Book_src"
                      /></a>
                    <a-card-meta :title="books[1].Book_name"  style="margin-top:10px">
                      <template slot="description">
                        {{books[1].Book_intro.substr(0,35)}}...
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>
                
                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/book/object/'+books[2].Book_id">
                      <img
                        width="180px"
                        slot="cover"
                        alt="example"
                        :src="books[2].Book_src"
                      /></a>
                    <a-card-meta :title="books[2].Book_name" style="margin-top:10px">
                      <template slot="description">
                        {{books[2].Book_intro.substr(0,35)}}...
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

              <a-col :span="4"/>
              </a-row>
            </div>
          </a-tab-pane>
          <a-tab-pane key="2" tab="影视">
            <!--这里是影视-->
            <a-page-header
              style="margin-left:25%"
              title="热点影视"
              sub-title="24小时内最热影视"
            />
             <!--这里是书籍内容-->
            <div style="padding: 20px;margin: auto;">
              <a-row type="flex" justify="center" align="top">
                <a-col :span="4"/>

                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/movie/object/'+movies[0].Movie_id">
                      <img
                        width="180px"
                        slot="cover"
                        alt="example"
                        :src="movies[0].Movie_src"
                      /></a>
                    <a-card-meta :title="movies[0].Movie_name" style="margin-top:10px">
                      <template slot="description">
                        {{movies[0].Movie_intro.substr(0,35)}}...
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>

                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/movie/object/'+movies[1].Movie_id">
                      <img
                        width="180px"
                        slot="cover"
                        alt="example"
                        :src="movies[1].Movie_src"
                      /></a>
                    <a-card-meta :title="movies[1].Movie_name" style="margin-top:10px">
                      <template slot="description">
                        {{movies[1].Movie_intro.substr(0,35)}}...
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>
                
                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/movie/object/'+movies[2].Movie_id">
                      <img
                        width="180px"
                        slot="cover"
                        alt="example"
                        style="margin:0 auto;text-align:center"
                        :src="movies[2].Movie_src"
                      /></a>
                    <a-card-meta :title="movies[2].Movie_name" style="margin-top:10px">
                      <template slot="description">
                        {{movies[2].Movie_intro.substr(0,35)}}...
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

              <a-col :span="4"/>
              </a-row>
            </div>
          </a-tab-pane>
        </a-tabs>

        <div>
          <a-row>
            <a-col :span="3" />

            <a-col :span="12">
              <a-page-header
                style="margin-left:24px"
                title="今日神评"
              />
              <!--帖子渲染部分-->
              <a-list
                  class="comment-list"
                  item-layout="vertical"
                  :data-source="posts"
                  style="margin:24px;text-align:center"
              >
              <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                  <a-list-item-meta :description="item.content">
                      <a slot="title" :href="'/object/'+item.id">
                      {{item.title}}
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
            </a-col>

            <a-col :span="1">
              <a-divider type="vertical"></a-divider>
            </a-col>
            <a-col :span="5" style="text-align:left">
              <a-page-header
                style="margin-left:0px"
                title="热门话题"
              />
              <a-list
                  item-layout="vertical"
                  :data-source="topics"
              >
              <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                  <a-card>
                    <div style="color:rgb(170, 46, 24);"><a :href="'/#/topic/topic/'+ item.Topic_id">
                      <b style="color:red">#{{item.Topic_name}}</b>
                    </a></div>
                  </a-card>
              </a-list-item>
              </a-list>
            </a-col>

            <a-col :span="3"/>
          </a-row>
        </div>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
// @ is an alias to /src

import global_ from '../components/Global'
export default {
  components: {

  },
  data(){
    return{
      head:[
        "https://i.loli.net/2020/06/13/mZMXQlvjiAEuVcz.jpg",
        "https://i.loli.net/2020/06/13/VxiAKgYeRTJzcau.jpg",
        "https://i.loli.net/2020/06/13/vMjOu8w1USeiy9Q.jpg",
        "https://i.loli.net/2020/06/13/a9iUSQFYjs56H1o.jpg",
      ],
      posts: [],
      books: [],
      movies: [],
      bookcomments: [],
      moviecomments: [],
      topics: []
    }
  },
  created:function(){
    console.log(global_.username);
  },
  mounted() {
    this.$http.get('http://182.92.57.178:5000/books').then(res=>{
      console.log(res)
      this.books = res.data.result
      this.showBook()
    }).catch(function(error){
      console.log(error);
    })
    this.$http.get('http://182.92.57.178:5000/movies').then(res=>{
      console.log(res)
      this.movies = res.data.result
      this.showMovie()
    }).catch(function(error){
      console.log(error);
    })
    this.$http.get('http://182.92.57.178:5000/all_comments').then(res=>{
      console.log(res)
      this.bookcomments = res.data.result.book_comments
      this.moviecomments = res.data.result.movie_comments
      this.showComment()
    }).catch(function(error){
      console.log(error);
    })
    this.$http.get('http://182.92.57.178:5000/topics/hot').then(res=>{
      console.log(res)
      this.topics = res.data.result
      this.showTopics()
    }).catch(function(error){
      console.log(error);
    })
  },
  methods: {
    onChange(a, b, c) {
      console.log(a, b, c);
    },
    showBook(){
      console.log(this.books);
      this.books.sort(function (a, b) {
        return b.Book_score - a.Book_score;
      })
      console.log(this.books);
    },
    showMovie(){
      console.log(this.movies);
      this.movies.sort(function (a, b) {
        return b.Movie_score - a.Movie_score;
      })
      console.log(this.movies);
    },
    showComment(){
      this.bookcomments.sort(function (a, b) {
        return b.Book_comment_approve - a.Book_comment_approve;
      })
      this.moviecomments.sort(function (a, b) {
        return b.Movie_comment_approve - a.Movie_comment_approve;
      })
      console.log(this.bookcomments)
      console.log(this.moviecomments)
      this.posts.push({
        "id": this.bookcomments[0].Book_comment_id,
        "content": this.bookcomments[0].Book_comment_content,
        "title": this.bookcomments[0].Book_comment_title,
        "Create_time": this.bookcomments[0].Create_time,
        "disapproval": this.bookcomments[0].Book_comment_disapprove,
        "approval": this.bookcomments[0].Book_comment_approve
      })
      this.posts.push({
        "id": this.moviecomments[0].Movie_comment_id,
        "content": this.moviecomments[0].Movie_comment_content,
        "title": this.moviecomments[0].Movie_comment_title,
        "Create_time": this.moviecomments[0].Create_time,
        "disapproval": this.moviecomments[0].Movie_comment_disapprove,
        "approval": this.moviecomments[0].Movie_comment_approve
      })
    },
    showTopics(){

    }
  },

}
</script>

<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  line-height: calc( 100% / 1700 * 520 );
  background: rgb(66, 66, 66);
  overflow: hidden;
}

.ant-carousel >>> .slick-slide h3 {
  color: #fff;
}

.ant-carousel >>> .custom-slick-arrow {
  width: 25px;
  height: 25px;
  font-size: 25px;
  color: #fff;
  background-color: rgba(31, 45, 61, 0.11);
  opacity: 0.3;
}

.ant-carousel >>> .custom-slick-arrow:before {
  display: none;
}
.ant-carousel >>> .custom-slick-arrow:hover {
  opacity: 0.5;
}
</style>