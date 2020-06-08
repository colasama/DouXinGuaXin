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
          <p v-if="noTitleKey === 'article'">
            article content
          </p>
          <p v-else-if="noTitleKey === 'app'">
            app content
          </p>
          <p v-else-if="noTitleKey === 'project'">
            project content
          </p>
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
          key: 'app',
          tab: '头像',
        },
        {
          key: 'project',
          tab: '设置',
        },
      ],
      key: 'tab1',
      noTitleKey: 'app',
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