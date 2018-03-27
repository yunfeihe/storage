// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from "vue-router";
import VueReouce from "vue-resource";
import goods from "./components/goods/goods.vue";
import seller from "./components/seller/seller.vue";
import ratings from "./components/ratings/ratings.vue";

import "./common/css/index.css";

Vue.config.productionTip = false
Vue.use(VueRouter);
Vue.use(VueReouce);

const routes = [
  {
    path: "/goods",
    component: goods,
  },
  {
    path: "/seller",
    component: seller,
  },
  {
    path: "/ratings",
    component: ratings,
  },

]

const router = new VueRouter({
  routes,
  linkActiveClass: "active",
});

/* eslint-disable no-new */
let app = new Vue({
  el: '#app',
  router,
  components: {
    App, 
  },
  template: '<App></App>'
})

// let firstTime = false;
// if(!firstTime){
//   router.go("/goods");
//   firstTime = true;
// }

