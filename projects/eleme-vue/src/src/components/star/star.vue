<template>
  <div class="star" :class="starType">
    <span 
          v-for="(itemClass, index) in itemClasses" 
          :class="itemClass"
          :key="index" 
          class="star-item">
    </span>
  </div>
</template>



<script>
// import header from "./components/header/header";
export default {
  props:{
      size: {
          type: Number,
      },
      score: {
          type: Number,
      },
  },
  computed: {
      starType(){
          return "star-" + this.size;
      },
      itemClasses(){
          let classes = [];
          const numOfStar = 5;
          let numOfOnStar = Math.floor(this.score);
          let hasHalfStar = this.score % 1 !== 0 ? true : false;
          let numOfOffStar = 0;
        console.log("this.score", this.score)

          for(let i=0; i<numOfOnStar; i++){
              classes.push("on");
          }
          if(hasHalfStar) {
              classes.push("half");
          }
          while (this.scroe + numOfOffStar <= 4){
              numOfOffStar += 1;
              classes.push("off");
          }
          console.log("classes", classes)
          return classes;
      },
  },
}
</script>

<style>
    @import "./star.css";
</style>
