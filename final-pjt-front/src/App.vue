<template>
  <div id="app">

    <nav class="navbar navbar-expand-lg" >
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{name:'movies'}"><img src="@/assets/CJBOX_logo2-2.gif" width="60px" alt=""></router-link>
          <ul class="navbar-nav">
            <b-nav-item-dropdown class="mx-2" text="장르">
              <b-dropdown-item v-for="(genre, index) in genres" :key="index"><router-link :to="{ name: 'genre', params: {category: genre} }" >{{ genre }}</router-link></b-dropdown-item>
            </b-nav-item-dropdown>
            <div class="d-flex">
              <li class="nav-item mx-1">
                <router-link class="nav-link" :to="{ name: 'search'}"><b-icon icon="search" title="검색"></b-icon></router-link>
              </li>
              <li class="nav-item mx-1">
                <router-link class="nav-link" :to="{name:'login'}"><b-icon icon="box-arrow-in-right" title="로그인"></b-icon></router-link>
              </li>
              <li class="nav-item mx-1">
                <router-link class="nav-link" :to="{name:'signup'}"><b-icon icon="person-plus" title="회원가입"></b-icon></router-link>
              </li>
            </div>
          </ul>
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

</style>
