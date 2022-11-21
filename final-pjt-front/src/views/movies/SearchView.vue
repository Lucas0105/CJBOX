<template>
<div class="search-main-view">
  <div id="search-page">
    <form @submit.prevent="searchSubmit" class="input-form">
      <label class="d-flex justify-content-between mx-auto">
        <input type="text" class="search-input" placeholder="영화 검색" :value="searchInput" @input="searchSubmit" @keydown="searchSubmit">
      <p class="h1 my-auto"><b-icon icon="search" title="검색" type="submit" ></b-icon></p>  
      </label>
    </form>
    <div class="search-box">
      <SearchList
      :movies="searchResult"
      />
    </div>
  </div>

</div>

</template>

<script>
import SearchList from '@/components/SearchList'

export default {
  name:'SearchView',
  data(){
    return{
      searchInput:null
    }
  },
  components:{
    SearchList
  },
  computed:{
    searchResult() {
      return this.$store.getters['movie/searchResult']
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
.search-main-view{
  height: 100vh;
  background-color: #17223b;


}
#search-page{
  background-color: #17223b;
  color: aliceblue;
  position: relative;
  top: -80px;
}
.search-input{
  width: 90%;
  border:0;
  background: transparent;
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

.input-form{
  padding-top:100px;
}
.b-icon{
  color:white
}
</style>