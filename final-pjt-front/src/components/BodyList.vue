<template>
  <div class="row movie-box">
      <BodyListItem
      v-for="movie in movies" :key="movie.id"
      :movie="movie"
      />

      <div class="overflow-auto">
        <div class="mt-3">
          <b-pagination
            v-model="currentPage"
            pills
            :total-rows="rows"
            :per-page="perPage"
            first-number
          ></b-pagination>
        </div>
      </div>
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
    },
    data() {
      return {
        rows: 10,
        perPage: 1,
        currentPage: 1
      }
    },
    watch:{
      currentPage:{
        handler:'changePage'
      }
    },
    methods:{
      changePage(){
        this.$emit('current-page', this.currentPage)
      }
    },

    
}
</script>

<style  scoped>
.movie-box{
  margin: 0 10% !important;
  margin-top:150px !important;
}
ul{
  justify-content: center;
}

</style>