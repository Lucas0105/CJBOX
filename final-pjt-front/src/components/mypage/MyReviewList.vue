<template>
  <div class="d-flex review-out-box mx-auto mt-2">
    <div class="d-flex review-box mx-auto">
      <div @click="goToDetail" >
        <img :src="review.movie.poster_path" alt="img" >
      </div>  
      <div style="width:80%" class="mx-auto">
        <h5>{{ review.movie.title}}</h5>
        <div class="d-flex">
            <star-rating :rating="review.vote/2" :read-only="true" :increment="0.01" :star-size="20" :show-rating="false"></star-rating>
          </div>
        <p>
          {{ review.created_at}}
        </p>
        <p>
          {{ review.content}}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
    name:'MyReviewList',
    components:{
      StarRating
    },
    props:{
      review:Object
    },
    methods:{
      goToDetail(){
        this.$router.push({name:'detail', params:{id: this.review.movie.id}})
        this.$router.go(this.$router.currentRoute)
      }
    }
}
</script>

<style scoped>
.review-box{
  width:80%
}
.review-out-box{
  height:12.5em;
  padding:1%;
  width:90%;
  background-color:#17223b;
  border-radius: 10px;
}
img{
  height: 100% 
}
.movie-img{
  margin:2.5px;
}

h5{
  margin:0
}

</style>
