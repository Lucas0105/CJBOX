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
  </div>
</template>

<script>
import ReviewForm from "@/components/ReviewForm"
export default {
    name:'TheReview',
    components:{
      ReviewForm
    },
    props:{
      movie:Object
    }
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