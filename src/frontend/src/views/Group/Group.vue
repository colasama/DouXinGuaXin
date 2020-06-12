<template>
  <div>
  <a-layout style="min-height:100%">
        <a-layout-content style="min-width:1200px;margin:0 auto;">
            <a-page-header
                style="margin-left:24px;margin-top:30px"
                title="小组"
                sub-title="Groups"
            />

            <div class="header">
                <div>
                    <h1 style="color:white;font-size:40px">#一个小组</h1>
                    <a-button style="text-align:center;border:1px" v-if="!ifJoinedGroup" type="dashed" ><b>加入小组</b></a-button>
                    <a-button v-if="ifJoinedGroup" type="dashed"><b>发表帖子</b></a-button>
                </div>
            </div>

            <a-divider>
                <div style="font-size:18px">共有{{posts.length}}条帖子</div>
            </a-divider>

            <!--帖子渲染部分-->
            <a-list
                class="comment-list"
                item-layout="vertical"
                :data-source="posts"
                style="margin:24px;text-align:center"
            >
            <a-list-item slot="renderItem" slot-scope="item" style="text-align:left">
                <a-list-item-meta :description="item.Group_content_content">
                    <a slot="title" :href="'/object/'+item.Group_content_id">
                    {{item.Group_content_title}}
                    <a-tag style="margin-left:8px" color="red">精华</a-tag>
                    <a-tag style="margin-left:8px" color="orange">置顶</a-tag>
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
<style>
.header{
    height:400px;
    margin:24px;
    text-align:center;
    background:rgb(47, 146, 116);
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
<script>
export default {
  components:{
    
  },
  data() {
    return {
        posts:[
            {"Group_content_id": 4, "Group_content_content": "testtesttest", "Group_content_title": "test", "Group_id":1, 
            "User_id": 15, "Username":"test","Group_content_image": "/example", "Create_time": "2020-06-03 17:50:52", "Is_highlighted": 1, "Is_pinned": 1}, 
            {"Group_content_id": 5, "Group_content_content": "testtesttest123", "Group_content_title": "test123", "Group_id": 1, 
            "User_id": 15,  "Username":"test","Group_content_image": "/example", "Create_time": "2020-06-03 18:30:04", "Is_highlighted": 1, "Is_pinned": 1}
        ],
        ifJoinedGroup:false,
    };
  },
  methods: {
    //估计得有一个getUsernameByID一个getPosts
  }
};
</script>