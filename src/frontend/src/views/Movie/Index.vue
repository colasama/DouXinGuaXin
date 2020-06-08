<template>
  <div>
  <a-layout>
      <a-layout-content style="margin-top:30px;height:100%" >
        <a-button @click="refresh">Refresh</a-button>
        <a-select style="width: 70px" default-value="书籍">
          <a-select-option value="book">
            书籍
          </a-select-option>
          <a-select-option value="movie">
            影视
          </a-select-option>
        </a-select>
        <a-input-search placeholder="影视搜索" style="width: 200px" @search="onSearch"/>
        <div>{{books}}</div>
        <!--以下是列表渲染部分-->
        <a-list :grid="{ gutter: 16, column: 4 }" :data-source="books.result" style="margin:24px">
          <a-list-item slot="renderItem" slot-scope="book">
            <a-card>
              <a-row type="flex" justify="center" align="center">
                <a-col :span="8" >
                <img
                  height="200px"
                  :src="book.Book_src"
                />
                </a-col>
                <a-col :span="16">
                  <a-card-meta :title="book.Book_name"/>
                    {{book.Book_intro.substring(0,50)}}...<br/>
                  <a-rate :default-value="book.Book_score" disabled />
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
      books: [
      ],
    };
  },
  methods: {
    created(){
      this.$http.get('http://182.92.57.178:5000/books').then((response)=>{
        console.log("rua");
        console.log(response.data);
        this.books=response.data;
      }).catch((response)=>{
        console.log(response);
      })
    },
    refresh(){
      this.$http.get('http://182.92.57.178:5000/books').then((response)=>{
        console.log("rua");
        console.log(response.data);
        this.books=response.data;
      }).catch((response)=>{
        console.log(response);
      })
    }


  }
};
</script>