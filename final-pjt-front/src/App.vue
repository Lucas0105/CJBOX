<template>
  <div id="app">

    <nav class="navbar navbar-expand-lg" >
      <div class="container-fluid">
        <router-link class="navbar-brand" to='/movies'><img src="@/assets/CJBOX_logo2-2.gif" width="60px" alt=""></router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <b-nav-item-dropdown text="장르" right>
              <b-dropdown-item href="#">EN</b-dropdown-item>
              <b-dropdown-item href="#">ES</b-dropdown-item>
              <b-dropdown-item href="#">RU</b-dropdown-item>
              <b-dropdown-item href="#">FA</b-dropdown-item>
            </b-nav-item-dropdown>
            <!-- <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li> -->
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'search'}">검색</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to='/accounts/login'>로그인</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to='/accounts/signup'>회원가입</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view></router-view>
    </div>
  
</template>

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
