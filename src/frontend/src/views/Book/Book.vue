<template>
  <div>
  <a-layout>
      <a-layout-content style="margin-top:30px">
        
        <a-layout>
            <a-layout-content>
                <a-page-header
                    style="margin-left:0"
                    title="返回上一页"
                    @back="back"
                />
                <a-card style="margin:0 20px 0 20px">
                
                <a-row>
                    <img style="text-align:left" :src="book[0].coversrc" height="500px"  />
                </a-row>
                <a-row>
                <h style="font-size:40px">{{book[0].name}}</h>
                <div style="font-size:18px">{{book[0].author}}</div>
                </a-row>
                <a-row>
                    <a-rate :default-value="book[0].star" disabled /> 
                </a-row>
                <a-row>
                    <div style="font-size:32px"><h1>{{book[0].star}}</h1></div>
                </a-row>
                <a-row>  
                    <div style="margin:0 50px 0 50px">{{book[0].pro}}</div>
                </a-row>
                </a-card>
            </a-layout-content>
        </a-layout>
        <a-page-header
            style="margin-left:10%;margin-top:30px"
            title="评论列表"
            sub-title="Comments"
        />
        <!--以下是列表渲染部分-->
        <a-list
            class="comment-list"
            :header="`${data.length} replies`"
            item-layout="horizontal"
            :data-source="data"
            style="margin-top:20px"
        >
          <a-list-item slot="renderItem" slot-scope="item">
            <a-comment :author="item.author" :avatar="item.avatar">
                <template slot="actions">
                <span v-bind:key="action" v-for="action in item.actions">{{ action }}</span>
                </template>
                <p slot="content">
                {{ item.content }}
                </p>
                <a-tooltip slot="datetime" :title="item.datetime.format('YYYY-MM-DD HH:mm:ss')">
                <span>{{ item.datetime.fromNow() }}</span>
                </a-tooltip>
            </a-comment>
          </a-list-item>
        </a-list>

      </a-layout-content>
      <a-layout-footer><h6>书籍影视交流平台</h6></a-layout-footer>
    </a-layout>
  </div>
</template>

<script>
import moment from 'moment';

export default {
    data() {
        return {
        book: [
            {name:'Hunter X Hunter', 
            author:'富坚义博', 
            pro:'故事讲述一个自幼丧母的少年小冈，为了要寻找失散多年的父亲，及成为一个和父亲一样出色的“猎人”，踏上了崎岖而漫长的旅程，接受重重测试，途中遇上各色各样的同伴和敌人，各自为了不同的目的而展开一场又一场的战斗……',
            star:'5',
            coversrc:"https://img9.doubanio.com/view/subject/s/public/s26041185.jpg"},
            
        ],
        data: [
            {
            actions: ['Reply to','Like'],
            author: 'Han Solo',
            avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
            content:
                'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
            datetime: moment().subtract(1, 'days'),
            },
            {
            actions: ['Reply to','Like'],
            author: 'Han Solo',
            avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
            content:
                'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
            datetime: moment().subtract(2, 'days'),
            }],
            moment,
        }
    },
  methods: {
    back(){
        this.$router.push({path:"/book/index"});
    },
  }
};
</script>