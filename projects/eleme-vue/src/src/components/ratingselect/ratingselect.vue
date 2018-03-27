<template>
    <div class="rating-select">
        <div class="rating-type">
            <span
            @click="select(2, $event)" 
            :class="{active:selectType===2}"
            class="block positive">{{ desc.all }}<span class="count">{{ ratings.length }}</span></span>
            <span 
            @click="select(0, $event)" 
            :class="{active:selectType===0}"
            class="block positive">{{ desc.positive }}<span class="count">{{ positives.length }}</span></span>
            <span 
            @click="select(1, $event)" 
            :class="{active:selectType===1}"
            class="block negative">{{ desc.negative }}<span class="count">{{ negatives.length }}</span></span>
        </div>
        <div 
        @click="toggleContent"
        :class="{on:onlyContent}"
        class="swich">
            <span class="icon-check_circle icon"></span>
            <span class="text">只看有内容的评价</span>
        </div>
    </div>
</template>

<script>
const POSITIVE = 0;
const NEGATIVE = 1;
const ALL = 2;
export default {
  data(){
      return {
      };
  },
  props: {
      ratings: {
          type: Array,
          default(){
              return []
          },
      },
      selectType: {
          type: Number,
          default: ALL,
      },
      onlyContent: {
          type: Boolean,
          default: false,
      },
      desc: {
          type: Object,
          default(){
              return {
                  all: "全部",
                  positive: "满意",
                  negative: "不满意",
              }
          },
      }
  },
  methods: {
      select(type, event){
          if(!event._constructed){
              return;
          }
          this.selectType = type;
          this.$emit("typeOrContent", type, this.onlyContent, this.$event);
      },
      toggleContent(){
          if(!event._constructed){
              return;
          }
          this.onlyContent = !this.onlyContent;
          this.$emit("typeOrContent", this.selectType, this.onlyContent, this.$event);
      },
  },
  computed: {
      positives(){
          return this.ratings.filter((rating) => {
              return rating.type === POSITIVE;
          });
      },
      negatives(){
          return this.ratings.filter((rating) => {
              return rating.type === NEGATIVE;
          });
      },
      type:{
          get(){
            let type = this._type;
            return type;
          },
          set(value){
              this._type = value;
          },

      },
      isOnlyContent:{
          get(){
              let flag = this._isOnlyContent;
              return flag;
          },
          set(value) {
              this._isOnlyContent = value;
          }
          
      },
  }
}
</script>

<style>
.rating-select {
    
}
.rating-select .rating-type {
    padding: 18px 0;
    margin: 0 18px;
    border-bottom: 1px solid rgba(7, 17, 27, 0.1);
    font-size: 0;
}
.rating-select .rating-type .block {
    display: inline-block;
    padding: 8px 12px;
    margin-right: 8px;
    border-radius: 1px;
    color: rgb(77, 85, 93);
    font-size: 8px;
    line-height: 12px;
}
.rating-select .rating-type .block .count {
    font-size: 8px;
    margin-left: 2px;
}

.rating-select .rating-type .block.active {
    color: white;
}

.rating-select .rating-type .block.positive {
    background-color: rgba(0, 160, 220, 0.2);
}

.rating-select .rating-type .block.positive.active {
    background-color: rgba(0, 160, 220, 1);
}

.rating-select .rating-type .block.negative {
    background-color: rgba(77, 85, 93, 0.2);
}
.rating-select .rating-type .block.negative.active {
    background-color: rgba(77, 85, 93, 1);
}
.swich {
    padding: 12px 0px;
    margin: 0 18px;
    line-height: 24px;
    border-bottom: 1px solid rgba(7, 71, 27, 0.1);
    color: rgb(147, 153, 159);
}
.swich .icon {
    margin-right: 4px;
    font-size: 24px;
    display: inline-block;
    
}
.swich.on .icon {
    color: #00c580;
    
}
.swich .text {
    display: inline-block;
    font-size: 12px;
    vertical-align: top;
}
</style>
