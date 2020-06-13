<template>
  <div>
  {{this.$route.params.id}}
  <a-layout style="min-height:100%">
      <a-layout-content style="margin-top:30px;text-align:center">
            <a-page-header
                style="margin-left:24px"
                title="返回上一页"
                @back="back"
            />
          <!--参考那个Topic里一样的 唯一区别是这个有标题，其余大致相同 可以参考api文档的返回参数来设计
            <a-card style="margin:24px;text-align:left">

                <span style="margin-left:24px;font-size:24px"><b>{{group_content_title}}</b></span>
                <div style="margin-left:24px;margin-top:10px;font-size:16px"><a-avatar style="margin:-12px 5px 0 0"></a-avatar>{{User_name}} &nbsp; {{Create_time}}</div>
                <a-divider></a-divider>

                <div style="font-size:16px;margin:30px 0 0 24px;">{{group_content_content}}</div>
                <template slot="actions" >
                    <span> <a-icon type="like-o" style="margin-left: 8px" /> 赞</span>
                    <span> <a-icon type="dislike-o" style="margin-left: 8px" /> 踩</span>
                </template>
        
            </a-card>-->
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
export default {
    data() {
        return {
            group_cotents: []
        }
    },
    mounted() {
        this.$http.get('http://182.92.57.178:5000/groups/' + this.$route.params.id).then(res=>{
            console.log(res)
            this.group_cotents = res.data.result
        }).catch(function(error){
            console.log(error);
        })
    },
    methods: {
    back(){
        this.$router.push({path:"/group/index"});
    },
  }
};
</script>