<template>
  <div class="row movie-box">
      <BodyListItem
      v-for="movie in movies" :key="movie.id"
      :movie="movie"
      />
      <div class="overflow-auto">
        <div class="mt-3">
          <b-pagination
            :value="page"
            @input="changePage"
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
      movies:Array,
      rows:Number,
      currentPage:Number
    },
    data() {
      return {
        perPage: 1,
      }
    },
    methods:{
      changePage(page){
        this.$emit('current-page', page)
      },
    },
    computed: {
      page(){
        return this.currentPage ? this.currentPage:1
      }
    }

    
}
</script>

<style  scoped>
.movie-box{
  margin: 0 10% !important;
  margin-top:80px !important;
}
ul{
  justify-content: center;
}
.card-body{
  padding-bottom: 0 !important;
}
</style>