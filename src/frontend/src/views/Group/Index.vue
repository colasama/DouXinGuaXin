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
            title="今日神贴"
            sub-title="God Posts"
        />

        <a-list item-layout="horizontal" :data-source="posts">
          <a-list-item style="margin:0 200px 0 200px" slot="renderItem" slot-scope="item">
            <a-list-item-meta
              :description="item.content"
            >
              <a slot="title" :href="'/#/group/object/'+item.id">{{ item.title }}</a>
              <a-avatar
                slot="avatar"
                src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
              />
            </a-list-item-meta>
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