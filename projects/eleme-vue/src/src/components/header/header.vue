<template>
    <div class="header">
        <div class="content-wrap">
            <div class="avatar">
                <img height="64" width="64" :src="seller.avatar" alt="">
            </div>
            <div class="content">
                <span class="title">
                    <span class="brand"></span>
                    <span class="name">{{seller.name}}</span>
                </span>
                <div class="description">
                    {{ seller.description }}/{{ seller.deliveryTime }}分钟送达
                </div>
                <div v-if="seller.supports" class="support">
                    <span class="icon" :class="mapClass[seller.supports[0].type]"></span>
                    <span class="text">{{ seller.supports[0].description }}</span>
                </div>
            </div>
            <div v-if="seller.supports" 
                 class="support-count"
                 @click="showDetail">
                <span class="count">{{ seller.supports.length }}个</span>
                <span class="icon-keyboard_arrow_right"></span>
            </div>
            <div @click="showDetail" class="bulletin-wrap">
                <span class="title"></span>
                <span class="text">{{ seller.bulletin }}</span>
                <span class="icon-keyboard_arrow_right"></span>
            </div>
        </div>
        <div class="background">
            <img :src="seller.avatar" alt="" height="100%" width="100%">
        </div>
<transition name="fade">
  <div v-show="detailShow" class="detail">
    <div class="detail-wrap clear-fix">
      <div class="detail-main">
        <h1>{{ seller.name }}</h1>
        <div class="star-wrap">
          <el-star :score="seller.score" :size="48">
          </el-star>
        </div>
        <div class="sub-title">
          <div class="line"></div>
          <div class="text">优惠信息</div>
          <div class="line"></div>
        </div>
        <ul v-if="seller.supports" class="supports">
          <li class="support-item" v-for="(item, index) in seller.supports">
            <span class="icon" :class="mapClass[item.type]"></span>
            <span class="text">{{ item.description }}</span>

          </li>
        </ul>
        <div class="sub-title">
          <div class="line"></div>
          <div class="text">商家公告</div>
          <div class="line"></div>
        </div>
        <div class="bulletin-text">
          {{ seller.bulletin }}
        </div>
      </div>
    </div>
    <div class="close" @click="hideDetail">
      <span class="icon-close"></span>
    </div>
  </div>
</transition>


    </div>  
</template>

<script>
    import star from "../star/star.vue";
    export default {
        data(){
            return {
                detailShow: false,
            };
        },
        methods: {
            showDetail(){
                this.detailShow = true;
            },
            hideDetail(){
                this.detailShow = false;
            },
        },
        props: {
            seller: {
                type: Object,
            }
        },
        created () {
            console.log("seller.star", this.seller.star)

            this.mapClass = [
                "decrease",
                "discount",
                "guarantee",
                "invoice",
                "sepcial",
            ];
        },
        components: {
            "el-star": star,
        },
    };

</script>

<style>
@import "./header.css";
</style>
