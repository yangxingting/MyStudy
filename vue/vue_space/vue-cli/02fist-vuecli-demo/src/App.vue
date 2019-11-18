<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <myPage></myPage>
    <van-button>这里是一个按钮 </van-button>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
//es6 语法倒入 myPage
import ABC from "./components/myPage"
import {Button} from "vant"

export default {
  name: 'app',
  components: {
    // HelloWorld
    "myPage":ABC,
    [Button.name]:Button
  }
}
</script>

// 全局样式 
<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
body,div,p,span,h1,h2,h3,h4{
  margin: 0;
  padding: 0;
  list-style: none;
}

</style>
