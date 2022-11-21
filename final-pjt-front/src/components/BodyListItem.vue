<template>
  <div class="col-6 col-lg-3 col-xxl-2 movie-card">
       <b-card
        :img-src="movie.poster_path"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 15rem;"
        class="mb-2 border-0"
        @click="toDetail"
      >
        <b-card-text >
          <span :title="movie.title">
            {{ movie.title | resize }}
          </span><br>
          
        </b-card-text>

      </b-card>
      <div class="bottom-icon d-flex justify-content-between mx-auto mb-2" >
        <div>
            <b-icon icon="heart"  class="loved"></b-icon>
        </div>
        <div>
          <small> 
            <b-icon icon="star-fill" class="star"></b-icon>
            <span class="star-text"> {{ movie.vote_average}}</span> 
            <span> ({{ movie.vote_count }})</span>
          </small>
          
        </div>
      </div>
  </div>
</template>

<script>
export default {
    name:'BodyListItem',
    props:{
      movie : Object
    },
    filters:{
      resize(value){
        if(value.length >= 11){
          value = value.slice(0,7) + '...'
          return value
        }else{
          return value
        }
      }
    },
    methods:{
      toDetail() {
        this.$router.push({name:'detail', params:{id: this.movie.id}})
      }
    }
}
</script>

<style scoped>
/* .movie-card{
} */
.card{
  margin:auto !important;
}
.card-body{
  background-color: #17223b !important;
}
.card-text{
  color:aliceblue  !important;
  font-size:15px;
}
.card-img-top{
  height:300px !important;
}

.loved{
  color:gray
}
.star, .star-text{
  color:#FFD400
}
.bottom-icon{
  max-width: 15rem;
  padding-left: 1em;
  padding-right: 1em;
  padding-bottom: 1em;
}
span{
  color:aliceblue
}
.card-body{
  padding-bottom: 0 !important;
}
</style>