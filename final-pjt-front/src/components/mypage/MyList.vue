<template>
<div  class="col-6 col-lg-3 col-xxl-2 movie-card" @click="goToDetail">
    <b-card :img-src="movie.poster_path" img-alt="Image" img-top >
    <b-card-text>
    {{ movie.title }}
    ★★★★★ {{ movie.vote_average}}({{movie.vote_count}})
    </b-card-text>
    <template #footer>
    <small ><b-icon icon="heart-fill"  class="loved"></b-icon><span class="cnt">{{movie.like_users[0]}}</span></small>
    </template>
</b-card>
</div>

</template>

<script>
export default {
    name:'MyList',
    props:{
        movie:Object
    },
    methods:{
      goToDetail(){
        this.$router.push({name:'detail', params:{id: this.movie.id}})
      }
    }
}
</script>

<style scoped>
.card{
   margin:auto !important;
  --bs-card-bg: none;
  transition: all 0.2s linear;
  cursor: pointer;
}
.loved{
    color: red;
}
.card-footer{
    border-top:solid 1px #a0a0a0 
}
.cnt{
    font-weight: bold;
}
img{
    border-radius:10px
}


</style>