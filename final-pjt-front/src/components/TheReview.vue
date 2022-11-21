<template>
  <div class="review-page">
    <hr>
    <h2>감상평</h2>
    <div class="review-box mx-auto" >
      <div class="review-form mx-auto">
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
      <!-- pagination -->
      <div class="overflow-auto">
        <div class="mt-3">
          <b-pagination
            v-model="currentPage"
            pills
            :total-rows="rows"
            :per-page="perPage"
            first-number
          ></b-pagination>
        </div>
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
        rows:10,
        currentPage:1,
        perPage:1

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
  opacity: 0.8;
}

ul{
  justify-content: center;
}
</style>