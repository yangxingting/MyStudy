import VueRouter from "vue-router"
import Vue from 'vue'

import Home from "./components/Home.vue"
import Mine from "./components/Mine.vue"
import Order from "./components/Order.vue"
import Merchant from "./components/Merchant.vue"

Vue.use(VueRouter)

const routes = [{
        path: "/",
        component: Home,
        name: "home"
    },
    {
        path: "/order",
        component: Order,
        name: "order"
    },
    {
        path: "/mine",
        component: Mine,
        name: "mine"
    }, {
        path: "/merchant/:merchantId",
        component: Merchant,
        name: "merchant",

    }

]

const router = new VueRouter({
    routes
})

//将路由导出
export default router;