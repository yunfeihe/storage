<template>
  <div class="seller" ref="el-seller">
    <div class="seller-content">
      <div class="overview">
        <h1 class="title">{{ seller.name }}</h1>
        <div class="desc">
          <el-star :size="36" :score="seller.score"></el-star>
          <span class="text">({{ seller.ratingCount }})</span>
          <span class="text">月售{{ seller.sellCount }}单</span>
        </div>
        <ul class="remark">
          <li class="block">
            <h2>起送价</h2>
            <div class="content">
              <span class="stress">{{ seller.minPrice }}</span>元
            </div>
          </li>
          <li class="block">
            <h2>商家配送</h2>
            <div class="content">
              <span class="stress">{{ seller.deliveryPrice }}</span>元
            </div>
          </li>
          <li class="block">
            <h2>平均配送时间</h2>
            <div class="content">
              <span class="stress">{{ seller.deliveryTime }}</span>分钟
            </div>
          </li>
        </ul>
        <div 
        @click="toggleFavorite"
        class="favorite">
          <span
          :class="{active: isFavorite}" 
          class="icon icon-favorite"
          ></span>
          <span class="text">{{ favoriteText }}</span>
        </div>
      </div>
      <el-split></el-split>
      <div class="bulletin">
        <h1 class="title">公告与活动</h1>
        <div class="content-wrap">
          <div class="content">{{ seller.bulletin }}</div>
          <ul v-if="seller.supports" class="supports">
            <li 
            class="support-item" 
            v-for="item in seller.supports">
              <span 
              class="icon" 
              :class="mapClass[item.type]"></span>
              <span class="text">{{ item.description }}</span>

            </li>
          </ul>
        </div>
      </div>
      <el-split></el-split>
      <div class="pics">
        <h1 class="title">商家实景</h1>
        <div class="pic-wrap" ref="pic-wrap">
          <ul class="pic-ul">
            <li 
            v-for="pic in seller.pics"
            class="pic-li"
            >
            <img width="120" height="90" :src="pic" alt="">
            </li>
          </ul>
        </div>
      </div>
      <el-split></el-split>
      <div class="info">
        <h1 class="title">商家信息</h1>
        <ul class="info-ul">
          <li 
          v-for="info in seller.infos"
          class="info-li">{{ info }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
  import BScroll from "better-scroll";
  import star from "../star/star.vue";
  import split from "../split/split.vue";

  export default {
    data(){
      return {
        isFavorite: true,
      };
    },
    props: {
      seller: {
        type: Object,
      },
    },
    components: {
      "el-star": star,
      "el-split": split,
    },
    created () {
      this.mapClass = [
          "decrease",
          "discount",
          "guarantee",
          "invoice",
          "sepcial",
      ];
      this.$nextTick(() => {
        this.scroll = new BScroll(this.$refs["el-seller"], {
          click: true,
        });
        this.picScroll = new BScroll(this.$refs["pic-wrap"], {
          scrollX: true,
          eventPassThough: true,
        });
      });
      
      
    },
    computed: {
      favoriteText() {
        return this.isFavorite ? "已收藏" : "未收藏";
      },
    },
    methods: {
      toggleFavorite(){
        this.isFavorite = !this.isFavorite;
      },
    }
  };

</script>

<style>
  @import "./seller.css"

</style>
