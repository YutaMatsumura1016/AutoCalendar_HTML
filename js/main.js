//全角撲滅
function zenhan(yotei) {
  const zen = "０１２３４５６７８９／（）、～　";
  const han = "0123456789/(),~ ";
  const dic = Object.fromEntries([...zen].map((c, i) => [c, han[i]]));
  const res = [...yotei].map(c => dic[c] || c).join("");
  return res;
}

//空白撲滅
function kuhaku(yotei_han){
  var i = 0;
  while(i<yotei_han.length){
    if(yotei_han != ""){
      if(yotei_han[0] == " "){
        yotei_han = yotei_han.trimStart()
      }
    return yotei_han;
    }
    i++;
  }
}

//本体
function hizukeni(yotei_han_kuhaku){
  var yoteiList = [];
  var hizukeListm = [];
  var hizuke = "";
  var hizukeListd = [];
  var naiyouList = [];
  var hizukem = "";
  var hizuked = "";
  var naiyou = "";

  var i = 0;
  var t = 0;
  //一文字ずつに分割
  while(i<yotei_han_kuhaku.length){
    yoteiList.push(yotei_han_kuhaku[i]);
    i++;
  }

  //分析
  while(t<yoteiList.length){
    //B月は入っていて、日はまだ(日を1桁入れるところまで)
    if(hizukeListm.length>0 && hizukeListm.length<=2 && hizukeListd.length == 0){
      // console.log("B")
      //B1今回が/
      if(yoteiList[t] == "/" || yoteiList[t] == "月"){
        hizuke = "/";
      }
      //B2前回が数字
      else if(!isNaN(yoteiList[t-1])){
        //B21今回も数字
        if(!isNaN(yoteiList[t])){
          hizukeListm.push(yoteiList[t]);
        }
        //B22今回は数字ではない
        else{
          hizukeListm = [];
          hizuke = "";
        }
      }
      //B3前回が/
      else if(hizuke == "/"){
        //B31今回は数字
        if(!isNaN(yoteiList[t])){
          hizukeListd.push(yoteiList[t]);
        }
        //B32今回は数字ではない
        else{
          hizukeListm = [];
          hizuke = "";
        }
      }
    }
    //F日に,が入っていて、月の,が1個以下。または日の,が2個以上
    else if(((hizukeListd.join("").includes(",")) && (hizukeListm.filter(x => x === ",").length<2)) || (hizukeListd.filter(x => x === ",").length > 1)){
      // console.log("F")
      //F1今回が数字
      if(!isNaN(yoteiList[t])){
        //F11次も数字
        if(!isNaN(yoteiList[t+1])){
          hizukeListd.push(yoteiList[t]);
        }
        //F12次は数字ではない
        else{
          hizukeListd.push(yoteiList[t]);
          //F121次が区切り文字ではない
          if (!(yoteiList[t+1] == "." || yoteiList[t+1] == "," || yoteiList[t+1] == "~")){
            naiyouList = yoteiList.slice(t+1);
          }
        }
      }
      //F2今回が区切り
      else if(yoteiList[t] == "." || yoteiList[t] == "," || yoteiList[t] == "~"){
        // console.log(yoteiList[t])
        //F21次の桁が数字ではない
        if(isNaN(parseInt(yoteiList[t+1]))){
          naiyouList = yoteiList.slice(t+1);
          break;
        }
        //F22次の桁が数字
        //次かその次に月がある
        if(yoteiList[t+2] == "/" || yoteiList[t+2] == "月" || yoteiList[t+3] == "/" || yoteiList[t+3] == "月"){
          hizukeListm.push(",");
        }
        //F23ない
        else{
          hizukeListd.push(",");
        }
      }
      //F3入れ終わり
      else if(isNaN(yoteiList[t])){
        naiyouList = yoteiList.slice(t);
        break;
      }
    }
    //E月に,が入っている
    else if("," in hizukeListm){
      // console.log("E")
      //E1今回が数字
      if(!isNaN(yoteiList[t])){
        hizukeListm.push(yoteiList[t]);
      }
      //E2今回が月
      else if(yoteiList[t] == "/" || yoteiList[t] == "月"){
        hizukeListd.push(",");
      }
      //E3今回は文字(例外)
      else{
        naiyouList = yoteiList.slice(t+1);
      }
    }
    //C日が1桁入っている
    else if(hizukeListd.length == 1){
      // console.log("C")
      //C1今回の桁も数字
      if(!isNaN(yoteiList[t])){
        hizukeListd.push(yoteiList[t]);
      }
      //C2今回の桁は区切り
      else if(yoteiList[t] == "." || yoteiList[t] == "," || yoteiList[t] == "~"){
        //C21次の桁が数字ではない
        if(isNaN(parseInt(yoteiList[t+1]))){
          naiyouList = yoteiList.slice(t);
          break;
        }
        //次の桁が数字
        //C22次かその次に月がある
        else if(yoteiList[t+2] == "/" || yoteiList[t+2] == "月" || yoteiList[t+3] == "/" || yoteiList[t+3] == "月"){
          hizukeListm.push(",");
        }
        //C23ない
        else{
          hizukeListd.push(",");
        }
      }
      //C3今回の桁は文字
      else{
        naiyouList = yoteiList.slice(t);
        break;
      }
    }
    //D日付が2桁入っている
    else if(hizukeListd.length==2){
      // console.log("D")
      //D1今回の桁が区切りでない
      if (!(yoteiList[t] == "." || yoteiList[t] == "," || yoteiList[t] == "~")){
        naiyouList = yoteiList.slice(t);
        break;
      }
      //D2今回の桁が区切り
      else if(yoteiList[t] == "." || yoteiList[t] == "," || yoteiList[t] == "~"){
        //D21次の桁が数字ではない
        if(isNaN(parseInt(yoteiList[t+1]))){
          naiyouList = yoteiList.slice(t+1);
          break;
        }
        //D22次の桁が数字
        //次かその次に月がある
        if(yoteiList[t+2] == "/" || yoteiList[t+2] == "月" || yoteiList[t+3] == "/" || yoteiList[t+3] == "月"){
          hizukeListm.push(",");
        }
        //D23ない
        else{
          hizukeListd.push(",");
        }
      }
    }
                
    //A何も入っていない
    else if(!isNaN(yoteiList[t])){
      // console.log("A");
      hizukeListm.push(yoteiList[t]);
    }
    else{
      // console.log("else");
    }
    t++;
  }

  //月の数を合わせる
  var c = 0;
  var d = 0; //月の,の数
  var e = 0;
  var f = 0; //日の,の数
  var m = "";

  while(c<hizukeListm.length){
    if(hizukeListm[c] == ","){
      d++;
    }
    c++;
  }
  while(e<hizukeListd.length){
    if(hizukeListd[e] == ","){
      f++;
    }
    e++;
  }
  if(d<f){
    t=0;
    while(t<hizukeListm.length){
      m=m+hizukeListm[t];
      t++;
    }
    i=0;
    while(i<f){
      hizukeListm.push(",");
      hizukeListm.push(m);
      i++;
    }
  }
  //文字列化
  var i = 0;
  while(i<hizukeListm.length){
    hizukem = hizukem + hizukeListm[i];
    i++;
  }
  var t = 0;
  while(t<hizukeListd.length){
    hizuked = hizuked + hizukeListd[t];
    t++;
  }
  //先頭空白削除
  if(naiyouList != []){
    if(naiyouList[0] == " "){
      naiyouList = naiyouList.trimStart();
    }
    var w = 0
    while(w<naiyouList.length){
      naiyou = naiyou + naiyouList[w];
      w++;
    }
  }

  var retArr = [hizukem, hizuked, naiyou];
  return retArr;
}

//曜日削除
function youbiDel(naiyou){
  var youbiArray = ["月","火","水","木","金","土","日"];
  while(true){
    if(naiyou[0] == "("){
      if(youbiArray.includes(naiyou[1])){
        var i=0;
        while(i<naiyou.length){
          if(naiyou[i] == ")"){
            naiyou = naiyou.slice(i+1);
            break;
          }
          i++;
        }
      }
    }
    else if(youbiArray.includes[0]){
      if(naiyou[1] == "曜"){
        if(naiyou[2] == "日"){
          naiyou = naiyou.slice(3);
        }
        else{
          naiyou = naiyou.slice(2);
        }
      }
      else{
        naiyou = naiyou.slice(1);
      }
    }
    else if(naiyou[0] == "," || naiyou[0] == "." || naiyou[0] == "~"){
      naiyou = naiyou.slice(1);
    }
    else{
      return(naiyou);
    }
  }
}

//main
function yoteiAuto() {
  var mail = document.getElementById("input_id").value;
  // var schedule = document.getElementById("input_data").value;

  var schedule = `【今後のスケジュール】

  今後の祭り
  7/29(土)遠藤さん結婚式
  7/30(日)上矢部
  8/5(土)東小
  8/19(土)永田台小
  8/26.27(土.日)どまつり
  9/9(土)センター南祭り
  9/10(日)センター南祭り予備日
  9717(日)相模原RANBU
  9/24(日)AQUA祭り
  10/1(日)ちばよさ
  10/21.22(土.日)横よさ
  11/4.5(土.日)どりよさ
  11/12(日)町田
  11/25.26(土日)テレどま
  12/3(日)秦野
  
  画練習日(文:和持に参加して欲しい日)
  8/20(日)どまつり練(ステージ)
  9/3(日)横よさ隊列練(ステージ)
  9/18(月)横よさ隊列練(ステージ)
  9/23(土)ちばよさ練(パレード)
  9/30(土)ちばよさ練(ステージ&パレード)
  10/8(日)横よさ練(ステージ&パレード)
  10/14(土)横よさ隊列練(パレード)
  10/15(日)横よさ隊列練(ステージ&パレード)
  10/29(日)どりよさ練(ステージ&パレード)
  11/11(土)町田練(ステージ&パレード)
  11/19(日)秦野練
  12/2(土)破天荒ラスト練`

  
  scheduleList = [];
  yoteimList = [];
  yoteidList = [];
  naiyouList = [];
  var i = 0;

  // 予定の追加
  var scheduleList = schedule.split(/\n/);

  try{
    //内容取得
    while(i<scheduleList.length){
      //整形
      var yotei = scheduleList[i];
      yotei_kuhaku = kuhaku(yotei);
      if(yotei!=""){
        var yotei_han_kuhaku = zenhan(yotei_kuhaku);
        //内容取得
        if(yotei_han_kuhaku != ""){
          var hizukeniRe = hizukeni(yotei_han_kuhaku);
          var hizukem = hizukeniRe[0];
          var hizuked = hizukeniRe[1];
          var naiyou = hizukeniRe[2];
          if(naiyou != ""){
            naiyou = youbiDel(naiyou);
            console.log(naiyou)
            yoteimList.push(hizukem);
            yoteidList.push(hizuked);
            naiyouList.push(naiyou);
          }
        }
      }
      i++;
    }
  
  } catch {
    return("予定の取得中にエラーが発生しました。");
  }



}