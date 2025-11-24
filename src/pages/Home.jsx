import React, { useEffect, useState } from "react";
import "../css/Home.css";

function Home({ onStart }) {
  const [fadeIn, setFadeIn] = useState(false);
  const [typingText, setTypingText] = useState("");
  const [guideVisible, setGuideVisible] = useState(false);

  // 시간대별 환영 멘트
  const getGreeting = () => {
    const hour = new Date().getHours();
    if (hour < 12) return "좋은 아침이에요! ☀️";
    if (hour < 18) return "좋은 오후네요! 🌤️";
    return "좋은 저녁이에요! 🌙";
  };

  const greeting = getGreeting();

  // 타이핑 애니메이션
  const fullSentence =
    "모멘트 커피에 오신 걸 환영해요! 저는 직원 하니예요. 편하게 말 걸어주세요. ☕️😊";

  useEffect(() => {
    setFadeIn(true);

    let index = 0;
    const interval = setInterval(() => {
      setTypingText(fullSentence.slice(0, index));
      index++;
      if (index > fullSentence.length) {
        clearInterval(interval);
        setGuideVisible(true);
      }
    }, 40);

    return () => clearInterval(interval);
  }, []);

  // 랜덤 추천 문구
  const recommendations = [
    "‣ ‘아메리카노 추천해줘’라고 말해보세요!",
    "‣ ‘따뜻한 음료 뭐 있어?’라고 물어볼 수 있어요.",
    "‣ ‘인기 메뉴 알려줘’라고 해보세요!",
    "‣ 화면을 터치하면 바로 주문이 시작돼요!"
  ];

  const randomTip = recommendations[Math.floor(Math.random() * recommendations.length)];

  // 파티클 효과 (간단)
  const createParticles = (e) => {
    const body = document.body;
    const particle = document.createElement("div");
    particle.className = "particle";
    particle.style.left = `${e.clientX}px`;
    particle.style.top = `${e.clientY}px`;
    body.appendChild(particle);

    setTimeout(() => {
      particle.remove();
    }, 800);
  };

  return (
    <div
      className={`intro-wrapper ${fadeIn ? "fade-in" : ""}`}
      onClick={(e) => {
        createParticles(e);
        if (onStart) onStart();
      }}
    >
      <h1 className="logo">MOMENT COFFEE</h1>
      <p className="sub-greeting">{greeting}</p>

      <p className="welcome-text typing">
        {typingText}
        <span className="cursor">|</span>
      </p>

      <img src="/images/hani.png" alt="하니 캐릭터" className="hani-img" />

      <button className="voice-button">
        <img src="/images/mic.png" alt="mic" />
        음성으로 주문하기
      </button>

      {guideVisible && (
        <div className="guide-banner slide-up">
          <p>{randomTip}</p>
        </div>
      )}
    </div>
  );
}

export default Home;
