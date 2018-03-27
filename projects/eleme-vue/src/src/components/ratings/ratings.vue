<template>
    <div class="ratings" ref="el-ratings">
        <div class="ratings-content">
            <div class="overview">
                <div class="left">
                    <h1 class="score">{{ seller.score }}</h1>
                    <div class="title">综合评分</div>
                    <div class="rank">高于周边商家{{seller.rankRate}}%</div>
                </div>
                <div class="right">
                    <div class="score-wrap">
                        <span class="title">服务态度</span>
                        <el-star
                        :size="36"
                        :score="seller.serviceScore"
                        ></el-star>
                        <span class="score">{{ seller.serviceScore }}</span>
                    </div>
                    <div class="score-wrap">
                        <span class="title">商品评分</span>
                        <el-star
                        :size="36"
                        :score="seller.foodScore"
                        ></el-star>
                        <span class="score">{{ seller.foodScore }}</span>
                    </div>
                    <div class="delivery-time">
                        <span class="title">送达时间</span>
                        <span class="time">{{ seller.deliveryTime }}分钟</span>
                    </div>
                </div>
            </div>
            <el-split></el-split>
            <el-rating-select
            @typeOrContent="changeTypeOrContent"
            :select-type="selectType"
            :only-content="onlyContent"
            :desc="desc"
            :ratings="ratings"
            ></el-rating-select>
            <div class="rating-wrap">
                <ul>
                    <li 
                    v-for="rating in ratings"
                    class="rating-item"
                    >
                        <div class="avatar">
                            <img width="28" height="28" :src="rating.avatar" alt="">
                        </div>
                        <div class="content">
                            <h1 class="name">{{ rating.username }}</h1>
                            <div class="star-wrap">
                                <el-star
                                :size="24"
                                :score="rating.score"
                                ></el-star>
                                <span 
                                v-show="rating.deliveryTime"
                                class="delivery-time"
                                >{{ rating.deliveryTime }}</span>
                            </div>
                            <div class="text">{{ rating.text }}</div>
                            <div 
                            v-show="rating.recommend && rating.recommend.length !== 0"
                            class="recommend"
                            >
                            <span class="icon icon-thumb_up icon"></span>
                            <span class="item" v-for="item in rating.recommend">{{ item }}</span>
                            </div>
                            <div class="time">{{ rating.rateTime | formatDate }}</div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    import star from "../star/star.vue"
    import BScroll from "better-scroll";
    import split from "../split/split.vue";
    import ratingSelect from "../ratingselect/ratingselect.vue"
    import __data from "../../data.js";

const POSITIVE = 0;
const NEGATIVE = 1;
const ALL = 2;
    export default {
        data(){
            return {
                ratings: [],
                showFlag: false,
                selectType: ALL,
                onlyContent: true,
                desc: {
                    all: "全部",
                    positive: "满意",
                    negative: "不满意",
                },
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
            "el-rating-select": ratingSelect,
        },
        created(){
            // this.$http.get("http://localhost:8000/api/ratings")
            // .then((res) => {
            //     this.ratings = res.body.data;
            //     console.log("ratings:", this.ratings);
            // })

            this.ratings = __data.ratings;
            this.$nextTick(() => {
                this.scroll = new BScroll(this.$refs["el-ratings"], {
                    click: true,
                });
            });
        },
        filters: {
            formatDate(time) {
                let date = new Date(time);
                return date.toLocaleString();
            }
        },
        methods: {
            changeTypeOrContent(type, content, event){
                this.onlyContent = content;
                this.selectType = type;
            },
        }
        
    };
</script>

<style>
    @import "./ratings.css";

</style>
