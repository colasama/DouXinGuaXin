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
                      width="60px"
                      slot="cover"
                      alt="example"
                      :src="books[0].Book_src"
                    /></a>
                    <a-card-meta :title="books[0].Book_name">
                      <template slot="description">
                        {{books[0].Book_intro.substr(0,35)}}
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>

                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/book/object/'+books[1].Book_id">
                      <img
                        width="60px"
                        slot="cover"
                        alt="example"
                        :src="books[1].Book_src"
                      /></a>
                    <a-card-meta :title="books[1].Book_name">
                      <template slot="description">
                        {{books[1].Book_intro.substr(0,35)}}
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>
                
                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/book/object/'+books[2].Book_id">
                      <img
                        width="60px"
                        slot="cover"
                        alt="example"
                        :src="books[2].Book_src"
                      /></a>
                    <a-card-meta :title="books[2].Book_name">
                      <template slot="description">
                        {{books[2].Book_intro.substr(0,35)}}
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
                        width="60px"
                        slot="cover"
                        alt="example"
                        :src="movies[0].Movie_src"
                      /></a>
                    <a-card-meta :title="movies[0].Movie_name">
                      <template slot="description">
                        {{movies[0].Movie_intro.substr(0,35)}}
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>

                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/movie/object/'+movies[1].Movie_id">
                      <img
                        width="60px"
                        slot="cover"
                        alt="example"
                        :src="movies[1].Movie_src"
                      /></a>
                    <a-card-meta :title="movies[1].Movie_name">
                      <template slot="description">
                        {{movies[1].Movie_intro.substr(0,35)}}
                      </template>
                    </a-card-meta>
                  </a-card>
                </a-col>

                <a-col :span="2"/>
                
                <a-col :span="4">
                  <a-card hoverable style="width: 240px">
                    <a :href="'/#/movie/object/'+movies[2].Movie_id">
                      <img
                        width="60px"
                        slot="cover"
                        alt="example"
                        :src="movies[2].Movie_src"
                      /></a>
                    <a-card-meta :title="movies[2].Movie_name">
                      <template slot="description">
                        {{movies[2].Movie_intro.substr(0,35)}}
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
                  <a-list-item-meta :description="item.Group_content_content">
                      <a slot="title" :href="'/object/'+item.Group_content_id">
                      {{item.Group_content_title}}
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
              <a-card style="margin-top:10px">
                <div style="color:rgb(170, 46, 24);"><b>#一个小组</b></div>
              </a-card>
              <a-card style="margin-top:10px">
                <div style="color:rgb(170, 46, 24);"><b>#二个小组</b></div>
              </a-card>
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
        "https://i.loli.net/2020/06/08/Sj6c3gY9Ilebf1N.png",
        "https://i.loli.net/2020/06/08/TG8EqWNlRjt6MVo.png",
        "https://i.loli.net/2020/06/08/t5GDicomyeKW7ad.jpg",
        "https://i.loli.net/2020/06/08/eyvBgJF6lbIVLRp.jpg",
      ],
      posts:[
            {"Group_content_id": 4, "Group_content_content": "testtesttest", "Group_content_title": "test", "Group_id":1, 
            "User_id": 15, "Username":"test","Group_content_image": "/example", "Create_time": "2020-06-03 17:50:52", "Is_highlighted": 1, "Is_pinned": 1}, 
            {"Group_content_id": 5, "Group_content_content": "testtesttest123", "Group_content_title": "test123", "Group_id": 1, 
            "User_id": 15,  "Username":"test","Group_content_image": "/example", "Create_time": "2020-06-03 18:30:04", "Is_highlighted": 1, "Is_pinned": 1}
        ],
      books: [],
      movies: []
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