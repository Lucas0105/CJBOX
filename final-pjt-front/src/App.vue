<template>
  <div id="app">

    <nav class="navbar navbar-expand-lg" >
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{name:'movies'}"><img src="@/assets/CJBOX_logo2-2.gif" width="60px" alt=""></router-link>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav ">
            <b-nav-item-dropdown text="장르" right  >
              <b-dropdown-item v-for="(genre, index) in genres" :key="index"><router-link :to="{ name: 'genre', params: {category: genre} }" >{{ genre }}</router-link></b-dropdown-item>
            </b-nav-item-dropdown>
            <div class="d-flex">
              <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'search'}"><b-icon icon="search"></b-icon></router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" :to="{name:'login'}"><b-icon icon="box-arrow-in-right"></b-icon></router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" :to="{name:'signup'}"><b-icon icon="person-plus"></b-icon></router-link>
              </li>
            </div>
          </ul>
        </div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
    </nav>
    <router-view></router-view>
    </div>
  
</template>

<script>
export default {
  computed:{
    genres(){
      return this.$store.state.movie.genre_list
    }
  }
}
</script>
<style>
.navbar{
  background-color: rgba(57, 66, 86, 0.5);
  padding: 0 !important;
  height: 80px;
  z-index: 1;
}
.nav-link{
  color:#EEEEEE !important
}
.navbar-brand{
  padding-top: 0 !important;
  padding-bottom: 0 !important
}
p{
  color:#EEEEEE 
}

</style>
