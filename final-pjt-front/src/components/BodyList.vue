<template>
  <div class="row movie-box">
      <BodyListItem
      v-for="movie in movies" :key="movie.id"
      :movie="movie"
      />
  </div>
</template>

<script>
import BodyListItem from '@/components/BodyListItem'

export default {
    name:'BodyList',
    components:{
      BodyListItem
    },
    props:{
      movies:Array
    }
}
</script>

<style>
.movie-box{
  margin: 0 10% !important;
  margin-top:150px !important;
}
</style>