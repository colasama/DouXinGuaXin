<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>
        <a-page-header
            style="margin-left:28px;margin-top:30px"
            title="小组"
            sub-title="Groups"
        />
         <wordcloud
          :data="groups"
          nameKey="name"
          valueKey="value"
          :color="myColors"
          :showTooltip="false"
          :wordClick="wordClickHandler">
          </wordcloud>

        <a-list :grid="{ gutter: 16, column: 16 }" :data-source="groupp" style="margin:24px">
          <a-list-item slot="renderItem" slot-scope="group">
            <a-tag>{{group}}</a-tag>
          </a-list-item>
        </a-list>
        
        <a-divider/>
        
        <a-page-header
            style="margin-left:10%;margin-top:30px"
            title="热门帖子"
            sub-title="Hot Posts"
        />
              <a-list
                  class="comment-list"
                  item-layout="vertical"
                  :data-source="posts"
                  style="margin:24px 200px 0 200px;text-align:center"
              >
              <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                  <a-list-item-meta :description="item.content">
                      <a slot="title" :href="'/object/'+item.id">
                      {{item.title}}
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
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
import wordcloud from 'vue-wordcloud';

export default {
  components:{
    wordcloud
  },
  data() {
    return {
      groups: [
        {"name":"系统编程","value":"28"},
        {"name":"面向对象","value":"30"},
        {"name":"软件工程","value":"31"},
        {"name":"面向对象","value":"20"},
      ],
      posts:[
        {"name":"rr","title":"aa","content":"aasasasas","id":"1"},
        {"name":"rr","title":"aa","content":"aasasasas","id":"2"}
      ],
      groupp: [
        "软件工程","面向对象","系统编程"
      ],
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
    };
  },
  methods: {
    wordClickHandler(){
      
    }
  }
};
</script>