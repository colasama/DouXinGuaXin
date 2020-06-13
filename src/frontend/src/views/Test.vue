<template>
    <div>
        <a-layout style="min-height:100%">
            <a-button @click="showReport">举报</a-button>
            <!--举报框-->
            <a-modal 
                centered="true"
                title="提交举报"
                :visible="visible"
                :confirm-loading="confirmLoading"
                @ok="handleOk"
                @cancel="handleCancel"
                okText="提交"
                cancelText="取消"
                >
                <div>
                        <div style="margin-top:10px">请确认您要举报的内容：</div>
                        <h2 style="color:black;margin-top:10px;text-align:center">鸽子: 我太菜了</h2>
                        <a-input style="margin-top:10px" placeholder="请填写举报标题" />
                        <a-textarea style="margin-top:10px" placeholder="请描述举报原因，原因需要大于25字。" :auto-size="{ minRows: 5, maxRows: 5 }"></a-textarea>
                        <!--a-button style="margin-top:10px">提交</a-button-->
                </div>
            </a-modal>
        </a-layout>
    </div>
</template>

<script>
    export default {
        components:{
        },
        data() {
            return {
                visible: true,
                okVisible: false,
                confirmLoading: false,
            };
        },
        created: function(){
        },
        watch:{

        },
        methods: {
            showReport(){
                this.visible=true;
            },
            handleOk(e){
                console.log(e);
                this.visible=false;
                this.showSuccess();
            },
            handleCancel(){
                this.visible=false;
            },
            destroyALL(){
                this.$destroyAll();
            },
            showSuccess(){
                this.$success({
                    centered: true,
                    title: '举报成功',
                    content: "已经收到了您的举报，我们将尽快核实并处理！",//<a-result status="success" title=""/>,
                    onOK(){
                        this.destroyALL();
                    }
                })
            },
        }
    };
</script>