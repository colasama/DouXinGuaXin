<template>
  <div class="home">
    
    <a-layout>
      <a-layout-content>
      <a-carousel :after-change="onChange">
          <div><h3>1</h3></div>
          <div><h3>2</h3></div>
          <div><h3>3</h3></div>
          <div><h3>4</h3></div>
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
      <a-layout-footer><h6>书籍影视交流平台</h6></a-layout-footer>
    </a-layout>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {

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
  height: 240px;
  line-height: 240px;
  background: #FFE4B5;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide h3 {
  color: #fff;
}
</style>