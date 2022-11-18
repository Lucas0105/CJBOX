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
        {{ movie.title}}
      </b-card-text>

  </b-card>
  </div>
</template>

<script>
export default {
    name:'BodyListItem',
    props:{
      movie : Object
    }
}
</script>

<style>
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
</style>