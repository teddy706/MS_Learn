import React, { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw, Timer as TimerIcon } from 'lucide-react';

export default function StudyTimer() {
  const [secondsLeft, setSecondsLeft] = useState(25 * 60); // 25 min default
  const [isActive, setIsActive] = useState(false);
  const [timerMode, setTimerMode] = useState(25); // 25m, 15m, 5m

  useEffect(() => {
    let interval = null;
    if (isActive && secondsLeft > 0) {
      interval = setInterval(() => {
        setSecondsLeft(prev => prev - 1);
      }, 1000);
    } else if (secondsLeft === 0) {
      setIsActive(false);
      alert('⏰ 학습 시간 뽀모도로 타이머가 완료되었습니다! 잠시 휴식을 취하세요.');
    }
    return () => clearInterval(interval);
  }, [isActive, secondsLeft]);

  const toggleTimer = () => setIsActive(!isActive);

  const resetTimer = (mins = timerMode) => {
    setIsActive(false);
    setTimerMode(mins);
    setSecondsLeft(mins * 60);
  };

  const formatTime = (totalSecs) => {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  };

  return (
    <div className="timer-widget">
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem', color: 'var(--text-secondary)' }}>
        <TimerIcon size={22} className="text-primary" />
        <h3 style={{ fontSize: '1.2rem', fontWeight: 700 }}>뽀모도로 집중 학습 타이머</h3>
      </div>

      <div className="timer-display">
        {formatTime(secondsLeft)}
      </div>

      {/* Preset Modes */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
        {[
          { label: '25분 집중', mins: 25 },
          { label: '15분 학습', mins: 15 },
          { label: '5분 휴식', mins: 5 },
        ].map(mode => (
          <button
            key={mode.mins}
            className={`btn ${timerMode === mode.mins ? 'btn-primary' : 'btn-secondary'}`}
            style={{ padding: '0.35rem 0.75rem', fontSize: '0.85rem' }}
            onClick={() => resetTimer(mode.mins)}
          >
            {mode.label}
          </button>
        ))}
      </div>

      {/* Controls */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem' }}>
        <button
          className="btn btn-primary"
          style={{ padding: '0.65rem 1.5rem', fontSize: '1rem' }}
          onClick={toggleTimer}
        >
          {isActive ? <Pause size={18} /> : <Play size={18} />}
          <span>{isActive ? '일시 정지' : '시작하기'}</span>
        </button>

        <button
          className="btn btn-secondary"
          style={{ padding: '0.65rem 1rem' }}
          onClick={() => resetTimer()}
          title="타이머 리셋"
        >
          <RotateCcw size={18} />
        </button>
      </div>
    </div>
  );
}
