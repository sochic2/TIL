<template>
    <v-container>
        <v-flex width="auto">
            <v-card class="mx-10">
                <v-card-title class='mx-6'><h5>{{confer.title}}</h5></v-card-title>
                <span class='mx-10' style='color:grey'>{{confer.start}} ~ {{confer.end}}</span>
                <button class="mx-10" v-on:click="Like()" style='float: right'><v-icon id='likebtn'></v-icon></button>
                <v-img v-on:click="tohome(confer.img)"
                class="white--text mx-10 my-4"
                width="50%"
                text-align="center"
                :src='confer.img'></v-img>
                <div class="mx-10 my-4">
                    <div class='my-2' style='color:grey'>{{confer.dday}}</div>
                    <div class='my-2' style='color:grey'>{{confer.host}}</div>
                    <span class='my-2' style='color:grey' v-for="field in confer.field">
                        <span v-if='field === confer.field[0]'>{{field}}</span>
                        <span v-else>, {{field}}</span>
                    </span>
                    <br>
                    <div class='my-2'><a v-on:click="tohome(confer.homepage)">링크가기</a></div>
                    <br style='height: 3px'>
                </div>
            </v-card>
            <br>
            <div v-if='userchk' class='mx-10'>
                <!-- 댓글 작성 -->
                <div>
                댓글 : <input type='text' class="mb-2" id='contentfield' style="background-color: #F0F8FF;"><input type='submit' value='  작성' v-on:click="postComment()"> 
                <!-- 댓글 수정 모달 -->
                </div>
                <v-dialog v-model="dialogc" width="500">
                    <!-- 댓글 리스트 -->
                    <template v-slot:activator="{ on }">
                        <v-flex v-for="(i, index) in comments.length" v-bind:key='index'>
                            <span>{{comments[i-1].user}} : </span>
                            <span>{{comments[i-1].content}} </span>
                            <!-- <button v-on:click="updateComment(comments[i-1].id)"> update </button> -->
                            <div>
                            <v-btn text v-on="on" v-on:click='abc(comments[i-1].content, comments[i-1].id)'>
                                <p>update</p>
                            </v-btn>
                            <v-btn text>
                                <p v-on:click="deleteComment(comments[i-1].id)">delete</p>
                            </v-btn>
                            </div>
                        </v-flex>
                    </template>
                    <v-card>
                        <v-card-title class="headline grey lighten-2" primary-title>댓글 수정</v-card-title>
                        <v-card-text>
                            <v-layout wrap>
                                <textarea id='textarea' style="background-color: #F0F8FF;">{{commentcontent}}</textarea>
                            </v-layout>
                        </v-card-text>

                        <v-divider></v-divider>

                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="primary" text v-on:click="updateComment(commentid)">update</v-btn>
                            <v-btn color="primary" text @click=" dialogc = false">닫기</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </div>
        </v-flex>
    </v-container>
</template>

<script>
                                                                               
import firebase from "firebase";
import FirebaseService from '../plugins/FirebaseService';
// import "firebase/firestore";

export default {
    data() {
        return {
            confer: [],
            comments: [],
            userEmail: '',
            likey: '',
            fields: '',
            dialogc: false,
            commentcontent: [],
            commentid: '',
            userchk: false
        }
    },
    created() {
        // 현재 사용자 정보 불러오기
        firebase.auth().onAuthStateChanged(user => {
            if (user) {
                // User is signed in.
                this.userEmail = user.email;
                this.userchk = true
                this.checkLike(this.userEmail)
                .then(() => {
                    const likebtn = document.getElementById('likebtn')

                    if(this.likey === undefined) {
                        likebtn.innerText = 'favorite_border'

                    } else {
                        likebtn.innerText = 'favorite'
                    }
                })
            } else {
                // No user is signed in.
                this.userEmail = 'Guest'
                this.userchk = false
            }
        })
    },
    mounted () {
        this.getDetail(),
        this.getComments()
    },
    methods: {
        async getDetail() {
            this.confer = await FirebaseService.getConference(this.$route.params.id)
        },
        async getComments() {
            this.comments = await FirebaseService.getComments(this.$route.params.id)
        },
        async checkLike(user) {
            this.likey = await FirebaseService.checkMyConference(this.$route.params.id, user)
            // console.log(1)
            // console.log(this.likey)
        },
        updateComment(comm_id) {
            FirebaseService.updateComment(this.$route.params.id, comm_id, textarea.value)
            .then(()=>{
                location.href = '/conference/'+this.$route.params.id
            })
        },
        deleteComment(comm_id) {
            FirebaseService.deleteComment(this.$route.params.id, comm_id)
            FirebaseService.deleteUserComment(this.userEmail, comm_id)
            .then(()=>{
                location.href = '/conference/'+this.$route.params.id
            })
        },
        postComment() {
            FirebaseService.postComment(this.$route.params.id, this.userEmail, contentfield.value)
            .then(()=>{
                location.href = '/conference/'+this.$route.params.id
            })
        },
        LikeConference() {
            FirebaseService.postMyConference(this.$route.params.id, this.userEmail)
            FirebaseService.postUserToConference(this.$route.params.id, this.userEmail)
            .then(()=>{
                location.href = '/conference/'+this.$route.params.id
            })
        },
        UnLikeConference() {
            FirebaseService.deleteMyConference(this.$route.params.id, this.userEmail)
            FirebaseService.deleteUserToConference(this.$route.params.id, this.userEmail)
            .then(()=>{
                location.href = '/conference/'+this.$route.params.id
            })
        },
        Like() {
            if(this.likey === undefined) {
                this.LikeConference()
            } else {
                this.UnLikeConference()
            }
        },
        tohome(url) {
            window.open(url)
        },
        abc(content, id) {
            this.commentcontent = content
            this.commentid = id
        }
    }
}
</script>