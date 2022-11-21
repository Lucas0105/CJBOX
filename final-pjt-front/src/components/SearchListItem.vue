<template>
  <div class="col-2">
    <b-card
        :img-src="movie.poster_path"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 13rem;"
        class="mb-2 border-0 mx-auto"
        @click="toDetail"
      >
        <b-card-text >
          <span>
            {{movie.title}}
          </span>
        </b-card-text>

      </b-card>
  </div>
</template>

<script>
export default {
    name:'SearchListItem',
    data(){
        return{

        }
    },
    props:{
        movie:Object
    },
    methods:{
      toDetail() {
        this.$router.push({name:'detail', params:{id: this.movie.id}})
        this.$store.commit('movie/RESET_SEARCH')
      },
  
    }
}
</script>

<style scoped>
.card-body{
  background-color: #17223b !important;
}
</style>