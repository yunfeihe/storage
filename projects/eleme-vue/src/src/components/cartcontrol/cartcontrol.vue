<template>
    <div 
        class="cart-control"
    >
        <div 
            v-show="food.count>0"
            class="cart-minus icon-remove_circle_outline"
            @click="minus"
        ></div>
        <div 
            v-show="food.count>0"
            class="cart-count"
        
        >{{ food.count }}</div>
        <div 
            class="cart-plus icon-add_circle"
            @click="plus"
        ></div>
    </div>
</template>

<script>
    import Vue from "vue";
    export default {
       props: {
           food: {
               type: Object,
           },
       },
       created() {

       },
       methods: {
           plus(e){
               if(!e._constructed){
                   return;
               }
               console.log("plus");
               if(!this.food.count) {
                   Vue.set(this.food, "count", 1);
               } else {
                   this.food.count += 1;
               }
           },
           minus(e){
               if(!e._constructed){
                   return;
               }
               this.food.count -= 1;

           },
       },
    };
</script>

<style>
    @import "./cartcontrol.css";
</style>
