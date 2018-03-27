<template>
    <div class="shop-cart">
        <div class="content">
            <div class="content-left"  @click="toggleList">
                <div class="logo-wrap">
                    <div 
                        class="logo"
                        :class = "{'highlight': totalCount}"
                    ><span class="icon-shopping_cart"></span></div>
                    <div 
                        class="num"
                        v-show="totalCount > 0"
                    >{{ totalCount }}</div>
                </div>
                <div 
                    class="price"
                    :class = "{'highlight': totalCount}"
                >￥{{ totalPrice }}</div>
                <div class="description">另需配送费￥{{ deliveryPrice }}元</div>

            </div>
            <div class="content-right">
                <div 
                    class="pay"
                    :class="{enough: minPrice-totalPrice <= 0}"
                >{{ payDescription }}</div>
            </div>
        </div>
        <div 
            v-show="listShow"
            class="shop-cart-list">
            <div class="list-header">
                <h1 class="title">购物车</h1>
                <span 
                @click="empty"
                class="empty">清空</span>
            </div>
            <div 
            class="list-content"
            ref="cart-control-wrap"
            >
                <ul>
                    <li
                    v-for="food of selectFoods"
                    class="food"
                    >
                        <span class="name">{{ food.name }}</span>
                        <div class="price">
                            <span><span class="money-icon">￥</span>{{ food.price * food.count }}</span>
                        </div>
                        <div 
                        class="cartcontrol-wrap" 
                        
                        >
                            <el-cart-control
                                :food="food"
                                
                            >

                            </el-cart-control>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        <div class="list-mask"
        v-show="listShow"
        
        ></div>
    </div>
</template>

<script>
    import BScroll from "better-scroll";
    import cartControl from "../cartcontrol/cartcontrol.vue";
    export default {
        data(){
            return {
                isFold: false,
            };
        },
        props: {
            "selectFoods": {
                type: Array,
                default() {
                    return [
                        {
                            price: 10,
                            count: 2,
                        },
                    ];
                }
            },
            deliveryPrice: {
                type: Number,
            },
            minPrice: {
                type: Number,
            },
        },
        computed: {
            totalPrice() {
                let total = 0;
                for(let food of this.selectFoods){
                    total += food.price * food.count;
                }
                return total;
            },
            totalCount() {
                let count = 0;
                for(let food of this.selectFoods){
                    count += food.count;
                }
                return count;
            },
            payDescription() {
                if(this.totalPrice === 0){
                    return `￥${this.minPrice}起送`;
                } else if (this.totalPrice < this.minPrice) {
                    let diff = this.minPrice - this.totalPrice
                    return `还差￥${diff}元起送`;
                } else {
                    return "请结算"; 
                }
            },
            listShow(){
                if(!this.totalCount){
                    this.isFold = true;
                    return false;
                }
                let isShow = !this.isFold;
                if (isShow) {
                    this.$nextTick(() => {
                        if(!this.scroll){
                            console.log("***", this.$refs["cart-control-wrap"]);
                            let cartControlEl = this.$refs["cart-control-wrap"];
                            this.scroll = new BScroll(cartControlEl, {
                                click: true,
                            });
                        } else {
                            this.scroll.refresh();
                        }
                        
                    });  
                }
                return isShow;
            },
        },
        components: {
            "el-cart-control": cartControl,
        },
        methods: {
            toggleList(){
                console.log("toggle");
                if(!this.totalCount){
                    return;
                }
                this.isFold = !this.isFold;
            },
            empty(){
                this.selectFoods.map((food) => {
                    food.count = 0;
                });
            },
        },

    };
</script>

<style>
    @import "./shopcart.css";
</style>
