<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>
        <a-page-header
            style="margin-left:28px;margin-top:30px"
            title="个人主页"
            sub-title="Profile"
        />

        <div>
        <a-card
          style="width:90%;margin:24px auto;"
          :tab-list="tabListNoTitle"
          :active-tab-key="noTitleKey"
          @tabChange="key => onTabChange(key, 'noTitleKey')"
        >
          <div v-if="noTitleKey === 'article'" style="margin-bottom:20px">
            <a-avatar :size="128" style="margin-top:20px"></a-avatar>
            <div style="font-size:24px;color:grey;margin:10px"><b>{{User_name}}</b></div>
            <div>账号：colanns</div>
            <div>ID: 0000001</div>
            <div>手机号：13051008168</div>
            <div>邮箱：mycolands@gmail.com</div>
          </div>
          <div v-else-if="noTitleKey === 'project'">
            <div><a-input placeholder="手机号" style="width:400px;margin-top:20px"></a-input></div>
            <div><a-input placeholder="修改邮箱" style="width:400px;margin-top:20px"></a-input></div>
            <div><a-input placeholder="昵称" style="width:400px;margin-top:20px"></a-input></div>
            <div><a-button type="primary" style="width:400px;margin:20px 0 20px 0">保存</a-button></div>
          </div>
        </a-card>
      </div>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<style>
</style>

<script>
export default {
  data() {
    return {
      User_name:"Colanns",
      tabList: [
        {
          key: 'tab1',
          // tab: 'tab1',
          scopedSlots: { tab: 'customRender' },
        },
        {
          key: 'tab2',
          tab: 'tab2',
        },
      ],
      contentList: {
        tab1: 'content1',
        tab2: 'content2',
      },
      tabListNoTitle: [
        {
          key: 'article',
          tab: '个人信息',
        },
        {
          key: 'project',
          tab: '设置',
        },
      ],
      key: 'tab1',
      noTitleKey: 'article',
    };
  },
  methods: {
    onTabChange(key, type) {
      console.log(key, type);
      this[type] = key;
    },
  },
};
</script>