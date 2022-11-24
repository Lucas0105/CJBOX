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
      page:Number
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


</style>