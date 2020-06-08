<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content style="margin-top:25px">
        <a-page-header
          style="text-align:center"
          title="搜索结果"
        />
        <a-select style="width: 70px;height: 40px;" default-value="书籍">
          <a-select-option value="book">
            书籍
          </a-select-option>
          <a-select-option value="movie">
            影视
          </a-select-option>
          <a-select-option value="posts">
            帖子
          </a-select-option>
          <a-select-option value="topic">
            图文
          </a-select-option>
        </a-select>
        <a-input-search placeholder="书籍搜索" style="width: 400px;height:40px;" @search="onSearch"/>
      
      <a-list item-layout="horizontal" :data-source="data">
        <a-list-item slot="renderItem" slot-scope="item">
          <a-card style="width:100%">
          <a-list-item-meta
            :description="item.des"
          >
            <a slot="title" :href="'/books/' + item.id">{{ item.title }}</a>
            <!--a-avatar
              slot="avatar"
              src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
            /-->
          </a-list-item-meta>
          </a-card>
        </a-list-item>
        
      </a-list>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
  export default{
  data() {
      return {
        results: [],
        data:[
          {id:1,title:"aaa",des:"fff"},
          {id:1,title:"aaa",des:"fff"},
          {id:1,title:"aaa",des:"fff"},
          {id:1,title:"aaa",des:"fff"},
          {id:1,title:"aaa",des:"fff"},
          {id:1,title:"aaa",des:"fff"},
        ]
      };
    },
    methods:{ 

    },
  }
</script>