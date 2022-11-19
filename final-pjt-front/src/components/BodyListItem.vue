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
        <b-card-text :title="movie.title">
          {{ movie.title | resize }}<br>
          <b-icon icon="star-fill" class="star"></b-icon>
          {{ movie.vote_average}} ({{ movie.vote_count }})
        </b-card-text>

        <b-icon variant="warning" icon="star" class="loved" scale="1.5" ></b-icon>
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
.movie-card{
  position: relative;
}
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
  /* color:yellow; */
  position:absolute;
  top:15px;
  left:15px;

}

.star{
  color:rgba(236, 0, 0, 0.603);  
}
</style>