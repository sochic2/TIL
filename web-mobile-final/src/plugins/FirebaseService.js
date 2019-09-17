import firebase from 'firebase/app'
import 'firebase/firestore'
import 'firebase/auth'

const POSTS = 'posts'
const PORTFOLIOS = 'portfolios'

// Your web app's Firebase configuration
const firebaseConfig = {
	apiKey: "AIzaSyBsF3jesOhPlj4_B9246R4ajpg0--8QY-0",
	authDomain: "test-560e9.firebaseapp.com",
	databaseURL: "https://test-560e9.firebaseio.com",
	projectId: "test-560e9",
	storageBucket: "test-560e9.appspot.com",
	messagingSenderId: "1093388579226",
	appId: "1:1093388579226:web:f193b260cd66da2a"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const firestore = firebase.firestore()

export default {
	 // 탈퇴
	Withdrawl() {
		var user = firebase.auth().currentUser
		// console.log(user.email)
		firestore.collection('usertest').doc(user.email).delete()
		user.delete()
		.then(() => {
			location.href = '/'
		})
	},



  // alert
  alert() {
    return firestore.collection('alert').doc('alert')
    .get()
    .then(function(doc) {
      let data = doc.data()
      alert(data.content)
      return data
    })
  },
  // placeholder 가져오기
  getalert() {
    return firestore.collection('alert').doc('alert')
    .get()
    .then(function(doc) {
      let data = doc.data()
      // console.log(data.content)
      return data.content
    })
  },

  // alertchange
  alertchange(value) {

    let userDoc = firestore.collection('alert').doc('alert')
    userDoc.update(
      {content: value}
    )
    .then(()=> {
      location.href = '/admin'
    })
  },

  // check auth
  checkAuth(user_id) {
    return firestore.collection('usertest').doc(user_id)
    .get()
		.then(function(doc) {
			let data = doc.data()
			return data
		})
  },


  // auth change
  changeToAdmin(user_id) {
    let userDoc = firestore.collection('usertest').doc(user_id)
    userDoc.update(
      {
        권한: '관리자'
      }
    )
    .then(()=> {
      location.href = '/admin'
    })
  },

  changeToNormal(user_id) {
    let userDoc = firestore.collection('usertest').doc(user_id)
    userDoc.update(
      {
        권한: '새싹회원'
      }
    )
    .then(()=> {
      location.href = '/admin'
    })
  },

	// schedule test
	postSchedule(userEmail, title, details, date) {
		return firestore.collection('schedule').doc(userEmail).set({
			created_at: firebase.firestore.FieldValue.serverTimestamp(),
			date,
			details,
			title,
			userEmail,
		})
	},

  //get users
  getUsers() {
  const userCollection = firestore.collection('usertest')
  return userCollection
  .get()
  .then((docSnapshots) => {
    return docSnapshots.docs.map((doc) => {
      let data = doc.data()
      return data
    })
  })
},

// 현재 유저 권한 정보, 방문자, 관리자 라고 리턴하려면 .then 써야함
// routerjs 위쪽에서 사용
getUserAuth(user_id) {
  const userDocument = firestore.collection('usertest').doc(user_id)
  return userDocument
  .get()
  .then(function(doc) {
    let data = doc.data()
    return data.권한
  })
},
    // get conferences
    getConferences() {
		const conferenceCollection = firestore.collection('conference')
		return conferenceCollection
			.orderBy('start', 'desc')
			.get()
			.then((docSnapshots) => {
				return docSnapshots.docs.map((doc) => {
					let data = doc.data()
					// data.created_at = new Date(data.created_at.toDate())
					// console.log(doc.data())
					return data
				})
			})
	},

	// 사용자가 지정한 Conference가져오기
	getUserConference(userEmail) {
		const userConferenceCollection = firestore.collection('usertest').doc(userEmail).collection('conference')
		return userConferenceCollection
			.get()
			.then((querySnapshot) => {
				return querySnapshot.docs.map((doc) => {
					const userCid = doc.data().id
					return userCid
				})
			})
	},

	// 좋아요
	postMyConference(conf_id, user) {
		return firestore.collection('usertest').doc(user).collection('conference').doc(conf_id).set({
			id: conf_id
		})
	},
	// 좋아요시 컨퍼런스에 유저 정보 등록
	postUserToConference(conf_id, user) {
		return firestore.collection('conference').doc(conf_id).collection('user').doc(user).set({
			id: user
		})
	},
	// 좋아요 취소
	deleteMyConference(conf_id, user) {
		return firestore.collection('usertest').doc(user).collection('conference').doc(conf_id).delete()
	},
	deleteUserToConference(conf_id, user) {
		return firestore.collection('conference').doc(conf_id).collection('usertest').doc(user).delete()
	},
	// 좋아요 확인
	checkMyConference(conf_id, user) {
		const conferenceDocument = firestore.collection('usertest').doc(user).collection('conference').doc(conf_id)
  		return conferenceDocument
		.get()
		.then(function(doc) {
			let data = doc.data()
			return data
		  })
		.catch(function() {
			return []
		})
	},

	// 컨퍼런스 디테일
	getConference(conf_id) {
		const conferenceDocument = firestore.collection('conference').doc(conf_id)
		return conferenceDocument
			.get()
			.then((doc) => {
				let data = doc.data()
				return data
			})
	},

	// 컨퍼런스 수정
	updateConference(conf_id, title, start, end, img, link) {
		return firestore.collection('conference').doc(conf_id).update({
			title: title,
			start: start,
			end: end,
			img: img,
			link: link
		})
	},
	// 컨퍼런스 삭제(컨퍼런스, 유저 기록 모두)
	deleteConference(conf_id) {
		return firestore.collection('conference').doc(conf_id).delete()
	},
	deleteUserConference(user, conf_id) {
		return firestore.collection('usertest').doc(user).collection('conference').doc(conf_id).delete()
	},

	// 컨퍼런스 댓글들 가져오기
	getComments(conf_id) {
		const commentCollection = firestore.collection('conference').doc(conf_id).collection('comment')
		return commentCollection
			.orderBy('created_at')
			.get()
			.then((docSnapshots) => {
				return docSnapshots.docs.map((doc) => {
					let data = doc.data()
					return data
				})
			})
	},

	// 마크다운 생성
	postMarkdown(user, title, content, date) {
		return firestore.collection('usertest').doc(user).collection('markdown').add({
			user: user,
			title: title,
			content: content,
			date: date,
			created_at: firebase.firestore.FieldValue.serverTimestamp()
		}).then(function(docRef) {
			firestore.collection('usertest').doc(user).collection('markdown').doc(docRef.id).update({
				id: docRef.id
			})
		})
	},
	// 마크다운 가져오기
	getMarkdowns(user) {
		const markdownCollection = firestore.collection('usertest').doc(user).collection('markdown')
		return markdownCollection
		.orderBy('date')
		.get()
		.then((docSnapshots) => {
			return docSnapshots.docs.map((doc) => {
				let data = doc.data()
				return data
			})
		})
	},
	// 마크다운 삭제
	deleteMarkdown(user, md_id) {
		return firestore.collection('usertest').doc(user).collection('markdown').doc(md_id).delete()
	},
	// 마크다운 디테일
	getMarkdown(user, md_id) {
		const markdownDocument = firestore.collection('usertest').doc(user).collection('markdown').doc(md_id)
		return markdownDocument
			.get()
			.then((doc) => {
				let data = doc.data()
				return data
			})
	},

	// 댓글 생성
	postComment(conf_id, user, content) {
		return firestore.collection('conference').doc(conf_id).collection('comment').add({
			user: user,
			content: content,
			created_at: firebase.firestore.FieldValue.serverTimestamp()
		}).then(function (docRef) {
			firestore.collection('conference').doc(conf_id).collection('comment').doc(docRef.id).update({
				id: docRef.id
			}),
				firestore.collection('usertest').doc(user).collection('comment').doc(docRef.id).set({
					conference: conf_id,
					content: content,
					id: docRef.id
				})
		})
	},

	// 댓글 수정
	updateComment(conf_id, comm_id, content) {
		return firestore.collection('conference').doc(conf_id).collection('comment').doc(comm_id).update({
			content: content
		})
	},
	// 댓글 삭제(컨퍼런스, 유저 기록 모두)
	deleteComment(conf_id, comm_id) {
		return firestore.collection('conference').doc(conf_id).collection('comment').doc(comm_id).delete()
	},
	deleteUserComment(user, comm_id) {
		return firestore.collection('usertest').doc(user).collection('comment').doc(comm_id).delete()
	},

	// 회원가입시 user collection에 방문자 권한 부여
	signup(useremail) {
		return firestore.collection('usertest').doc(useremail).set({
			id: useremail,
			권한: '새싹회원'
		})
	},

	getPosts() {
		const postsCollection = firestore.collection(POSTS)
		return postsCollection
			.orderBy('created_at', 'desc')
			.get()
			.then((docSnapshots) => {
				return docSnapshots.docs.map((doc) => {
					let data = doc.data()
					data.created_at = new Date(data.created_at.toDate())
					return data
				})
			})
	},
	postPost(title, body) {
		return firestore.collection(POSTS).add({
			title,
			body,
			created_at: firebase.firestore.FieldValue.serverTimestamp()
		})
	},
	getPortfolios() {
		const postsCollection = firestore.collection(PORTFOLIOS)
		return postsCollection
			.orderBy('created_at', 'desc')
			.get()
			.then((docSnapshots) => {
				return docSnapshots.docs.map((doc) => {
					let data = doc.data()
					data.created_at = new Date(data.created_at.toDate())
					return data
				})
			})
	},
	postPortfolio(title, body, img) {
		return firestore.collection(PORTFOLIOS).add({
			title,
			body,
			img,
			created_at: firebase.firestore.FieldValue.serverTimestamp()
		})
	},


	logging(name) {
		name = name ? name : 'Anonymous user'
		return firestore.collection('LOG').add({
			name,
			time: firebase.firestore.FieldValue.serverTimestamp()
		})
	},

	loginWithFacebook() {
		let provider = new firebase.auth.FacebookAuthProvider()
		return firebase.auth().signInWithPopup(provider).then(function (result) {
			let accessToken = result.credential.accessToken
			let user = result.user
			return result
		}).catch(function (error) {
			console.error('[Facebook Login Error]', error)
		})
	},

	loginWithGoogle() {
		let provider = new firebase.auth.GoogleAuthProvider()
		return firebase.auth().signInWithPopup(provider).then(function (result) {
			let accessToken = result.credential.accessToken
			let user = result.user
			return result
		}).catch(function (error) {
			console.error('[Google Login Error]', error)
		})
	},
	tojson(obj) {
		return firestore.collection(makejson).add({
			obj
		})
	}

}
