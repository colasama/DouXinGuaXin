<template>
  <div>
  <a-layout>
      <a-layout-content style="margin-top:30px">
        <a-select style="width: 70px" default-value="书籍">
          <a-select-option value="book">
            书籍
          </a-select-option>
          <a-select-option value="movie">
            影视
          </a-select-option>
        </a-select>
        <a-input-search placeholder="书籍搜索" style="width: 200px" @search="onSearch"/>
        <!--以下是列表渲染部分-->
        <a-list :grid="{ gutter: 16, column: 4 }" :data-source="books" style="margin-top:20px">
          <a-list-item slot="renderItem" slot-scope="book">
            <a-card>
              <a-row type="flex" justify="center" align="center">
                <a-col :span="8" >
                <img
                  height="200px"
                  :src="book.coversrc"
                />
                </a-col>
                <a-col :span="16">
                  <a-card-meta :title="book.name"/>
                    {{book.pro}}<br/>
                  <a-rate :default-value="book.star" disabled />
                </a-col>
              </a-row>
            </a-card>
          </a-list-item>
        </a-list>

      </a-layout-content>
      <a-layout-footer><h6>书籍影视交流平台</h6></a-layout-footer>
    </a-layout>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books: [
        {name:'rua1', pro:'re1',star:'5',coversrc:'https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png'},
        {name:'rua2', pro:'re2',star:'5',coversrc:'https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png'},
        {name:'rua3', pro:'re3',star:'5',coversrc:'https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png'},
        {name:'rua4', pro:'re4',star:'5',coversrc:'https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png'},
        {name:'rua5', pro:'re5',star:'5',coversrc:'https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png'},
        {name:'rua6', pro:'re6',star:'5',coversrc:'https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png'}
      ],
    };
  },
  methods: {
    
  }
};
</script>