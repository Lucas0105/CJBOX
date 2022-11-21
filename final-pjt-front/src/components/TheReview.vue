<template>
  <div class="review-page">
    <hr>
    <h2>영화리뷰</h2>
    <div class="review-box mx-auto">
      <h1 style="white">review</h1>
      <ReviewForm
      :movie="movie"
      />
    </div>
    <div class="review-list mx-auto">
      <ReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
      />
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
      reviews:Array
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
  border:solid 1px red;
  opacity: 0.8;
}
</style>