<template>
  <div>
  <a-layout>
      <a-layout-content style="margin-top:10px">
        <a-select style="width: 70px" default-value="书籍">
          <a-select-option value="book">
            书籍
          </a-select-option>
          <a-select-option value="movie">
            影视
          </a-select-option>
        </a-select>
        <a-input-search placeholder="书籍搜索" style="width: 200px" @search="onSearch"/>


      </a-layout-content>
      <a-layout-footer><h6>书籍影视交流平台</h6></a-layout-footer>
    </a-layout>
  </div>
</template>
