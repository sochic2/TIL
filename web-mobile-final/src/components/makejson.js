
const admin = require('firebase-admin');
var serviceAccount = require('../services/serviceAccountKey.json');

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
})

let db = admin.firestore();
let CONFERENCE = db.collection('conference');


const axios = require('axios');
const request = require('request');
const cheerio = require('cheerio');


const crawling = (TARGER_URL) => axios.get(TARGER_URL)
    .then(res => {
        const conference = new Object();
        const $ = cheerio.load(res.data);
        const $LIST = $('div.ms-list ul.list').children('li');
        $LIST.each(function (i) {
            

            if (i>=1) {
                // 마감여부
                const obj = new Object();

                obj.dday = $(this).find('span.dday').text()

                // 개별링크
                const link ="https://www.wevity.com/?c=find&s=1&gub=1&cidx=21"+ $(this).find('div.tit a').attr('href')
                axios.get(link)
                .then(res => {
                    
                    // console.log(res.data)
                    const $ = cheerio.load(res.data)
                    const $example = $('div.contest-detail')

                    $example.each(function() {
                        const title = $(this).find("div.tit-area h6.tit").text()
                        obj.title = $(this).find("div.tit-area h6.tit").text()
                        // console.log(title)
                        const img = "https://www.wevity.com"+$(this).find("div.cd-area div.img img").attr("src")
                        obj.img = "https://www.wevity.com"+$(this).find("div.cd-area div.img img").attr("src")
                    })

                    const $list = $('div.info ul.cd-info-list').children('li')
                    
                    $list.each(function (i) {
                        if (i===0){
                            // 분야

                            obj.field = $(this).text().split('\n\t\t\t\t\t').slice(2, 100)[0].replace('\t\t\t\t', '').split(',')

                            
                        } else if (i===1) {
                            // 응모대상

                            obj.target = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")

                    
                        } else if (i===2) {
                            // 주최
                            const host = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")
                            obj.host = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")

                        } else if (i===3) {
                            // 후원
                            const sponsor = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")
                            if (sponsor==='') {
                                obj.sponsor = 'None'

                            } else {
                                obj.sponsor = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")
                            }

                    
                        } else if (i===4) {
                            // 기간

                            obj.start = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split('\t')[0].split(' ~ ')[0]

                            obj.end = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split('\t')[0].split(' ~ ')[1]

                        } else if (i===5) {
                            // 총상금
                            const prize = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")
                            if (prize==="") {
                                obj.prize = "None"
                            } else {
                            obj.prize = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")
                            }

                        } else if (i===6) {
                            // 1등상금
                        const first_prize = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")
                        if (first_prize==="") {
                            obj.first_prize = "None"
                        } else {
                            obj.first_prize = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")
                        }

                        } else if (i===7) {
                            // 홈페이지
                        
                            obj.homepage = $(this).text().split('\n\t\t\t\t\t').slice(2, 4)[0].split(',')[0].replace( /(\s*)/g, "")

                        }
                })
            
                // console.log(obj)
                CONFERENCE.doc(obj.title).set(obj)

            })

            }
        })
        // console.log(conference)
    }
    )

    .catch(error => console.error(error))

const URL = ["https://www.wevity.com/?c=find&s=1&gub=1&cidx=21", "https://www.wevity.com/?c=find&s=1&gub=1&cidx=20", "https://www.wevity.com/?c=find&s=1&gub=1&cidx=22", "https://www.wevity.com/?c=find&s=1&gub=1&cidx=22&gp=2"];
URL.forEach(function(i) {

    crawling(i)

})
    
