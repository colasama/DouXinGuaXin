<template>
  <div>
  <a-layout>
      <a-layout-content>
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
        {"name":"系统编程","value":"4"},
        {"name":"面向对象","value":"5"},
        {"name":"软件工程","value":"5"}
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