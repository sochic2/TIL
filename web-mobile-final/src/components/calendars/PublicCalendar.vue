<template>
  <v-layout wrap>
    <!-- Controller -->
    <v-flex sm4 class="text-sm-left text-xs-center">
      <v-btn large @click="$refs.calendar.prev()">
        <v-icon dark left>keyboard_arrow_left</v-icon>Prev
      </v-btn>
    </v-flex>

    <v-flex sm4 mb-10 class="text-xs-center">
      <v-btn large v-on:click='todaySet()'>
        {{start}}
      </v-btn>
      <!-- <v-select v-model="type" :items="typeOptions" label="Type"></v-select> -->
    </v-flex>

    <v-flex sm4 class="text-sm-right text-xs-center">
      <v-btn large @click="$refs.calendar.next()">
        Next
        <v-icon right dark>keyboard_arrow_right</v-icon>
      </v-btn>
    </v-flex>

    <!-- Calendar -->
    <v-flex xs12 class="mb-3">
      <v-sheet height="1000px">
                                                                      <!-- today -->      
        <v-calendar ref="calendar" v-model="start" :type="type" :end="end" color="error">
          <template v-slot:day="{ date }" style="height:auto">
            <!-- start my event -->
            <template v-for="event in eventsMap[date]">
              <v-menu :key="event.title" v-model="event.open" full-width offset-x>
                <template v-slot:activator="{ on }">
                  <div v-if="!event.time" v-ripple class="my-event" v-on="on" v-html="event.title"></div>
                </template>
                <div style="width:500px;">
                <v-card color="grey lighten-4">
                  <v-toolbar color="primary" dark>

                    <v-toolbar-title style="font-size:0.9rem" v-html="event.title" v-on:click="toDetail(event.uid)"></v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn v-if='event.favoriteCon' v-on:click="unfavorite(event.uid)" icon>
                      <v-icon color='pink'>favorite</v-icon>
                    </v-btn>
                    <v-btn v-else v-on:click="favorite(event.uid)" icon>
                      <v-icon>favorite</v-icon>
                    </v-btn>

                  </v-toolbar>
                  <v-card-title primary-title style=" height: 500px;">
                      <v-img 
                        class="white--text mx-10"
                        max-width="80%" 
                        max-height="100%"
                        :src='event.img'
                         v-on:click="toDetail(event.uid)"
                        ></v-img>
                    <span v-html="event.details"></span>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn color="secondary">Cancel</v-btn>
                  </v-card-actions>
                </v-card>
                </div>
              </v-menu>
            </template>

            <!-- end event -->
            <template v-for="event in endEventsMap[date]">
              <v-menu :key="event.title" v-model="event.open" full-width offset-x>
                <template v-slot:activator="{ on }">
                  <div v-if="!event.time" v-ripple class="end-event" v-on="on" v-html="event.title"></div>
                </template>
                <div style="width:500px;">
                <v-card color="grey lighten-4" min-width="350px">
                  <v-toolbar color="gray" dark>

                    <v-toolbar-title style="font-size:0.9rem" v-html="event.title" v-on:click="toDetail(event.uid)"></v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn v-if='event.favoriteCon' v-on:click="unfavorite(event.uid)" icon>
                      <v-icon color='pink'>favorite</v-icon>
                    </v-btn>
                    <v-btn v-else v-on:click="favorite(event.uid)" icon>
                      <v-icon>favorite</v-icon>
                    </v-btn>

                  </v-toolbar>
                  <v-card-title gray-title style=" height: 500px;">
                      <v-img 
                        class="white--text mx-10"
                        max-width="80%" 
                        max-height="100%"
                        :src='event.img'
                         v-on:click="toDetail(event.uid)"
                      ></v-img>
                    <span v-html="event.details"></span>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn color="secondary">Cancel</v-btn>
                  </v-card-actions>
                </v-card>
                </div>
              </v-menu>
            </template>
          </template>
        </v-calendar>
      </v-sheet>
    </v-flex>
  </v-layout>
</template>

<script>
import firebase from "firebase";
import FirebaseService from "../../plugins/FirebaseService";
import "firebase/firestore";
import "firebase/auth";

export default {
  data: () => ({
    type: "month",
    start: "",
    end: "",
    typeOptions: [
      { text: "Day", value: "day" },
      { text: "4 Day", value: "4day" },
      { text: "Week", value: "week" },
      { text: "Month", value: "month" }
    ],
    endEvents: [],
    events: [
      // {
      //   title: 'test',
      //   details: 'test test',
      //   date: '2019-08-01',
      //   open: false,
      //   uid:0
      // },
    ]
  }),
  // get userInfo
  created() {
    // 현재 사용자 정보 불러오기
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        // User is signed in.
        this.userEmail = user.email;

        this.getUserConference(user.email)
      } else {
        // No user is signed in.
      }
    });

    // 컨퍼런스를 달력에 넣는 함수 실행하기
    this.conferenceInCalendar();

    // 현재 날짜 받기
    this.todaySet();
  },
  mounted() {},
  computed: {
    // convert the list of events into a map of lists keyed by date
    eventsMap() {
      const map = {};
      this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e));
      return map;
    },
    endEventsMap() {
      const map = {};
      this.endEvents.forEach(ee =>
        (map[ee.date] = map[ee.date] || []).push(ee)
      );
      return map;
    }
  },
  methods: {
    open(event) {
      alert(event.title);
    },
    // DB에 conference일정 달력에 넣는 함수
    async conferenceInCalendar() {
      const cic = await FirebaseService.getConferences();
      cic.forEach(c => {
        this.events.push({
          title: "(시) " + c.title,
          img:c.img,
          details: c.link,
          date: c.start,
          open: false,
          uid: c.title,
          favoriteCon: false
        }),
          this.endEvents.push({
            title: "(끝) " + c.title,
            details: c.link,
            img:c.img,
            date: c.end,
            open: false,
            uid: c.title,
            favoriteCon: false
          });
      });
    },
    toDetail(name) {
      location.href = "/conference/" + name;
    },
    todaySet() {
      var dateObject = new Date();
      var nYear = dateObject.getFullYear();
      var nMonth = dateObject.getMonth()+1;
      // if(nMonth < 10) {
      //   nMonth = '0'+nMonth;
      // };
      var nDate = dateObject.getDate();
      if(nDate < 10) {
        nDate = '0'+nDate;
      };
      this.start = nYear+'-'+nMonth+'-'+nDate
      // this.start = nMonth+' 월'
    },
    favorite(conf_id) {
      this.events.favoriteCon=true
      this.endEvents.favoriteCon=true
      FirebaseService.postMyConference(conf_id, this.userEmail)
      FirebaseService.postUserToConference(conf_id, this.userEmail).then(()=>location.href='/'
      )
    },
    unfavorite(conf_id) {
      this.events.favoriteCon=false
      this.endEvents.favoriteCon=false
      FirebaseService.deleteMyConference(conf_id, this.userEmail)
      FirebaseService.deleteUserToConference(conf_id, this.userEmail).then(()=>location.href='/')
    },

      // 내 컨퍼런스 구분
    // Conference Detail
    async getConferenceDetail(con_param) {
      const conDe = await FirebaseService.getConference(con_param);
      this.events.forEach(evt =>{
        if(evt.uid == conDe.title){
          evt.favoriteCon = true
        }
      })
      this.endEvents.forEach(evt =>{
        if(evt.uid == conDe.title){
          evt.favoriteCon = true
        }
      })
      // this.events.push({
      //     title: "(시) " + conDe.title,
      //     details: conDe.link,
      //     date: conDe.start,
      //     open: false,
      //     uid: conDe.title
      // });
      // this.endEvents.push({
      //     title: "(끝) " + conDe.title,
      //     details: conDe.link,
      //     date: conDe.end,
      //     open: false,
      //     uid: conDe.title
      // })
    },
    // 사용자 별 ConferenceID
    async getUserConference(user_param) {
      const userCon = await FirebaseService.getUserConference(user_param);
      userCon.forEach(eachCon => {
        this.getConferenceDetail(eachCon);
      });
    },





  }
};
</script>

<style lang="stylus" scoped>
.my-event {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-radius: 2px;
  background-color: #42A5F5;
  color: #ffffff;
  border: 1px solid #42A5F5;
  width: 100%;
  font-size: 12px;
  padding: 3px;
  cursor: pointer;
  margin-bottom: 1px;
}

.end-event {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-radius: 2px;
  background-color: #A9A9A9;
  color: #ffffff;
  border: 1px solid #A9A9A9;
  width: 100%;
  font-size: 12px;
  padding: 3px;
  cursor: pointer;
  margin-bottom: 1px;
}

.v-calendar-weekly__week{
  height : auto;
}

</style>
