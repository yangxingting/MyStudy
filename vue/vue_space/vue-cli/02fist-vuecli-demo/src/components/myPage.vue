// 组件定义
<template>
    <div class="mypage">
        <h1>我的Vue页面</h1>
        <p class="info">{{info}}</p>
    </div>
</template>

<script>
export default {
    // name,data,methods,生命周期函数，computed等
    name:"myPage",
    data:function(){
        return {
            info:"欢迎来到我的vue页面 "
        }
    }
}
</script>

// scoped 只在当前组件中有效
<style  scoped lang="scss">
.mypage{
    background-color: yellow;
    .info{
    background-color: red;
    color: white; 
}

}



</style>