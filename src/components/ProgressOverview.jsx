import React from 'react';
import { CheckCircle2, Clock, Zap, Target } from 'lucide-react';

export default function ProgressOverview({ totalUnits, completedUnitIds, modulesData }) {
  const completedCount = completedUnitIds.length;
  const progressPercent = totalUnits > 0 ? Math.round((completedCount / totalUnits) * 100) : 0;

  // Calculate total study time and remaining time
  let totalTimeMinutes = 0;
  let completedTimeMinutes = 0;
  let totalXP = 0;
  let earnedXP = 0;

  modulesData.forEach(module => {
    totalXP += module.xp || 0;
    let moduleCompletedCount = 0;
    
    module.units.forEach(unit => {
      totalTimeMinutes += unit.timeMinutes;
      if (completedUnitIds.includes(unit.id)) {
        completedTimeMinutes += unit.timeMinutes;
        moduleCompletedCount++;
      }
    });

    if (module.units.length > 0 && moduleCompletedCount === module.units.length) {
      earnedXP += module.xp || 0;
    }
  });

  const remainingTimeMinutes = totalTimeMinutes - completedTimeMinutes;

  const formatHoursMinutes = (totalMins) => {
    const hours = Math.floor(totalMins / 60);
    const mins = totalMins % 60;
    if (hours === 0) return `${mins}분`;
    return `${hours}시간 ${mins}분`;
  };

  return (
    <div className="progress-card">
      {/* Percentage Main Stat */}
      <div className="stat-item">
        <div className="stat-label">전체 학습 진도율</div>
        <div className="stat-value-huge">{progressPercent}%</div>
        <div className="progress-bar-container">
          <div 
            className="progress-bar-fill" 
            style={{ width: `${progressPercent}%` }} 
          />
        </div>
      </div>

      {/* Stats Summary Grid */}
      <div className="meta-stats-grid">
        <div className="meta-stat-box">
          <div className="stat-label" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <CheckCircle2 size={15} className="text-primary" /> Completed Units
          </div>
          <div className="meta-stat-val">
            {completedCount} / {totalUnits} 단원 완료
          </div>
        </div>

        <div className="meta-stat-box">
          <div className="stat-label" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <Clock size={15} style={{ color: 'var(--accent-amber)' }} /> 남은 예상 시간
          </div>
          <div className="meta-stat-val">
            {formatHoursMinutes(remainingTimeMinutes)}
          </div>
        </div>

        <div className="meta-stat-box">
          <div className="stat-label" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <Target size={15} style={{ color: 'var(--accent-purple)' }} /> 총 학습 커리큘럼
          </div>
          <div className="meta-stat-val">
            {modulesData.length}개 모듈 ({formatHoursMinutes(totalTimeMinutes)})
          </div>
        </div>

        <div className="meta-stat-box">
          <div className="stat-label" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <Zap size={15} style={{ color: 'var(--accent-emerald)' }} /> 획득 XP
          </div>
          <div className="meta-stat-val">
            {earnedXP.toLocaleString()} / {totalXP.toLocaleString()} XP
          </div>
        </div>
      </div>

      {/* Motivational Tag */}
      <div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'flex-end' }}>
        <span className="badge-tag" style={{ backgroundColor: 'var(--primary-light)', color: 'var(--primary)', padding: '0.5rem 0.8rem', fontSize: '0.85rem' }}>
          🎯 AB-100 목표 달성중!
        </span>
        <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '0.5rem' }}>
          MS Learn 공식 가이드 연동
        </span>
      </div>
    </div>
  );
}
