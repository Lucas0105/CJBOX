<template>
  <div class="review-page">
    <hr>
    <div class="review-box mx-auto" >
      <div class="review-form mx-auto">
        <ReviewForm
        :movie="movie"
        />
      </div>
      <div class="review-list mx-auto">
          <div class="mx-auto" style="width:90%;">
           <h4>관람평</h4>

            <div class="svg-item">
            <svg width="100%" height="100%" viewBox="0 0 40 40" class="donut">
              <circle class="donut-hole" cx="20" cy="20" r="15.91549430918954" fill="#fff"></circle>
              <circle class="donut-ring" cx="20" cy="20" r="15.91549430918954" fill="transparent" stroke-width="3.5"></circle>
              <circle class="donut-segment" cx="20" cy="20" r="15.91549430918954" fill="transparent" stroke-width="3.5" :stroke-dasharray="sentiment+' '+ (100-sentiment)" stroke-dashoffset="25"></circle>
              <g class="donut-text">

                <text y="50%" transform="translate(0, 2)">
                  <tspan x="50%" text-anchor="middle" class="donut-percent">{{ sentiment }}</tspan>   
                </text>
              </g>
            </svg>
          </div>

          </div>
          <div v-if="reviews?.length===0" style="text-align:center; height:50%">
              <h5>관람평이 없습니다.</h5>
          </div>
          <ReviewListItem
          v-for="review in reviews"
          :key="review.id"
          :review="review"
          :page="page"
          />
      </div>
      
    </div>
  </div>
</template>

<script>
import ReviewForm from "@/components/ReviewForm"
import ReviewListItem from "@/components/ReviewListItem"

export default {
    name:'TheReview',
    data() {
      return{

      }
    },
    computed:{

    },
    components:{
      ReviewForm,
      ReviewListItem
    },
    props:{
      movie:Object,
      reviews:Array,
      page:Number,
      sentiment:Number
    },
    methods:{
     
    },



}
</script>

<style scoped>
.review-page{
  color: aliceblue;
  width: 100%;
}

.review-box{
  width:80%;
  /* opacity: 0.8; */
}

@keyframes donut-chart-fill {
  to { stroke-dasharray: 0 100; }
}
body {
  font-size: 16px;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #333;  
}

.svg-item {
  width: 200px;
  height: 200px;
  font-size: 16px;
}
.donut-ring {
  stroke: #EBEBEB;
}

.donut-segment {
  animation: donut-chart-fill 1s reverse ease-in;
  transform-origin: center;
  stroke: #FF6200;
}

.donut-text {
  font-family: Arial, Helvetica, sans-serif;
  fill: #FF6200;
}

.donut-label {
  font-size: 0.28em;
  font-weight: 700;
  line-height: 1;
  fill: #000;
  transform: translateY(0.25em);    
}

.donut-percent {
  font-size: 0.5em;
  fill: #FF6200;
  line-height: 1;
  transform: translateY(0.5em);
}


</style>