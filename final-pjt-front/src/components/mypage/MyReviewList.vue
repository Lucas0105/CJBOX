<template>
  <div class="d-flex">
    <div @click="goToDetail">
      <img :src="review.movie.poster_path" alt="img" >
      <p>{{ review.movie.title}}</p>
    </div>

    <div>
      <star-rating :rating="review.vote/2" :read-only="true" :increment="0.01" :star-size="20" :show-rating="false"></star-rating>
      <p>
        {{ review.created_at}}
      </p>
      <p>
        {{ review.content}}
      </p>
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

      }
    }
}
</script>

<style scoped>
img{

  height: 100px;
}
.movie-img{
  margin:2.5px;
}
</style>