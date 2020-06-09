<template>
    <div style="text-align:center">
        <a-select style="width: 70px" default-value="书籍">
          <a-select-option value="book">
            书籍
          </a-select-option>
          <a-select-option value="movie">
            影视
          </a-select-option>
          <a-select-option value="group">
            小组
          </a-select-option>
          <a-select-option value="topic">
            话题
          </a-select-option>
          <a-select-option value="pictext">
            图文
          </a-select-option>
          <a-select-option value="post">
            帖子
          </a-select-option>
        </a-select>
        <a-input-search placeholder="搜索" style="width: 200px" @search="onSearch"/>
    </div>
</template>