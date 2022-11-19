<template>
  <div class="col-4 movie-card">
       <b-card
        :img-src="movie.poster_path"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 15rem;"
        class="mb-2 border-0"
      >
        <b-card-text >
          <span :title="movie.title">{{ movie.title | resize }}</span><br>
          <div class="bottom-icon d-flex justify-content-between">
            <div>
                <small><b-icon icon="heart"  class="loved"></b-icon></small>
            </div>
            <div>
              <small> 
                <b-icon icon="star-fill" class="star"></b-icon>
                <span class="star-text"> {{ movie.vote_average}}</span> ({{ movie.vote_count }})
              </small>
              
            </div>
          </div>
        </b-card-text>

      </b-card>

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
        if(value.length > 15){
          value = value.slice(0,13) + '...'
          return value
        }else{
          return value
        }
      }
    }
}
</script>

<style>
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

</style>