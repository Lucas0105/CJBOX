<template>
  <div class="search-page">
    <form @submit.prevent="searchSubmit">
      <label class="d-flex justify-content-between mx-auto">
        <input type="text" class="search-input" placeholder="영화 검색" :value="searchInput" @input="searchSubmit" @keydown="searchSubmit">
      <p class="h1 my-auto"><b-icon icon="search" title="검색" type="submit" ></b-icon></p>  
      </label>
    </form>
    <div class="result">
      {{searchResult}}
      <p>{{ searchInput }}</p>
    </div>

  </div>
</template>

<script>
export default {
  name:'SearchView',
  data(){
    return{
      searchInput:null
    }
  },
  computed:{
    searchResult() {
      return this.$store.state.movie.searchResult
    }
  },
  methods:{

    searchSubmit(e) {
      this.searchInput = e.target.value 
      console.log(this.searchInput)
      this.$store.dispatch('movie/searchSubmit', this.searchInput)
    },
  },

}
</script>

<style scoped>

.search-page{
  background-color: #17223b;
  height: 100vh;
  color: aliceblue;
}
.search-input{
  width: 90%;
  border:0;
  background: transparent;
  border: solid 1px red;
  color:aliceblue;
  font-size: 1.5em;

}
label{
  width:80%;  
  height: 70px;
  border-bottom: solid 1px white;
}
input::placeholder{
  color:aliceblue;
  opacity: 0.4;
}


.b-icon{
  color:white
}
</style>