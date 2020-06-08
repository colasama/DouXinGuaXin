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
              style="border: 1px solid rgb(235, 237, 240);margin-left:25%"
              title="热点书籍"
              sub-title="24小时内最热书籍"
            />
            <!--这里是书籍内容-->
            <div style="padding: 20px;margin: auto;">
              <a-row type="flex" justify="center" align="top">
                <a-col :span="4">

                  <a-card hoverable style="width: 240px">
                    <img
                      slot="cover"
                      alt="example"
                      src="https://img9.doubanio.com/view/subject/l/public/s33621450.jpg"
                    />
                    <a-card-meta title="Book1">
                      <template slot="description">
                        description 1
                      </template>
                    </a-card-meta>
                  </a-card>

                </a-col>
                <a-col :span="4">

                  <a-card hoverable style="width: 240px">
                    <img
                      slot="cover"
                      alt="example"
                      src="https://img9.doubanio.com/view/subject/l/public/s33613369.jpg"
                    />
                    <a-card-meta title="Book2">
                      <template slot="description">
                        description 2
                      </template>
                    </a-card-meta>
                  </a-card>

                </a-col>
                <a-col>

                  <a-card hoverable style="width: 240px">
                    <img
                      slot="cover"
                      alt="example"
                      src="https://img9.doubanio.com/view/subject/l/public/s33601722.jpg"
                    />
                    <a-card-meta title="Book3">
                      <template slot="description">
                        escription 3
                      </template>
                    </a-card-meta>
                  </a-card>
                  
                </a-col>
              </a-row>
            </div>
          </a-tab-pane>
          <a-tab-pane key="2" tab="影视">
            <!--这里是影视-->
          </a-tab-pane>
        </a-tabs>
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
      ]
    }
  },
  created:function(){
    console.log(global_.username);
  },
  methods: {
    onChange(a, b, c) {
      console.log(a, b, c);
    },
  },

}
</script>

<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 520px;
  line-height: 240px;
  background: #FFE4B5;
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