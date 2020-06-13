<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content style="margin:0 10% 0 10%">
        <a-page-header
            style="margin-left:28px;margin-top:30px"
            title="话题"
            sub-title="Topics"
        />
        
         <wordcloud
          :data="topics"
          nameKey="Topic_name"
          valueKey="Topic_id"
          :color="myColors"
          :showTooltip="false"
          :wordClick="wordClickHandler">
          </wordcloud>
        
        <a-divider/>

        <a-page-header
            style="margin-left:10%;margin-top:30px"
            title="话题列表"
            sub-title="Topic List"
        />

        <a-list
                  class="comment-list"
                  item-layout="vertical"
                  :data-source="topics"
                  style="margin:24px 200px 0 200px;text-align:center"
              >
              <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                  <a-card>
                    <a-list-item-meta :description="'话题简介：'+item.Topic_intro">
                        <a slot="title" :href="'/#/topic/topic/'+item.Topic_id">
                        {{item.Topic_name}}
                        </a>
                        <!--a-avatar slot="avatar" :src="item.avatar" /-->
                    </a-list-item-meta>
                    <template >
                        <span> <a-icon type="fire-o" style="margin-left: 8px" /> 话题相关： <span style="color:grey">{{item.Topic_related}}</span></span>
                        <a-tooltip :title="item.Create_time"><span>{{ item.Create_time}}</span></a-tooltip>    
                    </template>
                  </a-card>
                  
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
      wewe:"asas",
      topics: [],
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
    };
  },
  mounted:function(){
      this.$http.get('http://182.92.57.178:5000/topics').then((response)=>{
        console.log(response.data);
        this.topics=response.data.result;
      }).catch((response)=>{
        console.log(response);
      })
    },
  methods: {
    wordClickHandler(name,value){
      console.log(name)
      this.$router.push({ path:"/topic/topic/"+value});
    }
  }
};
</script>