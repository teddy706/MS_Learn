import React, { useState } from 'react';
import { ChevronDown, ChevronUp, ExternalLink, Clock, FileText, CheckCircle2, HelpCircle, BookOpen } from 'lucide-react';

export default function ModuleCard({ 
  module, 
  completedUnitIds, 
  onToggleUnit, 
  onOpenNotes, 
  userNotes,
  defaultExpanded = false 
}) {
  const [isExpanded, setIsExpanded] = useState(defaultExpanded);

  const completedUnitsInModule = module.units.filter(u => completedUnitIds.includes(u.id));
  const isModuleFullyCompleted = completedUnitsInModule.length === module.units.length;
  const moduleProgressPercent = Math.round((completedUnitsInModule.length / module.units.length) * 100);

  return (
    <div className={`module-card ${isModuleFullyCompleted ? 'completed-module' : ''}`}>
      {/* Header */}
      <div className="module-header" onClick={() => setIsExpanded(!isExpanded)}>
        <div className="module-header-left">
          <span className="module-code-badge">{module.code}</span>
          <div>
            <h3 className="module-title">{module.title}</h3>
            <div className="module-meta-info" style={{ marginTop: '0.2rem' }}>
              <span className="badge-tag">{module.category}</span>
              <span><Clock size={13} style={{ display: 'inline', marginRight: '3px' }} /> 약 {module.totalTimeMinutes}분</span>
              <span>{module.xp} XP</span>
              <span style={{ color: isModuleFullyCompleted ? 'var(--accent-emerald)' : 'var(--text-muted)', fontWeight: 600 }}>
                {completedUnitsInModule.length}/{module.units.length} 완료 ({moduleProgressPercent}%)
              </span>
            </div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <a
            href={module.url}
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-secondary"
            style={{ padding: '0.4rem 0.75rem', fontSize: '0.8rem' }}
            onClick={(e) => e.stopPropagation()}
            title="MS Learn 모듈 메인 페이지로 이동"
          >
            모듈 원본 <ExternalLink size={13} />
          </a>
          <button className="btn-icon" style={{ width: '32px', height: '32px' }}>
            {isExpanded ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
          </button>
        </div>
      </div>

      {/* Accordion Content */}
      {isExpanded && (
        <div className="units-container">
          <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '1rem', padding: '0 0.5rem' }}>
            {module.description}
          </p>

          {module.units.map((unit, index) => {
            const isCompleted = completedUnitIds.includes(unit.id);
            const hasNote = Boolean(userNotes[unit.id] && userNotes[unit.id].trim());

            return (
              <div 
                key={unit.id} 
                className={`unit-row ${isCompleted ? 'completed' : ''}`}
              >
                <div className="unit-left">
                  <input
                    type="checkbox"
                    className="unit-checkbox"
                    checked={isCompleted}
                    onChange={() => onToggleUnit(unit.id)}
                    id={`chk-${unit.id}`}
                  />
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)', width: '24px' }}>
                    {String(index + 1).padStart(2, '0')}
                  </span>
                  
                  {unit.type === 'quiz' ? (
                    <HelpCircle size={16} style={{ color: 'var(--accent-purple)' }} />
                  ) : unit.type === 'summary' ? (
                    <BookOpen size={16} style={{ color: 'var(--accent-amber)' }} />
                  ) : (
                    <FileText size={16} style={{ color: 'var(--primary)' }} />
                  )}

                  <a
                    href={unit.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="unit-title-link"
                    title="MS Learn 단원 페이지 개별 이동"
                  >
                    <span>{unit.title}</span>
                    <ExternalLink size={13} style={{ opacity: 0.6 }} />
                  </a>
                </div>

                <div className="unit-right">
                  <span className="unit-time">
                    <Clock size={13} /> {unit.timeMinutes}분
                  </span>

                  <button
                    className={`btn ${hasNote ? 'btn-primary' : 'btn-secondary'}`}
                    style={{ padding: '0.3rem 0.6rem', fontSize: '0.78rem' }}
                    onClick={() => onOpenNotes(unit)}
                    title="단원 메모 작성/수정"
                  >
                    <FileText size={13} />
                    {hasNote ? '메모 작성됨' : '메모 추가'}
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
