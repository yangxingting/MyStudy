<style lang="scss">
@import "styles/init.css";
.van-search {
    padding: 0;
}
</style>

<template>
  <div id="app">
    <router-view></router-view>
      <van-tabbar v-model="active">
          <van-tabbar-item icon="wap-home-o" to="/">首页</van-tabbar-item>
          <van-tabbar-item icon="orders-o" to="/order">订单</van-tabbar-item>
          <van-tabbar-item icon="user-o" to="/mine">我的</van-tabbar-item>
    </van-tabbar>    
    
      
    
    
  </div>
</template>

<script>
//倒入组件
import { Tabbar, TabbarItem } from 'vant';

export default {
  

  name: 'app',
  // 注册组件
  data(){
    return { 
      active:0,
    }
  },
  components: {
    [Tabbar.name]:Tabbar,
    [TabbarItem.name]:TabbarItem
  }
}
</script>

