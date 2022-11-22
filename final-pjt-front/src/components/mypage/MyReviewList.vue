<template>
  <div class="d-flex">
    <div @click="goToDetail">
      <img :src="review.movie.poster_path" alt="img" >
      <p>{{ review.movie.title}}</p>
    </div>

    <div>
      <p>★★★★  {{review.vote}}</p>
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
export default {
    name:'MyReviewList',
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