<template>
  <div>
  <a-layout class="wrapper">
      <a-layout-content class="contenter">
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
      <a-layout-footer class="footer"><h6>书籍影视交流平台</h6></a-layout-footer>
    </a-layout>
  </div>
</template>

<style>
.wrapper{
  display:flex;
  flex-direction:column;
  min-height:100%;
}

.contenter{
    text-align: center;
    position:absolute;
    width:100%;
    height: calc(100% - 100px) ;
    background: rgb(240, 242, 245);
  }

.footer{
  flex: 0;
  position:absolute;
  bottom:0;
  width:100%;
  background: rgb(227, 232, 236);
}
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