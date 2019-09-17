import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Logout from './components/logins/Logout.vue'
import AdminPage from './views/Adminpage.vue'
import Firebase from './plugins/FirebaseService.js'
import firebase from "firebase"
import 'firebase/auth'
Vue.use(Router)

// FirebaseService의 getUserAuth를 이용하여 .then으로 promise 해결
// 방문자, 관리자를 리턴 받고 그 값을 user_auth에 담아서 판명하여
// 관리바면 입장, 아니면 홈으로 리다이랙트 하기
var user_auth = ''
var connected_user = ''

var requireAuth = () => (to, from, next) => {
  firebase.auth().onAuthStateChanged(user => {
  if (user) {
    connected_user = user.email;
    Firebase.getUserAuth(connected_user).then(res => {
              user_auth = res
            }).then (res=>{
              if (user_auth === '관리자') {
                return next();
              }
              next('/');
            })
  } else {
    // No user is signed in.
    next('/')
  }
})
}

var requireLogin = () => (to, from, next) => {
  firebase.auth().onAuthStateChanged(user => {
    if (user) {
      next();
    }
    else {
      next('/')
    }
   })
}





export default new Router({

  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminPage,
      // admin page 권한 관리자일때만 들어가기
      beforeEnter: requireAuth()
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },

    {
      path : '/myPage',
      name : 'myPage',
      component: () => import('./views/MyPage.vue'),
      beforeEnter: requireLogin()
    },
    {
      path:'/conference/:id',
      name:'conference_detail',
      component: () => import('./views/ConferenceDetail.vue')
    },

    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    }


  ]
})
