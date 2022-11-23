<template>
<div  class="col-6 col-lg-3 col-xxl-2 movie-card" >
    <b-card :img-src="movie.poster_path" img-alt="Image" img-top @click="goToDetail"> 
    <b-card-text>
    {{ movie.title }}
    ★★★★★ {{ movie.vote_average}}({{movie.vote_count}})
    </b-card-text>
    </b-card>
    <div class="love-box">
        <small><b-icon icon="heart-fill"  class="loved" @click="addMyList"></b-icon><span class="cnt" @click="addMyList">좋아요 취소</span></small>
    </div>
</div>

</template>

<script>

export default {
    name:'MyList',
    data(){
        return{
            res_mylist :null
        }
    },
    props:{
        movie:Object,
    },
    methods:{
      goToDetail(){
        this.$router.push({name:'detail', params:{id: this.movie.id}})
      },
      addMyList(){
        this.$store.dispatch('user/addMyList', this.movie.id)
      }
    },

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
.card-body{
    padding-bottom:0;
    border-bottom:solid 1px #a0a0a0 
}
.cnt{
    font-weight: bold;
}
img{
    border-radius:10px
}
.love-box{
    cursor: pointer
}

</style>