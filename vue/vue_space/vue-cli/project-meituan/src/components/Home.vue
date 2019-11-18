
 <style scoped>
 .van-dropdown-menu >>> .van-dropdown-menu__title{
  color: #767676;
}
.van-dropdown-menu__item{
  font-size: 14px;
  color: #767676;
}

 </style> 
 
 
 <style scoped lang="scss">
 .header-group{
     background-color: #1c1B20;
     padding: 20px 14px 10px;
     .address-group{
         color:white;
         font-size: 16px;
         font-weight: 700;
     }
     .search-group{
         margin-top: 10px;
     }
     
 }
 .main-group{
     padding: 10px;

     
 }
 .merchant-list{
      .merchant-item{
          padding: 10px;
          display: flex;
          .logo{
              width: 85px;
              height: 64px;
          }
          .merchant-info{
              margin-left: 5px;
              .merchant-name{
                  font-size: 16px;
                  font-weight: 700;
              }
              .rate-group{
                  padding-top: 3px;
              }
              .tag-group{
                  padding-top: 3px;
                  span{
                      margin-right: 3px;
                  }
              }
          }

      }
      
      
 }

     
 </style>



 
 <template>
     <div class="home-container">
         <div class="header-group">
             <div class="address-group">
                 <i class="iconfont icon-dingweiweizhizuobiaoxianxing"></i>
                 <span class="address">上海</span>
                 <i class="iconfont icon-jiantouyou"></i>

                 
             </div>

             <div class="search-group">
                 <van-search placeholder="请输入搜索关键词"  />
             </div>
         </div>

        
         <div class="main-group">
             <h2>推荐商家</h2>
             <van-dropdown-menu> 
                 <van-dropdown-item v-model="sort" :options="sorts"></van-dropdown-item>
                 <div class="van-dropdown-menu__item">距离最近</div>
                    <div class="van-dropdown-menu__item">品质联盟</div>
                    <div class="van-dropdown-menu__item">筛选<i class="iconfont icon-loudou"></i></div>
             </van-dropdown-menu>

            <!-- 商品列表 -->
             <div class="merchant-list">
                 <!-- 列表item1 -->
                 <router-link to="/merchant/1">
                 <div class="merchant-item">
                        <!-- 图片logo -->
                       <img src="http://p1.meituan.net/xianfu/33c48a92a31a21e4bf32d3aa7c1c5c0d16649.jpg" alt="" class="logo">
                 
                        <!-- 商品描述信息 -->
                        <div class="merchant-info">
                            <div class="merchant-name ">肯德基</div>
                            <div class="rate-group">
                                <van-rate v-model="rate" size=10px></van-rate>
                                
                            </div>

                            <div class="tag-group">
                                <van-tag plain>美团专送</van-tag>
                                <van-tag plain>家常菜</van-tag>
                            </div>
                        </div>
                 </div>
                 </router-link>

                <!-- 列表item2 -->
                 <div class="merchant-item">
                        <!-- 图片logo -->
                       <img src="http://p1.meituan.net/xianfu/33c48a92a31a21e4bf32d3aa7c1c5c0d16649.jpg" alt="" class="logo">
                 
                        <!-- 商品描述信息 -->
                        <div class="merchant-info">
                            <div class="merchant-name ">肯德基</div>
                            <div class="rate-group">
                                <van-rate v-model="rate" size=10px></van-rate>
                                
                            </div>

                            <div class="tag-group">
                                <van-tag plain>美团专送</van-tag>
                                <van-tag plain>家常菜</van-tag>
                            </div>
                        </div>
                 </div>

             </div>
             
         </div>
        


         
          
     </div>

    
 </template>


<script>
import { Search,DropdownMenu, DropdownItem,Rate,Tag} from 'vant';

export default {
    name:"Home",
    data(){
        return {
            rate:4,
            sort:0,
            sorts:[
                { text: '综合排序', value: 0 },
                { text: '好评优先', value: 1 },
                { text: '销量最高', value: 2 },
                { text: '距离最近', value: 3 }, 
            ]
        }
    },
    components:{
        [Search.name]:Search,
        [DropdownMenu.name]:DropdownMenu,
        [DropdownItem.name]:DropdownItem,
        [Rate.name]:Rate, 
        [Tag.name]:Tag, 

    }
    
}
</script>

