<template>
  <div 
  v-show="showFlag"
  class="food"
  ref="el-food"
  >
    <div class="food-content">
        <div class="image-header">
            <img :src="food.image" alt="">
            <div class="back" @click="hide"><i class="icon-arrow_lift"></i></div>
        </div>
        <div class="content">
            <h1 class="title">{{ food.name }}</h1>
            <div class="detail">
                <span class="sell-count">月售{{ food.sellCount }}份</span>
                <span class="rating">好评率{{ food.rating }}%</span>
            </div>
            <div class="price">
                <span class="now">￥{{ food.price }}</span>
                <span class="old" v-show="food.oldPrice">￥{{ food.oldPrice }}</span>
            </div>
            <div class="cartcontrol-wrap">
                <el-cartcontrol
                :food="food"
                ></el-cartcontrol>
            </div>
            <div class="buy" 
            @click="addFirst(food, $event)"
            v-show="!food.count || food.count ===0"
            >加入购物车</div>
        </div>
        <el-split v-show="food.info"></el-split>
        <div class="info" v-show="food.info">
            <h1 class="title">商品信息</h1>
            <span class="text">{{ food.info }}</span>
        </div>
        <el-split></el-split>
        <div class="rating">
            <h1 class="title">商品评价</h1>
            <el-rating-select
            :select-type="selectType"
            :only-content="onlyContent"
            :desc="desc"
            :ratings="food.ratings"
            @typeOrContent="changeTypeOrContent"
            ></el-rating-select>
        </div>
        <div class="rating-wrap">
        
            <ul 
            v-show="food.ratings && food.ratings.length"
            
            >
                <li
                v-show="isNeedShow(rating.rateType, rating.text)"
                v-for="rating in food.ratings"
                class="rating-item"
                >   
                    <div class="user">
                        <span class="name">{{ rating.username }}</span>
                        <img :src="rating.avatar" alt="" class="avatar" width="12" height="12">
                    </div>
                    <div class="time">{{ rating.rateTime | formatDate }}</div>
                    <span class="text">
                        <span
                        class="icon"
                        :class="{'icon-thumb_up':rating.rateType===0,
                                 'icon-thumb_down': rating.rateType===1,
                                }"
                        ></span>
                        {{ rating.text }}
                    </span>
                </li>    
            </ul>
            <div 
            v-show="!food.ratings || !food.ratings.length"
            class="no-rating">暂无评价</div>
        </div>
    </div>
  </div>
</template>

<script>
import BScroll from "better-scroll";
import cartControl from "../cartcontrol/cartcontrol";
import Vue from "vue";
import split from "../split/split.vue";
import ratingSelect from "../ratingselect/ratingselect.vue";

const ALL = 2;

export default {
    data(){
        return {
            showFlag: false,
            selectType: ALL,
            onlyContent: true,
            desc: {
                all: "全部",
                positive: "推荐",
                negative: "吐槽",
            },
        };
    },
    props: {
        food: {
            type: Object,
        },
    },
    methods: {
        show(){
            this.showFlag = true;
            this.selectType = ALL;
            this.onlyContent = true;
            this.$nextTick(() => {
                if(!this.scroll) {
                    this.scroll = new BScroll(this.$refs["el-food"], {
                        click: true,
                    });
                } else {
                    this.scroll.refresh();
                }
            });
        },
        isNeedShow(type, text){
            if(this.onlyContent && !text){
                return false;
            }
            if(this.selectType === ALL){
                return true;
            } else {
                return type === this.selectType;
            }
        },
        hide(){
            this.showFlag = false;
        },
        addFirst(food, event){
            if(!event._constructed){
                return;
            }
            if(food.count){
                food.count += 1;
            } else {
                Vue.set(food, "count", 1);
            }
        },
        changeTypeOrContent(type, content, event){
            console.log("* args", arguments);

            this.onlyContent = content;
            this.selectType = type;
            this.$nextTick(() => {
                this.scroll.refresh();
            });
        },
    },
    filters: {
        formatDate(time) {
            let date = new Date(time);
            return date.toLocaleString();
        }
    },
    components: {
        "el-cartcontrol": cartControl,
        "el-split": split,
        "el-rating-select": ratingSelect,
    }

}
</script>

<style>
@import "./food.css";
</style>

