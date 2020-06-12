<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content style="margin:0 10% 0 10%">
        <a-page-header
            style="margin-left:28px;margin-top:30px"
            title="小组"
            sub-title="Groups"
        />
         <wordcloud
          :data="groups"
          style="cursor: pointer;"
          nameKey="Group_name"
          valueKey="Group_id"
          :color="myColors"
          :showTooltip="false"
          fontScale="n"
          :wordClick="wordClickHandler">
          </wordcloud>
        
        <a-divider/>
        
        <a-page-header
            style="margin-left:10%;margin-top:30px"
            title="小组列表"
            sub-title="Group List"
        />
              <a-list
                  class="comment-list"
                  item-layout="vertical"
                  :data-source="groups"
                  style="margin:24px 200px 0 200px;text-align:center"
              >
              <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                  <a-card>
                    <a-list-item-meta :description="'小组简介：'+item.Group_intro">
                        <a slot="title" :href="'/#/group/group/'+item.Group_id">
                        {{item.Group_name}}
                        </a>
                        <!--a-avatar slot="avatar" :src="item.avatar" /-->
                    </a-list-item-meta>
                    <template >
                        <span> <a-icon type="user-o" style="margin-left: 8px" /> 管理员ID {{item.User_id}}</span>
                        <span> <a-icon type="fire-o" style="margin-left: 8px" /> 小组相关： <span style="color:grey">{{item.Group_related}}</span></span>
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
      groups:[
      ],
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
    };
  },
  mounted:function(){
      this.$http.get('http://182.92.57.178:5000/groups').then((response)=>{
        console.log(response.data);
        this.groups=response.data.result;
      }).catch((response)=>{
        console.log(response);
      })
    },
  methods: {
    wordClickHandler(name){
      console.log(this.groups.findIndex(name).id)
      this.$router.push({path:"/group/group/"+this.groups.findIndex(name).id});
    },
  }
};
</script>