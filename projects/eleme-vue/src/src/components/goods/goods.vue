<template>
    <div class="goods">
        <div class="menu-wrap" ref="menu-wrap">
            <ul class="menu">
                <li 
                    v-for="goodsMenu, index in goods"
                    class="menu-item"
                    :key ="index"
                    :class="{'active':currentIndex===index}"
                    @click="selectMenu(index, $event)"
                >
                    <span class="text">{{ goodsMenu.name }}</span>
                </li>
            </ul>
        </div>
        <div class="foods-wrap" ref="foods-wrap">
            <ul class="foods-list">
                <li 
                    v-for="good in goods"
                    class="foods-li vue-foods-hook"
                >
                    <h1 class="title">{{ good.name }}</h1>
                    <ul class="food-list">
                        <li 
                            v-for="food in good.foods"
                            class="food-li"
                            
                        >
                            <div 
                            @click="selectFood(food, $event)"
                            class="icon">
                                <img :src="food.icon" alt="">
                            </div>
                            <div class="content">
                                <h2 class="name">{{ food.name }}</h2>
                                <span v-show="food.description" class="description">{{ food.description }}</span>
                                <div class="extra">
                                    <span>月售{{ food.sellCount }}份</span>
                                    <span>好评率{{ food.rating }}%</span>
                                </div>
                                <div class="price">
                                    <span class="now-price">￥{{ food.price }}</span>
                                    <span v-show="food.oldPrice" class="old-price">￥{{ food.oldPrice }}</span>
                                </div>
                                <div class="cartcontrol-wrap">
                                    <el-cartcontrol
                                        :food="food"
                                    ></el-cartcontrol>
                                </div>
                                
                            </div>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
        <el-shopcart
            :select-foods = "selectedFoods"
            :delivery-price = "seller.deliveryPrice"
            :min-price = "seller.minPrice"
        >
        </el-shopcart>
            <el-food
            :food="selectedFood"
            ref="el-food"
            >
            </el-food>
    </div>

</template>

<script>
    import BScroll from "better-scroll";
    import shopcart from "../shopcart/shopcart.vue";
    import cartControl from "../cartcontrol/cartcontrol.vue";
    import food from "../food/food.vue";
    import __data from "../../data.js";

    export default {
        props: {
            seller: {
                type: Object,
                required: true,
            },

        },
        data(){
            return {
                goods:{},
                listHeight: [],
                scrollY: 0,
                selectedFood: {},
            };
        },
        created(){
            // this.$http.get("http://localhost:8000/api/goods").then((res) => {
            //     this.goods = res.body.data;
            //     this.$nextTick(() => {
            //         this._initScroll();

            //         this._calcheight();

            //     });
            // });
            this.goods = __data.goods;
                this.$nextTick(() => {
                    this._initScroll();

                    this._calcheight();

                });
        },
        methods: {
            _initScroll(){

                this.menuScroll = new BScroll(this.$refs["menu-wrap"], {
                    click: true,
                });
                this.foodsScroll = new BScroll(this.$refs["foods-wrap"], {
                    probeType: 3,
                    click: true,
                });
                this.foodsScroll.on("scroll", (pos) => {
                    this.scrollY = Math.abs( Math.round(pos.y));
                });
            },
            _calcheight(){
                let foodsWrap = this.$refs["foods-wrap"];
                let foodsLi =  foodsWrap.getElementsByClassName("vue-foods-hook");
                let height = 0;
                this.listHeight.push(height)
                for(let item of foodsLi){
                    height += item.clientHeight;
                    this.listHeight.push(height);
                }                
            },
            selectMenu(index, event){
                if(!event._constructed){
                    return 
                }
                let target = this.$refs["foods-wrap"].getElementsByClassName("vue-foods-hook")[index];
                this.foodsScroll.scrollToElement(target, 300);
            },
            selectFood(food, event){
                if(!event._constructed){
                    return;
                }
                this.selectedFood = food;
                this.$refs["el-food"].show();
            },
        },
        computed: {
            currentIndex() {
                for(let i=0; i<this.listHeight.length; i++){
                    let heightTop = this.listHeight[i];
                    let heightBottom = this.listHeight[i + 1];
                    if(!this.listHeight[i+1]){
                        return i
                    } else if (this.scrollY >= heightTop && this.scrollY < heightBottom){
                       return i;
                    }
                }
               
            },
            selectedFoods() {
                let foods = [];
                if(typeof this.goods.forEach == "function"){
                    this.goods.forEach((good) => {
                        good.foods.forEach((food) => {
                            if(food.count) {
                                foods.push(food);
                            };
                        });
                    });
                }
                
                console.log("foods", foods)

                return foods;
            },
        },
        components: {
            "el-shopcart": shopcart,
            "el-cartcontrol": cartControl,
            "el-food": food,
        }
    };
</script>

<style>
    @import "./goods.css";
</style>
