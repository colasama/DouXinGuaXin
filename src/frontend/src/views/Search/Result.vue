<template>
  <div>
  <a-layout>
      <a-layout-content style="margin-top:15%;margin-bottom:15%">
          <h1 style="font-size:40px">千度搜索</h1>
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
      </a-layout-content>
    </a-layout>
  </div>
</template>
