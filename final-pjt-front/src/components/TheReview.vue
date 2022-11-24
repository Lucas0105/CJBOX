<template>
  <div class="review-page">
    <hr>
    <div class="review-box mx-auto" >
      <div class="review-form mx-auto">
        <ReviewForm
        :movie="movie"
        :sentiment="sentiment"
        />
      </div>
      <div class="review-list mx-auto">
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

</style>