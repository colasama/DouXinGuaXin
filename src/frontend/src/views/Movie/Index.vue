<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>
        <a-page-header
            style="margin-left:28px;margin-top:30px"
            title="影视"
            sub-title="Movies"
        />
        <a-button @click="refresh">Refresh</a-button>
        <div>{{movies}}</div>
        <!--以下是列表渲染部分-->
        <a-list :grid="{ gutter: 16, column: 4 }" :data-source="movies.result" style="margin:24px">
          <a-list-item slot="renderItem" slot-scope="movie">
            <a-card>
              <a-row type="flex" justify="center" align="center">
                <a-col :span="8" >
                <img
                  height="200px"
                  :src="movie.Movie_src"
                />
                </a-col>
                <a-col :span="16">
                  <a-card-meta :title="movie.Movie_name"/>
                    {{movie.Movie_intro.substring(0,50)}}...<br/>
                  <a-rate :default-value="movie.Movie_score" disabled />
                </a-col>
              </a-row>
            </a-card>
          </a-list-item>
        </a-list>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
export default {
  data() {
    return {
      movies: [
      ],
    };
  },
  mounted:function(){
      console.log("乌乌创建了");
      this.$http.get('http://182.92.57.178:5000/movies').then((response)=>{
        console.log("rua");
        console.log(response.data);
        this.movies=response.data;
      }).catch((response)=>{
        console.log(response);
      })
    },
  methods: {
    refresh(){
      this.$http.get('http://182.92.57.178:5000/movies').then((response)=>{
        console.log("rua");
        console.log(response.data);
        this.movies=response.data;
      }).catch((response)=>{
        console.log(response);
      })
    }
  }
};
</script>