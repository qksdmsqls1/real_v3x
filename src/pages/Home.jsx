import React from 'react';
import "../css/Home.css";



function Home() {
  return (
    <div className="intro-wrapper">
      <h1 className="logo">MOMENT COFFEE</h1>
      <p className="welcome-text">
        “어서오세요, 모멘트 커피에 오신 걸 환영해요!<br />
        저는 직원 모모(하니)입니다!<br />
        저랑 같이 메뉴 골라볼까요? 😊☕”
      </p>
      <img src="/images/hani.png" alt="하니 캐릭터" className="hani-img" />
    </div>
  );
}

export default Home;
