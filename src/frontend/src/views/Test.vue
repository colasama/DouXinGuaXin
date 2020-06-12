<template>
    <div>
        <a-layout style="min-height:100%">
            <a-button @click="showReport">举报</a-button>
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
                <p>
                    <cReport />
                </p>
            </a-modal>
        </a-layout>
    </div>
</template>

<script>
    import cReport from '../components/Report.vue';
    export default {
        components:{
            cReport,
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