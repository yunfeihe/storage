<template>
  <div id="app">
    <!-- <router-view/> -->
    <el-header :seller="seller"></el-header>
    <div class="tap">
      <div class="tab-item">
        <router-link to="./goods" >商品</router-link>
      </div>
      <div class="tab-item">
        <router-link to="./ratings">评论</router-link>
      </div>
      <div class="tab-item">
        <router-link to="./seller">商家</router-link>
      </div>
    </div>
    <div class="content">
      <keep-alive>
      <router-view :seller="seller"></router-view>

      </keep-alive>
    </div>
  </div>
</template>


<script>
import header from "./components/header/header";
import __data from "./data.js";
export default {
  name: 'App',
  data() {
    return {
      seller: {},
    };
  },
  created () {
    let vm = this;
    // this.$http.get("http://localhost:8000/api/seller").then((res) => {
    //   vm.seller = res.body.data;
    //   console.log("vm", vm.seller);
    // });
    vm.seller = __data.seller;
  },
  components: {
    "el-header": header,
  },
}
</script>

<style>
  #app .tap {
    display: flex;
    width: 100%;
    height: 40px;
    line-height: 40px;
    text-align: center;
    position: relative;
    border-bottom: 1px solid rgba(7, 17, 27, 0.1);

  }

  .tap::after {
    display: block;
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
  }

  #app .tap .tab-item {
    flex-grow: 1;
  }
  #app .tap .tab-item a {
    display: block;
    font-size: 14px;
    color: rgb(77, 85, 93);
  }
  #app .tap .tab-item a.active {
    color: red;
  }


</style>
